#!/usr/bin/env python3
"""Poll OKX + Bitget + Hyperliquid. Write one JSONL row per successful cycle.

Run on a VPS, not this rate-limited sandbox:
  python3 recorder.py --hours 48 --out logs/bbo.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_cost():
    return json.loads((HERE / "cost.json").read_text())


def http_json(url: str, data: bytes | None = None, timeout: float = 15.0) -> dict:
    headers = {
        "User-Agent": "lagdesk-recorder/1.0",
        "Accept": "application/json",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def mid_spread(bid, ask):
    bid, ask = float(bid), float(ask)
    mid = (bid + ask) / 2.0
    spr = (ask - bid) / mid * 1e4 if mid else None
    return bid, ask, mid, spr


class Backoff:
    def __init__(self):
        self.delay = 1.0

    def fail(self):
        time.sleep(self.delay)
        self.delay = min(self.delay * 2.0, 60.0)

    def ok(self):
        self.delay = 1.0


def fetch_okx():
    raw = http_json("https://www.okx.com/api/v5/market/tickers?instType=SWAP")
    return {row["instId"]: row for row in raw.get("data", [])}


def fetch_bitget():
    raw = http_json(
        "https://api.bitget.com/api/v2/mix/market/tickers?productType=USDT-FUTURES"
    )
    return {row["symbol"]: row for row in raw.get("data", [])}


def fetch_hl():
    return http_json(
        "https://api.hyperliquid.xyz/info",
        data=json.dumps({"type": "allMids"}).encode(),
    )


def row_for(coin: str, spec: dict, okx, bitget, hl):
    o = okx.get(spec["okx"])
    b = bitget.get(spec["bitget"])
    h_raw = hl.get(spec["hl"]) if hl else None
    out = {"coin": coin, "ok": False, "skip": None}

    if o is None:
        out["skip"] = "missing_okx"
        return out
    if b is None or not b.get("bidPr"):
        out["skip"] = "missing_bitget"
        return out

    o_bid, o_ask, o_mid, o_spr = mid_spread(o["bidPx"], o["askPx"])
    g_bid, g_ask, g_mid, g_spr = mid_spread(b["bidPr"], b["askPr"])
    cex_mid = (o_mid + g_mid) / 2.0
    cex_floor_bps = abs(o_mid - g_mid) / cex_mid * 1e4
    out.update(
        {
            "okx_bid": o_bid,
            "okx_ask": o_ask,
            "okx_mid": o_mid,
            "okx_spr_bps": o_spr,
            "bg_bid": g_bid,
            "bg_ask": g_ask,
            "bg_mid": g_mid,
            "bg_spr_bps": g_spr,
            "cex_mid": cex_mid,
            "cex_floor_bps": cex_floor_bps,
        }
    )
    if h_raw is None:
        out["skip"] = "missing_hl"
        return out

    h_mid = float(h_raw) * float(spec.get("hl_mult") or 1)
    hl_vs_cex = (h_mid - cex_mid) / cex_mid * 1e4
    out.update({"ok": True, "hl_mid": h_mid, "hl_vs_cex_bps": hl_vs_cex})
    return out


def cycle(cost, hl_ok: bool):
    ts = time.time()
    errors = []
    okx = bitget = hl = {}
    try:
        okx = fetch_okx()
    except Exception as e:
        errors.append(f"okx:{e}")
    try:
        bitget = fetch_bitget()
    except Exception as e:
        errors.append(f"bitget:{e}")
    if hl_ok:
        try:
            hl = fetch_hl()
        except Exception as e:
            errors.append(f"hl:{e}")
            hl_ok = False

    books = []
    for coin in cost["universe"]:
        spec = cost["contracts"][coin]
        books.append(row_for(coin, spec, okx, bitget, hl if hl_ok else {}))

    return {
        "ts": ts,
        "iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts)),
        "hl_ok": hl_ok,
        "errors": errors,
        "books": books,
    }, hl_ok


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--hours", type=float, default=0.02)
    p.add_argument("--out", default=str(HERE / "logs" / "bbo.jsonl"))
    p.add_argument("--no-hl", action="store_true", help="CEX triangle only (sandbox / 429)")
    args = p.parse_args()

    cost = load_cost()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    end = time.time() + args.hours * 3600
    hl_gate = Backoff()
    hl_ok = not args.no_hl
    n = 0
    print(f"recording -> {out} hours={args.hours} poll={cost['poll_seconds']}s", flush=True)

    while time.time() < end:
        t0 = time.time()
        rec, hl_ok_now = cycle(cost, hl_ok)
        if any(e.startswith("hl:") for e in rec["errors"]):
            hl_gate.fail()
            hl_ok = False
        else:
            if not args.no_hl:
                hl_gate.ok()
                hl_ok = True
        with out.open("a") as f:
            f.write(json.dumps(rec) + "\n")
        n += 1
        if n % 5 == 1:
            print(rec["iso"], "hl_ok", rec["hl_ok"], "err", rec["errors"][:2], flush=True)
        sleep = cost["poll_seconds"] - (time.time() - t0)
        if not rec["hl_ok"] and not args.no_hl:
            sleep = max(sleep, hl_gate.delay)
        time.sleep(max(0.2, sleep))

    print(f"done rows={n} file={out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
