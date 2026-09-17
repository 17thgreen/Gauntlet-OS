# Playbook and Venture Challenge

**Status:** RATIFIED workflow for prepared ideas  
**Does not:** start a fleet or grant spend

A ticket that KEeps out of [DISCOVERY_FUNNEL](DISCOVERY_FUNNEL.md) becomes a **prepared opportunity** only when both companions exist:

| Document | Job |
|----------|-----|
| Operational Playbook (8–10 pages) | Strongest defendable version of the business |
| Venture Challenge Commission | Assignment to attack that playbook and produce a buildable, theater-free result |

The playbook is the opening argument. The fleet must earn changes with better reasoning and evidence. It may conclude that another customer, offer, channel, or object is better. It may conclude the idea should stay parked.

Every idea can deserve this pair **without** deserving an active fleet. Attention and capital are separate Decision Records.

## Ten playbook sections (required)

1. Opportunity and recommendation — who pays, what they get, why this approach first
2. Evidence and uncertainties — [V]/[I]/[A]/[H]/[E]/[U]
3. Competing models — at least three; why the recommended one wins *provisionally*
4. Offer and first customer — price hypothesis, channel, shortest path to a collected dollar
5. Economics — costs, contribution, working capital, downside, human minutes
6. Operating workflow — find customer → deliver → collect → support → reorder
7. Fleet and software — seats, deterministic code vs agents, human gates
8. First experiment — cheapest meaningful test, baseline, green/kill, stop rules
9. Build and launch sequence — deliverables, dependencies, budget *requests*, milestones
10. Pointer to the Challenge Commission

## Standing objectives (every commission)

Expose tradeoffs. Do not bury them in a weighted score.

- Fastest *credible* path to first collected dollar
- Strong net earnings after all costs, including human time
- Simple operations with reliable delivery
- Maximum *sustainable* automation, measured in minutes not slogans
- Repeat revenue and room to scale

## Anti-theater (every future challenge)

| Requirement | Fleet must show |
|-------------|-----------------|
| Numbers have a status | Observed, calculated, assumed, or unknown — with provenance |
| Capabilities have an implementation status | Working, simulated, externally blocked, or unbuilt |
| One complete workflow first | Real input → persist → approval if required → verifiable output |
| Empty states are honest | No invented customers, quotes, orders, or revenue. DEMO stays DEMO |
| Failures are handled | Missing data, dupes, dead integrations, interrupted jobs recover |
| Human work is measured | Minutes per customer / transaction / exception. Absolute hours cap |

Hard eligibility (authenticity, license, consent, data rights) is a **gate**, not a 5% weight in a score. Economics compare only survivors.

$25M–$500M stories are optional strategy exercises. They do not consume the first-dollar work.

## Repository layout

```
records/opportunities/<SLUG>/
  README.md                 # status, links, authority = NONE until a DR
  PLAYBOOK.md               # opening argument (preserve; do not overwrite)
  VENTURE_CHALLENGE.md      # the commission
  revisions/                # dated challenge findings and approved edits
  experiments/              # TEST / EC results
  operating/                # current instructions after authority is granted
```

Inbox tickets do not get this pair until KEEP.
