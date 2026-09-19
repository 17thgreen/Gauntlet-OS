# Lag Desk

**Status:** `HUNT / NOT A GO`  
**Authority:** none  
**Fleet:** none  
**Date parked:** 2026-09-18

Two clocks, not a trading bot. Fast clock = CEX perp mid (OKX / Bitget). Slow clock = Hyperliquid mid. The only inequality we are willing to test from a normal machine is **basis that lasts seconds**, after spreads, after the CEX–CEX floor, after taker fees.

This is not the crypto-binary pack and not ALMANAC. If the 48-hour file is dead, cemetery *this tape*. Keep the job (find two clocks).

## What is already done

- Thesis and labels: [THESIS.md](THESIS.md)
- Frozen cost band: [kit/cost.json](kit/cost.json) — do not edit after seeing P&L
- Recorder + examiner (stdlib Python): [kit/recorder.py](kit/recorder.py), [kit/examine.py](kit/examine.py)
- Smoke test (CEX only, this host cannot hold an HL connection): WIF CEX–CEX floor ~10 bp and persistent; BTC floor ~2 bp. That floor is noise Bet B must beat.
- Bet A (700 ms HL lag vs Binance) is treated as **dead on liquid names**: ~0.7 bp of lag vs ~4.5 bp HL taker. NY metal is gated until an event-time histogram on *named thin coins* says otherwise.

## What needs to be done

1. **Run the recorder on a box that can reach `api.hyperliquid.xyz`.**
   ```bash
   cd records/opportunities/LAG-DESK/kit
   python3 recorder.py --hours 48 --out logs/bbo.jsonl
   python3 examine.py logs/bbo.jsonl
   ```
   Do not put Grok (or any LLM) between the poll and the JSONL row. Clock writes. Examiner reads the file after.

2. **Read the examine table against frozen rules.**
   - `WATCH` on a candidate = keep recording toward 10 sessions / 20 hits.
   - All `HOLD` / `FLAT` / `NO_HL` = kill Bet B (this tape). Do not change `cost.json` to rescue it.
   - `Go` still requires `go_min_hits` across `go_min_sessions` in `cost.json`.

3. **If WATCH survives 48h:** add L2 touch (mid overstates edge), size clamp at 20% of HL touch / `$500` min, paper stub only. Still no live wallet.

4. **If the tape dies:** pick the next pair of clocks (need not be crypto or prediction markets). Reuse the kit; change `cost.json` and the two URLs only. Cemetery this folder’s verdict in one line.

5. **Do not:** rent NY bare metal first; mix Bet A fills into Bet B; run a Grok hunter loop on each poll; promote on a REST snapshot.

## Residue (the test)

```
residue_bps = (HL mid − median CEX mid)
            − 0.5*(OKX spread + Bitget spread)
            − |OKX − Bitget|
            − HL taker − avg CEX taker
            − 2 bp slip
```

A hit is residue on the same side of 0 for ≥ 30 seconds.

## Relation to the shop

ALMANAC remains the collected-dollar experiment. Lag Desk is a parallel Discovery hunt. No fourth READY card. No self-grade.
