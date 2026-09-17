# TORII operational playbook

**Version:** 1 — opening argument  
**Date:** 2026-09-17  
**Status:** Proposal. Numbers without a collected invoice are not [V].  
**Copy ban:** Do not clone Master Set Collectibles’ SKU list, suppliers, or storefront.

---

## 1. Opportunity and recommendation

**Who pays:** U.S. specialty retailers and serious resellers (TCG/anime/hobby shops, Whatnot/eBay sellers already moving Japanese product) who want one invoice and one inbound for goods they already sell or have asked for.

**What they receive:** A quoted landed wholesale price on a named SKU with authenticity evidence, carton/JAN where it exists, and a delivery window. Not a consumer Pokémon storefront.

**Recommended first approach:** *Demand-first wholesale gateway.* Identify a buyer who is already selling a Japanese SKU, quote a landed price against a verified supplier, take a deposit or PO, then buy. Inventory is the exception, not the default.

Why this first: the friend’s desk proved *import + multi-channel* can clear dollars. It did not prove that *we* should own $500k of the same boxes. Risk-adjusted ROIC beats gross margin. A 15% turn in three weeks beats a 35% box that sits six months.

---

## 2. Evidence and uncertainties

| Claim | Label | Note |
|-------|-------|------|
| Friend reported ~$500k in one month, ~13% net wholesale, ~2× that retail, $4–5M year run-rate, channels Shopify/eBay/Walmart/Temu/private | [H]/[I] | His books are not in this repo. Treat as existence proof of a category, not our forecast |
| Wholesale site Master Set Collectibles launched ~April | [I] | Public site named in the synthesis |
| Mega Dream ex quote ~$118/box vs U.S. realized ~$70–90 → reject | [I] | Screening example; re-verify before reuse |
| Storm Emeralda quote ~$178–191 vs U.S. realized at/below → reject | [I] | Same |
| OP-17 JP ~¥220/pack, 24/box ≈ ¥5,280 before freight; U.S. secondary was higher pre-release | [I] | Timing premium; pilot only |
| Chiikawa JP B2B catalogs show licensed goods + JAN | [I] | Demand and U.S. landed still [U] |
| Figures: JP–US spread can exist; freight $/ft³ dominates | [I] | |
| Labubu/blind box demand is real; counterfeit risk is material | [I] | Eligibility gate, not a score weight |
| *Our* collected revenue, supplier fills, buyer POs | [U] | Empty |

Hard gate: no buy if authenticity/licensing/provenance is UNKNOWN. A fat margin does not buy down fake goods. The old 5% IP weight in the synthesis score is retired.

---

## 3. Competing models (provisionally ranked)

**A. Demand-first wholesale gateway (recommended).** Quote against demonstrated demand; preorder/PO before the ocean container. Capital follows a name.

**B. Inventory-led multi-channel reseller (the friend).** Buy boxes, spray Shopify/eBay/Walmart. Faster if you already have allocation and a warehouse habit. Worse ROIC for a new operator. Copies the working machine.

**C. Sourcing-as-a-service / marketplace.** Never own stock; charge a finder's fee or take-rate. Cleaner balance sheet. First-dollar is slower unless a buyer will pay for a quote alone. Keep as the *scale* end-state if proprietary request data compounds.

**D. Consumer D2C anime store.** Pretty. Competes with everyone. Avoid as the first object.

A wins provisionally because it is the shortest path to a collected dollar *and* it manufactures the proprietary graph (buyer ↔ SKU ↔ supplier ↔ landed cost) that C needs later. B is allowed only as a capped test lot after a PO exists.

---

## 4. Offer and first customer

**Offer v0:** “Landed case price on SKU X, authentic, ETA Y, deposit Z% to lock.” One page, one SKU, one buyer.

**First customer profile:** A U.S. shop or reseller already listing that SKU or an adjacent JP set. Not a cold consumer.

**Path to first dollar:**

