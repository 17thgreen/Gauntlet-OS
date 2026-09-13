# Domain bindings and pilot fixtures

Date: 2026-09-13. Status: DESIGN DRAFT. All pilots below are specifications using synthetic or supplied fixtures, not active businesses or demonstrated outcomes.

## Shared fixture rules

Use the same coordinator, contracts, action broker, review interface and event store. Change only mission, workflow, domain schemas and tools. Use named test identities for Conductor, data governor, independent reviewer/Examiner, Prosecutor and required governors. These fixtures are not evidence of production isolation.

Fixture budgets use zero external spend. Model-free stub workers permit deterministic infrastructure tests; a separate bounded model-backed evaluation requires a recorded resource envelope. Stub success does not establish model quality.

## P1 — Business research

Objective: assess whether a specified service offer deserves a bounded customer-discovery test.

Inputs: supplied company brief, synthetic competitor pages, synthetic supplier costs, target-customer excerpts, and one intentionally contradictory source. All fixture observations carry SYNTHETIC tags.

Workflow:
1. Ingest and retain originals.
2. Extract attributable claims; preserve the contradiction.
3. Calculate unit economics from labeled inputs using code.
4. Identify demand, delivery and distribution uncertainties.
5. Produce a brief and an explicit first-customer test specification.
6. Independent reviewer checks citations, arithmetic and unsupported claims.
7. Accept the brief or reject with specific findings.

Outputs: evidence register, economics table with assumptions, recommendation, unresolved questions, test specification.

Artifact acceptance requires every material factual assertion to link to fixture evidence or be labeled assumption/inference; formula recalculation must match; contradictory evidence must be visible. No real market viability is asserted from synthetic data.

Business outcome status: UNTESTED. Outreach authorization: absent. Drafting customer interview questions is allowed; sending messages is not part of the fixture.

## P2 — Marketing production

Objective: produce a reviewable landing page and two distinct offer hypotheses for the same supplied service.

Inputs: P1 accepted brief, brand context, allowed claims, synthetic audience research and content requirements. Inherited sources retain P1's synthetic status.

Workflow:
1. Bind product, audience and offer context.
2. Produce two distinct positioning rationales.
3. Create local landing-page artifacts.
4. Check claims, navigation, form behavior in a fixture, accessibility requirements defined for the task, and event payloads.
5. Independently review creative fit against the supplied rubric.
6. Package a proposed live experiment, with unresolved sample/budget fields explicitly blocking launch.
7. Accept deliverables only after required reviews.

Outputs: page source, rendered preview where supported, claims ledger, event dictionary, proposed experiment record, reviewer findings.

Artifact acceptance is separate from effectiveness. A rubric may select the clearer draft, but cannot certify higher conversion. Tracking tests prove event wiring, not customer demand.

Commercial promotion needs a prospectively approved domain mapping and actual observations. The existing institutional ladder remains controlling; this document does not eliminate replication or forward requirements for commercial claims.

## P3 — Recurring operations

Objective: produce a recurring opportunity digest from a supplied feed, retaining changes and exceptions.

Inputs: synthetic feed snapshots with duplicates, one malformed record, and a later changed record. Schedule uses fixed UTC test occurrences.

Workflow:
1. Receive occurrence with unique key.
2. Collect snapshot and register provenance.
3. Normalize and deduplicate by declared identity rules.
4. Record changed fields without overwriting prior evidence.
5. Generate digest artifact and exception report.
6. Independently review the first occurrence against expected fixture outputs.
7. On an explicitly authorized mock-send step, dispatch to a fake endpoint through the broker.
8. Reconcile receipt and close occurrence.

Inject a crash after the mock endpoint accepts but before the worker records success. Retry must reconcile to one effect. Also test a provider without idempotency support: outcome becomes UNKNOWN and automatic resend is blocked.

Acceptance: expected digest, complete lineage, visible malformed record, duplicate suppression, correct schedule key and one confirmed mock effect. This fixture authorizes no real communication.

## Business-building composition

A larger mission may compose:
- Business research: choose the next uncertainty worth resolving.
- Product build: create the smallest delivery capability.
- Marketing production: prepare offer and distribution artifacts.
- Experiment: observe real customer behavior under approved limits.
- Operations: deliver and record economics, quality and retention.

Progress may loop back to research. Revisions retain prior assumptions and failure records. No single score combines demand, profitability, feasibility and authorization.

## Example MissionSpec skeleton

This is intentionally non-executable until placeholders are bound.

- mission_id: MISSION-PILOT-MARKETING-001
- completion_scope: artifact
- institutional_ref: Gauntlet-OS exact adopted commit plus adoption record
- domain_bindings: business-research fixture v0.1 + marketing-production fixture v0.1
- workflow_ref: BUILD v0.1
- objective: local campaign package with traceable claims and fixture-tested event wiring
- deliverables: two positioning variants, one page artifact, event dictionary, review record
- allowed_effects: internal fixture writes only
- external_spend_cap_minor: 0
- commercial_claim_status: UNTESTED
- launch_authorization: none
- unresolved: live traffic, live sample design and operating budget; these block launch only
- stop: missing source for a material claim; resource envelope exhausted; governor halt

## Portability check

P1, P2 and P3 must not introduce domain-specific conditionals into the core coordinator. Domain extensions may add schemas, evaluators and capabilities through declared interfaces. Record changes to shared core code separately from pack changes.

A successful three-fixture demonstration establishes only tested portability and recovery behavior. It does not prove arbitrary-domain competence or profitable business operation.
