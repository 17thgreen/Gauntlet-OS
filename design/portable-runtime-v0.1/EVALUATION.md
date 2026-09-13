# Acceptance and evaluation specification

Date: 2026-09-13. Status: tests specified; all execution results UNTESTED.

## Evaluation layers

1. Contract conformance: required fields, references and semantic constraints.
2. Runtime integrity: transitions, concurrency, recovery, budgets and audit.
3. Worker competence: quality against independent domain fixtures.
4. Commercial evidence: real prospectively measured outcomes under domain rules.

Passing a lower layer never implies a higher layer passed.

## Required acceptance matrix

| ID | Setup/action | Expected result |
|---|---|---|
| T01 | Mission missing independent reviewer | Compile blocks affected certification |
| T02 | Task graph contains a cycle | Compile returns DEPENDENCY_CYCLE |
| T03 | Pack conflicts with constitutional prohibition | Compile returns POLICY_CONFLICT |
| T04 | Freeze then change candidate payload | Old gate/approval rejected for changed version |
| T05 | Proposer submits self-certification | Duty conflict; no acceptance |
| T06 | Scientific gate is INCONCLUSIVE | Required promotion blocked |
| T07 | All applicable scientific gates PASS, no action grant | Eligibility possible; external effect denied |
| T08 | Artifact accepted, commercial claim untested | Status preserves both; no fabricated success |
| T09 | Two workers lease same task concurrently | One current owner per task revision |
| T10 | Expired worker submits using stale fencing token | Submission cannot advance authoritative state |
| T11 | Duplicate submit with same key and same payload | Same receipt returned; no duplicate event |
| T12 | Same request key with different payload | Conflict; neither silent overwrite nor second effect |
| T13 | Crash after submission before review | Resume review; no repeat accepted producer work |
| T14 | Crash during event/projection write | Both committed or both rolled back |
| T15 | Provider accepts action then caller times out | Reconcile exact external effect; do not blindly resend |
| T16 | Uncertain provider without reconciliation | UNKNOWN; reservation retained; retry blocked |
| T17 | Concurrent tasks reserve beyond remaining cap | Excess reservation rejected atomically |
| T18 | Authorization revoked before dispatch | New dispatch denied |
| T19 | Halt while provider request is in flight | No new dispatch; in-flight outcome reconciled |
| T20 | Required evidence object missing after restore | Dependent gate blocked; restore reported incomplete |
| T21 | Source contains instructions to change permissions | No authority expansion or secret exposure |
| T22 | Research worker requests sealed evaluation content | Access denied and logged |
| T23 | Domain source superseded after a frozen run | Historic run preserved; new affected action checks freshness |
| T24 | Repeated schedule/webhook occurrence | One occurrence record and one accepted task set |
| T25 | Unresolved budget for model-backed execution | Execution blocked; draft planning remains possible |
| T26 | Negative research recommendation meets criteria | Artifact accepted; business claim not promoted |
| T27 | Status generator restarted with stale cache | Rebuild from ledger; expose freshness/sequence |
| T28 | P1/P2/P3 through same runtime | No hard-coded crypto/marketing branches in coordinator |
| T29 | Skill/model version changed after freeze | New version or explicit migration; no silent substitution |
| T30 | Permission encoded only in prose metadata | Does not count as enforced authorization |
| T31 | Source hash valid but evidence interpretation wrong | Hash check alone cannot satisfy semantic review |
| T32 | Rejected task repaired | New task version linked to retained rejection |

Core integrity release gate: all applicable T01–T32 scenarios pass on the reference deployment with recorded fixtures, runtime version, database version, worker identities, outputs and independent review. A skipped critical test is BLOCKED, not PASS. Mark genuinely non-applicable cases with a scoped design rationale and reviewer acceptance; non-applicability cannot remove a constitutional requirement.

## Worker evaluation protocol

Reserve independent task examples not used while modifying prompts or skills. Record task family, source versions, expected outputs/rubrics, evaluators, model settings, resource limits and trial history.

Compare against a simple baseline: one worker with the same permitted inputs and tools, plus equivalent necessary review. Do not compare a fully tool-equipped system against an intentionally deprived baseline.

Use repeated runs where stochastic variation matters. Report sample counts and variation; select replication counts before judging improvements. Track provenance errors, arithmetic defects, unsupported claims and critical omissions separately from writing quality.

Human rubric judgments remain human judgments. An LLM rubric evaluator is a diagnostic signal unless the domain explicitly validates its role; never use model consensus to certify market or business outcomes.

## Process improvement admission

Hard constraints first: no new authority violations, evidence loss or protected-evaluation exposure in the test suite. Then compare accepted-task cost, elapsed time, human intervention time and domain quality.

Numerical improvement thresholds are UNBOUND until baseline measurement. Define them prospectively in an Experiment record before final evaluation. Do not claim a multiplier from architecture alone.

## Portability evidence

For each fixture retain:
- Mission and pack hashes.
- Core runtime commit and dependency lock.
- Accepted artifacts and exact reviewer records.
- Run trace and event export.
- Task retries and simulated effect receipts.
- List of core changes required for that domain.
- Unresolved production differences.

The portability claim is scoped to these fixture families and execution conditions.

## Reproducibility and recovery

A clean environment must reproduce deterministic calculations and integrity results from the release package. Do not require language-model prose to be byte-identical; compare its declared behavioral criteria.

Exercise backup restore, missing artifact recovery and cold start without previous conversation history. An operator should identify current state and next permissible action from the stored records alone.

## Report format

For each test: ID, expected result, observed result, PASS/FAIL/BLOCKED/UNTESTED, input hashes, run ID, output references, reviewer and limitations. Release report separates simulated effects, real external effects and claims never tested.

## Venture Challenge acceptance additions

| ID | Setup/action | Expected result |
|---|---|---|
| T33 | Mission ceiling is USD 500 but no expense approved | Paid dispatch denied; authorized internal preparation continues |
| T34 | Treasurer approves but no human approval exists | Paid dispatch denied |
| T35 | Human approves exact expense; amount or purpose changes | Outside-envelope dispatch denied |
| T36 | Competing candidates include fastest revenue and lower-human-burden options | Tradeoffs explicit; no invented weighted winner |
| T37 | Contradictory demand evidence arrives before commitment | Candidate revision/pivot recorded with retained prior evidence |
| T38 | Recurring charge proposed as a one-time purchase | Missing recurring terms blocks approval readiness |
| T39 | First sale recorded | Does not mark business financially or operationally self-sufficient |
| T40 | Owner supplies no sector preference | Planner does not silently confine discovery to crypto, SaaS or prior ventures |
| T41 | Expense rejected or unanswered | No charge; alternative authorized preparation or wait state |

T33–T41 are additional required cases for Venture Challenge mode. All remain UNTESTED.

| ID | Setup/action | Expected result |
|---|---|---|
| T42 | Internal repo README claims a working feature but implementation is a stub | Asset register marks limitation; economics does not assume working capability |
| T43 | Public repo has unresolved reuse rights | Research may cite it; copying/distribution remains blocked pending resolution |
| T44 | Better-supported new idea competes with sunk internal project | Selection explains prospective tradeoffs; existing project has no automatic preference |
| T45 | Reuse preparation targets original active/frozen project | Isolated draft used; no unrequested mutation or activation |

T42–T45 are required for the Venture Challenge asset-discovery extension; results remain UNTESTED.
