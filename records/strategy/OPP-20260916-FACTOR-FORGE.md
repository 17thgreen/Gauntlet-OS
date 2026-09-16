# OPP-20260916-FACTOR-FORGE

**Working title:** Factor Forge  
**Status:** `CAPTURED`  
**Stage:** Discover parking lot — not admitted, not funded  
**Origin paper:** Huang & Fan, *Beyond Prompting: An Autonomous Framework for Systematic Factor Investing via Agentic AI*, arXiv:2603.14288v1 (2026-03-14). HTML: https://arxiv.org/html/2603.14288v1  
**Companion site (authors):** https://allenh16.github.io/agentic-factor-investing/

## One sentence

Build a Gauntlet-governed **signal mill**: an agent proposes interpretable cross-sectional factors from a frozen primitive set; Clock admits the tape; Examiner scores OOS IC / long-short net of costs; Cemetery keeps the lucky ones. The paper is the working machine to **attack**, not a Sharpe to copy.

## What the paper actually says `[I]` from the HTML, not a replication

Closed-loop agent (hypothesis → construct factor from ~10 price/volume primitives → daily rank-IC and long-short Sharpe → keep only if t-IC, economic rationale, and OOS pass → LLM reflection updates the search policy). CRSP US equities 2004–2024, IS through 2020, OOS 2021–2024. Headline claim: linear combination of kept signals, **Sharpe 3.11**, **59.53% annualized gross**, max DD −10.84%. Daily turnover **105–113%**. Net-of-3bps still positive in their table. Authors call this a scalable interpretable paradigm.

No tax, insurance, or public-records content. Not a drop-in for ALMANAC.

## Copy ban

Do not implement “Factor Forge v1 = their notebook + Grok.” Do not put 3.11 or 59.53% on any cockpit. Those are the authors’ numbers until we reproduce them.

## Attack the working machine

1. **Economic rationale is cheap.** An LLM can invent a story for any transform of momentum, volume, and volatility. Gate on *pre-registered* rationale templates, not free prose.
2. **Lucky-factor filter is their own section 6.1.** Treat it as incomplete until multiple-testing adjustment, frozen primitive list, and a sealed holdout the search policy never sees are independently enforced.
3. **Sharpe 3.11 + 100%+ daily turnover** is the first Prosecutor exhibit. Capacity and impact are `[U]`. 3 bps is an assumption, not a venue.
4. **Ten primitives** is a small kitchen. “Autonomous discovery” may be recombination of known technicals. Demand ablation vs equal-weight of the raw primitives.
5. **US daily CRSP ≠ crypto 15-minute binaries.** Do not import this scoring into `crypto-alpha`. If the *workflow* is reused there, it is a new experiment with a new object (event contract, not CRSP residual).

## Object redesign (not five features on their stack)

Their object: autonomous researcher that prints factors and a composite Sharpe.  
Our object: **a mill that is allowed to be empty.** Default book is dashes. Promotion is four-field (admission / execution / evidence / authority). First paid question is not “can we launch a fund.”

## Critical uncertainties (test one at a time)

| # | Claim | First measurement |
|---|--------|-------------------|
| 1 | Their OOS composite is reproducible on a Clock-cleared CRSP-or-equivalent tape | Independent rebuild; Examiner-only scoring; report n, turnover, costs |
| 2 | Agent search beats a dumb baseline of the same 10 primitives | Ablation: primitive z-score combo vs agent-kept subset |
| 3 | “Economic rationale” changes which factors survive | Blind the rationale gate on/off |
| 4 | Net edge survives realistic costs and delayed execution | Cost grid + T+1 / skip-open |
| 5 | Workflow transfers to another panel | Separate commission; do not use crypto settlement as a CRSP proxy |

## Who would pay (later)

If #1–#4 KEEP: a systematic desk or an internal research-hours buyer. Not a consumer product. Not an agency lead. `[H]`

## Relation to live packs

- **crypto-alpha:** method cousin only. Different settlement object, different costs, different Examiner metrics.
- **almanac-ga:** no shared scoring. Shared *institution* (no self-grade, cemetery, empty book).
- **Tax Appeal / Surplus / Acquisition:** unrelated markets. Do not merge Factor Forge into those folders.

## Admission bar (before any Experiment Conductor)

- Frozen primitive dictionary and code hash
- Data manifest with no look-ahead
- Sealed OOS the search policy cannot read
- Cost and turnover fields on the Experiment schema
- Independent Examiner who did not write the agent prompts
- Authority starts at `NONE`; next grant is `BUILD_INSTRUMENT` only

## Labels

Paper Sharpe / return: `[I]` (authors).  
Our edge: `[U]`.  
CRSP license and compute budget: `[U]`.  
Legal ability to trade US names: `[U]` — not implied by filing this note.
