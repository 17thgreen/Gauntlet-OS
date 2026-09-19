#!/usr/bin/env python3
"""Read recorder JSONL. Print residue and go/kill. Do not change cost.json after seeing this."""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_cost():
    return json.loads((HERE / "cost.json").read_text())


def residue_bps(book: dict, cost: dict):
    if not book.get("ok"):
        return None
    fees = cost["fees_bps"]
    hl_vs = book["hl_vs_cex_bps"]
    half = 0.5 * ((book.get("okx_spr_bps") or 0) + (book.get("bg_spr_bps") or 0))
    floor = book.get("cex_floor_bps") or 0
    return (
        abs(hl_vs)
        - half
        - floor
        - fees["hl_taker"]
        - 0.5 * (fees["okx_taker"] + fees["bitget_taker"])
        - cost["slip_bps"]
    ) * (1 if hl_vs >= 0 else -1)


def persist_hits(series, persist_s, poll_s, thresh):
    need = max(1, int(round(persist_s / poll_s)))
    hits = 0
    run = 0
    last_sign = 0
    for x in series:
        if x is None:
            run = 0
            last_sign = 0
            continue
        sign = 1 if x > thresh else (-1 if x < -thresh else 0)
        if sign != 0 and sign == last_sign:
            run += 1
            if run == need:
                hits += 1
        else:
            run = 1 if sign else 0
            last_sign = sign
    return hits


def main():
    p = argparse.ArgumentParser()
    p.add_argument("log", nargs="?", default=str(HERE / "logs" / "bbo.jsonl"))
    args = p.parse_args()
    cost = load_cost()
    path = Path(args.log)
    if not path.exists():
        print("no log", path)
        return 1

    by_coin = defaultdict(list)
    n_rows = n_hl = 0
    with path.open() as f:
        for line in f:
            rec = json.loads(line)
            n_rows += 1
            if rec.get("hl_ok"):
                n_hl += 1
            for book in rec.get("books", []):
                by_coin[book["coin"]].append(
                    {
                        "ok": book.get("ok"),
                        "skip": book.get("skip"),
                        "hl_vs": book.get("hl_vs_cex_bps"),
                        "floor": book.get("cex_floor_bps"),
                        "res": residue_bps(book, cost) if book.get("ok") else None,
                    }
                )

    print(f"rows={n_rows} hl_rows={n_hl} poll={cost['poll_seconds']}s")
    print(
        f"{'coin':8} {'n_ok':>5} {'mean_hl':>8} {'mean_fl':>8} {'mean_res':>8} "
        f"{'hits30s':>8} {'verdict':>8}"
    )
    for coin in cost["universe"]:
        rows = [r for r in by_coin[coin] if r["ok"]]
        if not rows:
            floors = [r.get("floor") for r in by_coin[coin] if r.get("floor") is not None]
            skips = {r.get("skip") for r in by_coin[coin]}
            if floors:
                mean_f = sum(floors) / len(floors)
                print(
                    f"{coin:8} {'0':>5}      n/a {mean_f:8.2f}      n/a        0    NO_HL  {skips}"
                )
            else:
                print(f"{coin:8} {'0':>5}  no rows {skips}")
            continue
        hl = [r["hl_vs"] for r in rows if r["hl_vs"] is not None]
        fl = [r["floor"] for r in rows if r["floor"] is not None]
        res = [r["res"] for r in rows if r["res"] is not None]
        mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")
        hits = persist_hits(
            res, cost["persist_seconds"], cost["poll_seconds"], cost["hit_residue_bps"]
        )
        if not hl:
            verdict = "NO_HL"
        elif mean(res) > 0 and hits >= 1:
            verdict = "WATCH"
        elif mean(abs(x) for x in res) < 1 and mean(fl) < 3:
            verdict = "FLAT"
        else:
            verdict = "HOLD"
        print(
            f"{coin:8} {len(rows):5d} {mean(hl):8.2f} {mean(fl):8.2f} {mean(res):8.2f} "
            f"{hits:8d} {verdict:>8}"
        )

    print()
    print("WATCH = residue mean > 0 and at least one 30s run. Not a go.")
    print("Go still requires cost.json go_min_hits across go_min_sessions.")
    print("HOLD = gap exists but after fees/floor/spread it does not pay.")
    print("FLAT = CEX-CEX and residue too small to be a desk.")
    if n_hl == 0:
        print("NO HL IN LOG — CEX triangle only. Do not promote.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
