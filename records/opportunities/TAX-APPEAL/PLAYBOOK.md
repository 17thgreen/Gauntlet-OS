# Property Tax Appeal OS — operational playbook

**Version:** 1 — opening argument for Gauntlet-OS  
**Date:** 2026-09-17  
**Source thesis:** VC `OPP-20260911-002` handbook v0.2 + evidence ledger  
**Status:** Proposal. No collected fee. Authority = NONE.

This playbook takes a position so you can read it against ALMANAC and see what is actually shared. It does not start a fleet.

---

## 1. Opportunity and recommendation

**Who pays:** The property owner (or portfolio manager), after a *verified* first-year tax-dollar reduction.

**What they receive:** End-to-end Georgia assessment appeal. No reduction, no fee. Fee hypothesis: **25% of actual first-year tax dollars saved** `[H]`.

**Recommended first approach:** *Pre-underwrite, then ask.* Do not advertise a generic appeal shop. Rank a county × class × zoning cohort, build an evidence pack on the outliers, contact only those owners with a specific dollar range and a deadline. First geography: **Georgia**. First wedge: **large vacant land and industrial**, not ordinary SFR.

Why not start as Ownwell-with-a-bot: the 25% no-win/no-fee offer already exists `[V]` as a category. The only thing worth building is cheaper, better *selection* plus county adapters plus an outcome graph.

Why not run it as a second ALMANAC product this week: same parcel software, **different customer, different legal clock, different Examiner**. Overlay the rails. Do not overlay the mission.

---

## 2. Evidence and uncertainties

From the VC evidence ledger unless noted.

| Claim | Label |
|-------|-------|
| GA PT-311A; generally 45 days from assessment notice | [V] DOR form |
| Grounds: value, uniformity, taxability, exemption/covenant | [V] |
| Authorized agent may sign PT-311A with a letter of authorization; GA COA rejected “all non-lawyer BOE work is UPL” | [V] statute + *Grand Partners* |
| Two-year value protection after qualifying reduction, with statutory exceptions — weak appeals are not free | [V] O.C.G.A. §48-5-299(c) |
| County filing mechanics differ (Gwinnett/Fulton no email-fax; Forsyth email; Hall qPublic) | [V] |
| DOR 2024 appeal volumes: Fulton 36k parcels (9.86%), DeKalb 18k, Cobb 14k, … | [V] DOR archive |
| PropertyRadar can cut county × zoning × acreage × vacant cohorts; 50-field export | [V] Governor-observed UI |
| PropertyRadar *production* license for automated export/API | [U] |
| Parcel-level historical win/loss/reduction labels | [U] |
| Our P(success), mean savings, minutes/case, CAC | [U] |
| Licensing line: consulting vs appraisal vs court | [U] counsel |
| 25% is the right price for land/industrial | [H] |
| Pre-underwritten outbound beats inbound CAC | [H] |

Do not put DOR county *rates* on a cockpit as if they were our win rate. They are volume, not labels.

---

## 3. Competing models

**A. Pre-underwritten outbound on high-dollar cohorts (recommended).** Cost sits in data + ranking. Outreach only when expected fee − minutes − external cost is still green.

**B. Inbound consumer shop (Ownwell-shaped).** Wait for notices. High volume, low dollars, paid ads. Copies the category. Weak unless residential minutes ≈ 0.

**C. Software-only / lead-to-attorneys.** Sell ranked lists to existing appeal shops. Faster first dollar if someone will buy a list. Gives away the graph. Keep as a *fallback* if representation counsel says no.

**D. Bundle with ALMANAC as “one letter, two offers.”** Same mailbox, insurance lead + tax appeal. **Reject as v0.** Different consent, different claims, different buyer. Dual-purpose mail is how you poison both tests.

A wins provisionally because it uses the same PropertyRadar universe ALMANAC already needs, without sharing the ALMANAC Examiner or the agency customer.

---

## 4. Offer and first customer

**Offer v0:** “We file and work the Georgia appeal. If the taxable value does not drop, $0. If it does, 25% of year-one tax dollars actually saved.” No guaranteed savings number in the first sentence. Band only after the pack exists.

**First customer:** Owner of a **Forsyth-class** (or one chosen pilot county) vacant tract in one zoning code, 25–100 acres — the handbook’s example cohort — *or* one industrial outlier if land comps are empty. Not a homestead SFR.

**Path to first collected dollar:**

1. Freeze one county × class × zoning × size band.
2. Export the cohort from PropertyRadar (Pass 1 underwriting fields only).
3. Rank outliers on assessed $/acre vs peers; Terra Firma constraints on the top 25.
4. Independent human tax/valuation review: does the top of the list look appeal-worthy? If the model and the human disagree, stop mailing.
5. Evidence packs for 5–10. Authorization letter + PT-311A.
6. File inside the 45-day window.
7. Invoice only on verified savings.

First *experiment* is step 4, not step 6. Ranking quality before owner contact.

---

## 5. Economics

Illustration only `[E]`, from the handbook’s arithmetic, not our books:

- 15% off a $5,000 residential bill → $750 saved → **$188 fee** at 25%.
- 15% off a $120,000 industrial bill → $18,000 saved → **$4,500 fee**.

That is why SFR is last unless minutes are near zero.

**Appeal Alpha** (handbook): expected fee = P(success) × expected year-1 savings × 25%, minus CAC, labor, data, appraisal. Early P(success) is a **band**, not a fake probability.