1. Pick one SKU that survived eligibility (JAN/official distributor or equivalent).
2. Confirm U.S. *realized* prices (sold comps), not asks.
3. Get a supplier quote with identity evidence.
4. Compute landed (product + freight + duty + fees + shrink + payment cost).
5. Pitch 5 already-selling buyers. Take a deposit or signed PO.
6. Buy only what is covered + a written residual cap.
7. Collect the balance on ship or on receive — whichever the first contract says.

If nobody pays a deposit, the SKU is not demand. Do not “just buy a little.”

---

## 5. Economics

Working buy rules from the synthesis, restated as hypotheses `[H]` until we have invoices:

- ≥20% expected net wholesale contribution after all-in landed + marketplace/wholesale discounts, **or**
- ≥30% expected net retail if we are forced to retail the residual, **or**
- ≥15% with documented turns measured in weeks and a written exit.

Always compute: contribution $, days to cash, capital $ at risk, $/ft³ for bulky goods, MOQ vs pre-sold qty.

**Do not** publish a $1M / $5M / $25M model as a plan. Those are optional later exercises.

Human labor to measure from day one: minutes to produce one quote; minutes to land one PO; hours/week on exceptions (customs, shortage, authenticity dispute).

Working capital rule: residual speculative units ≤ a Governor-set dollar cap (start: small enough that a total loss is a lesson, not a hole).

---

## 6. Operating workflow

```
Buyer signal or Request-a-Product
  → eligibility (authentic / licensed / exportable)
  → realized-demand check
  → supplier quote + landed model
  → buyer quote / preorder
  → Treasurer+Governor if new spend
  → PO to supplier
  → freight / broker / receive
  → allocate to the PO, residual to a named channel or don’t buy it
  → collect, support, reorder clock
  → write back: won/lost reason, lead time, defect, margin realized
```

Lost quotes are first-class data. “Too expensive / already has a source / fake-risk / timing” beats a silent no.

Channels: core = direct B2B (email/Shopify wholesale). Opportunistic = eBay/Faire if the unit economics survive fees. Avoid standing up five storefronts before one PO.

---

## 7. Fleet and software

**Deterministic (not agents):** landed-cost calculator, eligibility stamps, inventory counts, label/tracking once a 3PL exists, invoice totals.

**Scout-class (research):** find comps, catalogs, release calendars, public BOL patterns. Output is a Field Report, never a buy.

**Human forever at v0:** supplier identity, first authenticity call, first wire, first large PO, anything that looks like gray-market.

**Do not staff 16 named agents.** TORII v0 is Governor + one Discovery/Build Bot + a spreadsheet or small DB. Shopify is a storefront, not the brain.

Unbuilt: CRM predictions, dynamic pricing, 1,000-buyer graph, CFO morning brief. Those are later commissions.

---

## 8. First experiment

**Question:** Will one already-selling U.S. buyer place a deposit against a landed quote on one eligible SKU?

**n:** 5 outbound quotes on the same SKU (or two SKUs if the first is dead).

**Green:** ≥1 collected deposit or binding PO.

**Kill this SKU:** 0 after 5 serious conversations + a landed number they saw.

**Kill this model:** if the only way to get a “yes” is to eat authenticity risk or to buy inventory first “and hope.”

**Stop:** no ocean freight until the deposit rule is written into the PO.

Baseline: friend’s 13% wholesale is *not* our baseline. Our baseline is $0 collected.

---

## 9. Build and launch sequence

1. Eligibility checklist + landed-cost sheet (Working).
2. One supplier file with documents (Working for one name, else Unbuilt).
3. One buyer list of 25 already-selling accounts (research; not a CRM).
4. Quote template.
5. First experiment (§8).
6. Only then: Shopify wholesale skin, 3PL talk, Request-a-Product form.

Budget *requests* (not approvals): sample buy, small freight test, data subscriptions if a quote cannot be made without them. Treasurer stamps each.

---

## 10. Challenge

The fleet’s assignment is [VENTURE_CHALLENGE.md](VENTURE_CHALLENGE.md). It may replace this object. It may not invent a store that already has customers.
