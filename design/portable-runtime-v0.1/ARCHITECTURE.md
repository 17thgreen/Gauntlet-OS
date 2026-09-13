# Architecture specification

Date: 2026-09-13. Status: DESIGN DRAFT. “Must” describes acceptance requirements for a future implementation.

## Product behavior

Logan supplies a goal and available context. Gauntlet returns a mission specification showing the intended outcome, dependencies, artifacts, limits and open questions. Once within an existing authorized scope, work advances without repeated permission requests for the same action. The operator sees completed work, blockers, pending decisions and measured costs.

The system must support a mission whose correct outcome is a negative recommendation or an accepted artifact with untested effectiveness.

## Component boundaries

| Component | Responsibility | Excluded responsibility |
|---|---|---|
| Mission compiler | Draft a typed mission from objective, retrieved facts and known authority | Invent missing budgets, grant itself authority |
| Specification validator | Check schemas, dependencies, capability coverage, policy references and separation of duties | Decide whether an empirical hypothesis is true |
| Coordinator | Own task queue, leases, transitions and scheduling | Interpret prose to waive a gate |
| Worker adapter | Execute a bounded assignment using tools or models | Directly mutate accepted state or approve its own result |
| Review and gate service | Validate independent reviews and exact gate inputs | Rewrite evidence to rescue a result |
| Action broker | Enforce action scope, reservations and receipts at the tool boundary | Accept a prompt as authorization |
| Evidence store | Retain source captures, artifacts, provenance and access records | Summarize away conflicting originals |
| Projection service | Generate current state and operator summaries from accepted events | Create new scientific claims |
| Operator interface | Present evidence, decisions and intervention points | Hold the only copy of state |

Conceptual flow: compiler drafts → validator checks → coordinator dispatches → worker submits → independent review accepts or rejects → coordinator advances. An external effect additionally passes through the action broker.

## Deployable shape

Start as a modular application, not a microservice fleet. Modules may share one deployment while preserving distinct interfaces and service identities. Use a persistent relational database for state, transactions and audit events; content-addressed storage for larger artifacts. Git stores specifications, source code, small manifests and reviewed releases.

Provisional implementation choices: Python core; PostgreSQL reference state store; LangGraph as the first orchestration adapter. These are selections to test, not claims of installed dependencies. No hosted vendor service is required by the portable contracts. SQLite may be used for isolated unit fixtures, but acceptance for concurrency and crash recovery must run on the chosen production backend.

LangGraph checkpoints are operational execution state, not the authoritative scientific ledger. The ledger and accepted artifacts must remain readable without a model conversation or LangGraph-specific object.

No framework upgrade silently changes an active mission: each mission pins protocol, domain packs, workflow, worker configuration, tool versions, evaluator and runtime build.

## Source of truth and transactions

Store entity revision and audit event in one database transaction. Generate read models from committed events. Artifacts upload to a temporary location, are hashed and finalized, then referenced by an event; failed finalization cannot create accepted evidence.

Immutability is an enforced storage permission and retention policy, not merely a filename convention. Workers may submit new objects, never overwrite accepted originals. Corrections create superseding records retaining prior values.

An artifact hash detects changed bytes; it does not prove correctness or authorized authorship. Use authenticated writers and access logging. Protect sealed data outside worker-accessible shared storage.

## Trust boundaries

A Bot name is an accountability label, not isolation. Execution identities must be derived from authenticated workers, not request-provided role strings. Gate writers and action authorizers require separate privileges from proposer workers.

Until the deployment demonstrates those boundaries, advertise administrative role separation only; do not claim enforced scientific independence. A single shared computer with broad credentials is insufficient for protecting sealed evaluations.

The coordinator supplies workers only the tools and evidence references needed for the task. Untrusted documents and skill content cannot widen tool access. External connectors receive narrow credentials through the broker; the worker does not receive broker credentials.

## Capability interface

Every capability declares input/output contracts, version, license, resource requirements, network destinations, permitted effect classes, and evaluation records. Admission binds an exact version and scopes where it is approved. A changed capability starts as a new candidate.

Use direct code for calculation, validation, scheduling and stable API operations. Use models for uncertain decomposition, synthesis and creative work. Retrieve small evidence packets with original references; retain full originals outside model context.

Optional integrations from the strategy memo remain deferred until a mission needs them. Initial fixtures should run with a document fixture loader, a deterministic calculator, a file-producing worker and a mock external service.

## What remains domain-specific

Metrics, causal interpretation, subject-matter evidence, permitted use of data, specialist mandates, publication criteria and operational limits belong to domain packs. The core understands gate results and authority, not Kalshi prices or advertising conversion formulas.

Quality acceptance can include documented human judgment. Quantitative claims must still have executed or traceable observations. Machine validation of a number does not establish causality.

## Resource model

Each mission specifies an overall resource envelope and smaller task limits. The scheduler reserves budget atomically before dispatch. Unknown provider usage is recorded as unknown and holds further dependent spending until reconciled; it is never zero by default.

User attention is measured as intervention time and decision count. The runtime should report overhead separately from productive work, so a multi-agent workflow can be compared with a simpler baseline.
