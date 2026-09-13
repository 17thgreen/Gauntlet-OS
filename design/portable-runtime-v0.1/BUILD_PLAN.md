# Build plan and implementation handoff

Date: 2026-09-13. Status: implementation specification. No runtime work reported complete.

## Engineering objective

Deliver a small portable executor whose correctness can be demonstrated before introducing broad connectors or live business operations. This is a staged build, not an open-ended platform rewrite.

Specifications and interface contracts remain in Gauntlet-OS. Before production code starts, record its repository placement; the existing domain-pack rules place domain code and operational evidence in their own repositories. No new repository is created by this design package.

## Ordered tickets

| ID | Unit | Dependencies | Concrete completion |
|---|---|---|---|
| B01 | Executable record contracts | None | JSON Schemas/typed models, semantic validator, valid and invalid fixtures matching CONTRACTS |
| B02 | Persistent ledger and artifacts | B01 | Migrations, revisions, transactional event/projection writes, artifact finalization and hash verification |
| B03 | Mission compiler and freeze | B01–B02 | Draft import plus bounded model adapter, scoped error report, immutable freeze manifest |
| B04 | Coordinator and worker adapter | B02–B03 | Ready queue, fenced leases, attempt records, bounded retries, stub workers |
| B05 | Review and policy transitions | B01–B04 | Authenticated reviewer writes, veto handling, separate acceptance/eligibility/authorization |
| B06 | Action broker and test provider | B02,B04,B05 | Envelope validation, atomic reservations, receipts, timeout reconciliation, halt behavior |
| B07 | Status and operator view | B02,B05 | Generated state with evidence links, freshness, costs and next permissible actions |
| B08 | Business-research fixture | B03–B07 | P1 complete with code-calculated economics and independent review |
| B09 | Marketing-production fixture | B08 | P2 accepted artifacts; commercial outcome remains untested |
| B10 | Recurring-operation fixture | B06–B07 | P3 including duplicate occurrence and ambiguous-effect recovery |
| B11 | Independent release evaluation | B08–B10 | Required integrity suite and restore test with recorded results |
| B12 | Model-backed comparison | B11 + resource envelope | Reserved domain tasks compared against simple baseline; no assumed improvement |
| B13 | First real integration | B11 + mission-specific need | Exact-version adapter admitted on its own compatibility/effect tests |

## First executable slice

B01–B05 should support one supplied brief through extraction, deterministic calculation, draft report, independent review and generated status. No external action is necessary.

Use a deterministic stub to test queue behavior, then a real model adapter to evaluate task quality. Clearly distinguish the two sets of results.

## Milestones

M1 — Contracts are executable; invalid assignments fail predictably.  
M2 — One internal workflow resumes correctly after interruption and records independent acceptance.  
M3 — Three domain fixtures reuse core machinery; mock external effects reconcile safely.  
M4 — Model-backed tasks demonstrate measured quality and attention costs.  
M5 — A selected live mission operates within actual authorization and has an outcome measurement plan.

No milestone implies the next. In particular, M3 does not authorize live marketing or trading.

## Builder handoff

Read README, ARCHITECTURE, CONTRACTS and existing constitutional files first. Begin B01 and B02, preserving the semantic separation of delivery, evidence and authorization.

For each ticket:
1. State intended interfaces and affected paths.
2. Implement the smallest complete unit.
3. Execute meaningful tests tied to EVALUATION.
4. Record results and limitations with exact source/fixture versions.
5. Submit reviewable changes; do not label unexecuted tests as passed.
6. Update ticket state from evidence, not narrative.

Do not bulk-install the strategy memo shortlist. Import a dependency only for a concrete accepted ticket and record version, license, maintenance risks and rollback procedure.

## Build economics

Track engineering effort by ticket, operational costs separately, and Human Governor intervention time. No delivery-date or cost guarantee is justified before the first slice runs.

After M2, compare the real integration burden with a simpler executor. If LangGraph adaptation introduces more complexity than it removes, record that finding and evaluate a simpler state machine or another candidate. The portable contracts must survive the change.

## Deferred work

Temporal migration, multiple orchestration frameworks, broad marketing connectors, DSPy optimization, graph databases, public customer accounts, automatic capital deployment and a general-purpose marketplace. Each needs a demonstrated requirement and a scoped admission experiment.

## Approval and authorization boundary

The current request authorizes developing this design package. Existing session authorization covers preserving it in Gauntlet-OS. Production deployment, paid integrations and live actions require their own applicable authorization; this package does not grant it.

The Human Governor need not approve every reversible drafting or testing step already authorized. Resolve routine engineering choices within a ticket while preserving policy. Escalate material governance changes as concrete decision records.

## Venture Challenge tickets

B14 — Challenge planner and candidate register (after B03/B05): compile an open business-selection mission, track independent specialist findings, selected candidate, alternatives and reversals. Validate on synthetic candidates; no predetermined sector or winner.

B15 — Human spending checkpoint (after B06/B14): exact purchase/envelope review UI, budget reservations, approval expiry/revocation and immutable receipts. No paid dispatch from ceiling alone.

B16 — Venture Challenge dry run (after B14/B15): synthetic $500 ceiling, internally prepared offer and delivery artifact, ranked tradeoffs, candidate pivot after contradictory evidence, one mocked approved expense and one denied expense. Report self-sufficiency as UNTESTED. A real challenge begins only with bound owner, resources, action permissions and applicable domain mapping.

B17 — Asset discovery and reuse register (after B03; before full B16): inventory accessible owner repos plus external candidates; retain exact source references, actual capability evidence, licensing unknowns, dependencies, and integration estimates. Demonstrate that a documented-only internal asset is not represented as production-ready, and that a better external/new idea may win. Reading source assets does not mutate original projects.