Cash: fee arrives after the county writes the value, not at authorization. Working capital is labor + data + filing, not inventory. Downside screen is mandatory: a sloppy filing can lose the two-year freeze protection `[V]`.

Human minutes: quote, pack, hearing, exception — measure from the first audited 25. Absolute weekly cap belongs in a later Experiment Commission, not here.

---

## 6. Operating workflow

```
PropertyRadar universe
  → county adapter (deadline, filing channel, form quirks)
  → zoning semantics (Terra Firma, not the raw code)
  → peer lattice (class × zoning × size × vacant/improved)
  → four lanes: market / uniformity / fact error / constraint
  → downside screen
  → expected savings band + minutes
  → contact enrichment only on the short list
  → authorization
  → file PT-311A by the county method
  → BOE / hearing officer / settle
  → invoice on verified savings
  → outcome graph (win/partial/loss, $, minutes, argument type)
```

PropertyRadar estimated value means **investigate**, not **the appeal number**.

---

## 7. Fleet, software, and the ALMANAC overlay

### What is actually the same software

| Layer | ALMANAC | Tax appeal | Share? |
|-------|---------|------------|--------|
| PropertyRadar cohort + export | Purchase-month lists, deed/sale as *renewal clock* | County × zoning × vacant/size as *peer universe* | **Yes — ingest + APN join** |
| Parcel graph | Situs, mailing owner, sale date, tax fields | Same identifiers + assessed FMV, land/impr split, millage | **Yes — one parcel table** |
| Terra Firma zoning / slope / flood / access | Optional later for landlord/DP-3 | Core evidence for land | **Yes if TF is already a library** |
| Mail vendor, NCOA, suppressions, piece tracking | Sequence at −90/−45 | One-shot appeal offer inside the 45-day window | **Rails yes, copy no** |
| Consent / TrustedForm / DNC ledger | Required for insurance solicitation | Different script; still need a ledger | **Pattern yes, records separate** |
| Counsel gate | PEWC / DNC / who may mail | UPL / appraisal / advertising / contingency | **Same seat type, different memo** |
| Mechanic | Print/mail ops | Print/mail + county portal upload | **Same hands, different jobs** |
| Clock | Tape/timestamps for list join | Assessment-notice date, filing clock | **Same discipline, different object** |
| Examiner | Agency buy, x-date accuracy, $ per response | Ranking-vs-expert, then savings collected | **Do not share scores** |
| Buyer | Independent agency | Property owner | **No** |
| Calendar | Policy renewal / original deed date | Assessment notice + 45 days | **No** |

### What you can accomplish once for both

1. **One PropertyRadar pipeline** — auth, export, field map, APN/FIPS key, freshness stamp. ALMANAC needs it for instrument P0. Appeal needs the same keys plus assessed-value fields.
2. **One parcel spine** — owner, mailing, situs, sale date, tax year. ALMANAC reads sale date as renewal clock. Appeal reads sale date as a market input. Same column, two readers.
3. **Mail factory** — vendor, suppressions, dead-letter handling. Templates and offers stay product-specific.
4. **County geography file** — FIPS, county name, qPublic/portal URLs. Appeal adds filing adapter rows later.
5. **Counsel packet pattern** — “what may leave the building.” Two opinions, one workflow.

### What you must not merge

- One letter that sells an insurance quote *and* an appeal.
- One “lead score.”
- Appeal deadlines driving ALMANAC mail, or renewal months driving PT-311A.
- Using ALMANAC agency outcomes as evidence that tax appeals work.
- Staffing a tax-appeal Conductor on the ALMANAC VM “to save seats.”

### Fleet if this ever launches

Discovery/Experiment seats copy the *institution*, not the ALMANAC domain pack. New pack: `tax-appeal-ga`. Deterministic: cohort math, millage, deadlines, form fill. Human: first authorization language, first filing, appraisal line, Superior Court.

---

## 8. First experiment

**Question:** On one frozen cohort, does the ranking put parcels a competent human would actually appeal at the top?

**n:** Full PropertyRadar pull for that cohort; human audit of top 25.

**Green:** Meaningful overlap (write the threshold after the first 25 are scored — do not fake it now).

**Kill this cohort:** Top 25 look random to the human; or eligibility/constraints explain the “outliers.”

**Kill this model:** Cannot get lawful representation or PropertyRadar rights; or minutes/case make even industrial fees unworkable.

**Stop:** No owner mail until ranking-vs-human exists. No dual ALMANAC mail.

---

## 9. Build and launch sequence

**Now (under ALMANAC, if it pays for itself there):** parcel spine + PropertyRadar ingest + mail rails. Tag schemas so appeal fields can attach later.

**Before any tax-appeal Experiment DR:**

1. Counsel memo: GA administrative representation + advertising + contingency `[U]`.
2. PropertyRadar production-use rights `[U]`.
3. One county adapter (deadline + filing channel) `[partial V]`.
4. Experiment in §8.

**Not this quarter unless §8 is green:** live owner outreach, hearing automation, 159-county map, residential factory.

Budget requests wait on Treasurer. Handbook research gates 1–8 still stand.

---

## 10. Challenge pointer

No fleet is assigned. If a later Discovery DR exists, it attacks this playbook the same way TORII’s commission attacks TORII: copy ban on Ownwell; first dollar after ranking quality; anti-theater; hard legal gate. Until then this file is for *you* to read against ALMANAC.

Canonical long handbook remains in the VC repo. This playbook is the Gauntlet opening argument plus the overlay map. Do not fork the thesis in chat.
