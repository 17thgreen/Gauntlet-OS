# Lag Desk — sharpened thesis

**Date:** 2026-09-18  
**Status:** proof design. No fleet. No live wallet.  
**Tape:** crypto perpetual venues (not prediction markets)  
**Constraint:** two clocks, then a histogram, then a paper book.

## One sentence

Liquid perps already tax the 100–700 ms discovery lag; mid-name **basis that lasts seconds** is the only gap we can measure from a normal box and the only one a Grok stack might harvest — and only after a 10-day paper proof on named coins.

## What is true (labeled)

| Claim | Label |
|-------|--------|
| Arrakis, event-time fills, 16 days to 2026-02-26: Binance leads HL ~700 ms on 29/29 liquid perps; Lighter ~100 ms behind Binance | [V] published study |
| Hasbrouck-style work assigns most BTC discovery to Binance; a 7% venue disconnect was not transferable before it closed | [V] public notes |
| HL base perp fees ≈ 1.5 bp maker / 4.5 bp taker | [V] fee schedules, mid-2026 |
| REST snapshot 2026-09-18: HL mid vs OKX mid about +6–7 bp BTC/ETH, +11–16 bp NEAR/ONDO/WLD, −13 bp APT | [V] our poll, receipt-time |
| PEPE “10,000× gap” was kPEPE vs PEPE units | [V] our bug |
| Binance REST from the research host = HTTP 451; HL 429 after a few calls | [V] |
| OKX vs Bitget over ~90s: BTC ~2 bp, WIF ~10 bp and persistent | [V] six- and five-sample polls |
| 700 ms × 1 bp/s move ≈ 0.7 bp — less than one HL taker fee | [I] |
| Mid-name HL–CEX gaps are mostly basis, not 700 ms of lead–lag | [I] |
| Those gaps survive fees often enough to paper-trade | [H] — this is the test |
| NY bare metal flips Bet A on BTC to green | [H] almost certainly false; gated spend |

## Two objects, do not mix P&L

```
CLOCK FAST     CLOCK SLOW              OBJECT
CEX match      HL consensus fill       Bet A  micro lead–lag   (~0.1–0.7 s)
CEX mid        HL mid / mark           Bet B  basis            (seconds–minutes)
CEX flush      HL book / liq tape      Bet C  cascade          (event)
```

Bet A is an HFT race. Grok is the wrong pipe. NY metal is allowed only after an event-time histogram on named thin coins shows lag × volatility > 2× all-in cost.

Bet B is the desk we can stand up from a normal machine. That is what `kit/` measures.

## Cost band

Round-trip friction floor ≈ 8–12 bp before slippage (HL taker 4.5 bp + CEX taker + half-spreads). Bet A on BTC is negative EV. Bet B is only *eligible* when HL vs median CEX exceeds that floor *and* the CEX–CEX gap for that coin.

## 10-day proof (paper only)

Universe: BTC, ETH (controls) + NEAR, ONDO, WLD, APT, WIF. Venues: OKX + Bitget + HL.

Forbidden during the proof: live orders, LLM on the hot path, editing `cost.json` after seeing results, mixing Bet A into Bet B.

Green coin: residue > 0 after fees on a pre-registered hit count. Kill coin: residue ≤ 0 or depth < min size on 80% of hits. Kill tape: every candidate dead; hunt the next pair of clocks.

## Relation to the shop

ALMANAC remains the path to a collected dollar. This folder is the parallel hunt.
