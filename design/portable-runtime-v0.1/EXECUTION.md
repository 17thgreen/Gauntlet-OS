# Execution and recovery specification

Date: 2026-09-13. Status: DESIGN DRAFT. No execution guarantees have yet been demonstrated.

## Mission lifecycle

DRAFT → READY → RUNNING → COMPLETED.
RUNNING may enter BLOCKED or PAUSED and resume only after the relevant cause is cleared.
Any nonterminal state may enter CANCELLED; unrecoverable failure may enter FAILED.
Terminal missions are immutable; continuing work uses a new mission/version.

READY requires validated specification, bound required roles and capabilities, permitted resource envelope and resolved execution prerequisites. COMPLETED requires all deliverables accepted and terminal bookkeeping reconciled. It does not imply a commercial claim passed.

## Task lifecycle

| Transition | Required condition |
|---|---|
| PENDING → READY | Dependencies satisfied, inputs available, applicable prerequisites met |
| READY → LEASED | Atomic lease and resource reservation succeed |
| LEASED → RUNNING | Worker acknowledges current lease token |
| RUNNING → SUBMITTED | Outputs finalized and attempt receipt persisted |
| SUBMITTED → ACCEPTED | Applicable independent review and required gate results pass |
| SUBMITTED → REJECTED | Reviewer records scoped defects |
| RUNNING → RETRY_WAIT | Transient failure, safe retry semantics, attempts and budget remain |
| RETRY_WAIT → READY | Retry time reached and prerequisites still valid |
| Any active state → BLOCKED | Missing evidence, active veto, exhausted budget, uncertain side effect |
| Active → CANCELLED | Authorized stop; reconcile in-flight actions |

REJECTED is terminal for that task version. Rework creates a new task version linked to the rejected output and findings. A worker cannot accept a task or clear a veto.

## Authority at the transition boundary

All transitions check authenticated actor mandate, exact mission/subject versions, current vetoes, gate validity, revision and budget in one transaction. The writer persists the transition event and projection together. Stale requests return CONFLICT.

A scientific gate PASS creates eligibility only. External action still requires broker authorization. An expired authorization never invalidates historical evidence, but blocks new effects.

## Proposed transport-neutral API

| Operation | Input | Result |
|---|---|---|
| compile_mission | Draft + existing context/authority refs | Validated draft or scoped errors; no authority granted |
| freeze_mission | Mission version + expected revision | Immutable freeze manifest |
| start_mission | Frozen mission + expected revision | Queued work or blocker |
| lease_task | Worker identity + capabilities | One lease token and bounded packet |
| heartbeat | Lease token | Extended lease or rejected stale token |
| submit_attempt | Lease + request ID + output manifests | Submission receipt, not acceptance |
| record_review | Subject hash + verdict + mandate | Review record |
| request_transition | Exact subject + target + revision | Transition or enumerated blockers |
| prepare_action | Envelope + canonical payload + request key | Reserved action or denial |
| reconcile_action | Action ID + provider evidence | Confirmed/failed/unknown state |
| halt | Scope + issuer mandate + reason | Stop record and reconciliation queue |
| get_status | Mission ID | Projection plus freshness and evidence links |

A later HTTP adapter should preserve semantics: validation errors, unauthorized requests, revision conflicts, blocked prerequisites, transient unavailability and unknown effects must remain distinguishable.

## Leasing and concurrent workers

Use expiring leases and monotonically increasing fencing tokens. An expired worker may upload orphan artifacts but cannot commit authoritative completion. A unique task/revision acceptance prevents double completion.

Leasing order follows Conductor priority, dependencies and budget. Independent ready tasks may run concurrently within the mission limit. Parallelism does not merge certification authority.

After lease expiry, coordinator inspects action receipts before deciding whether another attempt is safe. It must not blindly rerun the whole task if an external effect might have occurred.

## External effects

Persist PREPARED action and budget reservation before issuing the provider call. Recheck authorization and halt state immediately before dispatch. Use a stable provider idempotency key when supported.

If the provider confirms, retain the external ID and response evidence before finalizing. If a timeout leaves outcome uncertain, mark UNKNOWN and query the provider or route for reconciliation. If no reliable reconciliation or idempotency support exists, block automatic retries.

A halt prevents new dispatches. A request already sent may still complete; report that possibility and reconcile it. Compensation is a new scoped action, not deletion of the original event.

Hard budget compliance requires either provider-enforced caps or a reservable upper bound. If neither exists, block autonomous spending rather than claiming software accounting guarantees the cap. Do not release an uncertain reservation as if the action cost zero.

## Crash cases

| Failure point | Recovery |
|---|---|
| Before lease transaction | No task ownership or spend committed |
| After lease, before worker starts | Lease expires; inspect receipts; safely requeue |
| After artifact upload, before submission | Orphan object retained for reconciliation/retention policy |
| After submission, before review | Reviewer resumes from submitted record |
| After review, before next dispatch | Rebuild ready queue from committed state |
| After provider effect, before receipt | UNKNOWN; reconcile before retry |
| During event/projection transaction | Roll back both or commit both |
| During status generation | Rebuild from ledger sequence; show prior projection as stale |

## Retry and time semantics

Every task defines max_attempts, attempt_timeout, retryable error classes and backoff bounds. Validation, authority and scientific failures are not transient infrastructure errors. Preserve the same frozen inputs for a retry; changed inputs create a new version.

Deadlines use server UTC. Trigger occurrences get unique schedule/occurrence keys. Timezone and daylight-saving rules must be explicit for local schedules. Duplicate webhooks or scheduler deliveries must not duplicate accepted work.

## Observability and status

Report mission version, accepted outputs, pending reviews, blocked dependencies, active vetoes, reserved/observed/unknown cost, last event sequence and next permissible step. Summaries are derived; every consequential status links to records.

Capture model/tool version, duration, usage, retries and artifact references, with secret redaction. Raw prompts may contain confidential data and follow the mission's access policy.

Quiet operation means no repeated empty updates; failures in collectors or status generation remain visible operational incidents.

## Backup and restore

Back up both ledger and referenced artifact objects. Restore into a clean environment and verify manifest hashes and referential completeness. Missing artifacts mark dependent evidence unavailable and block affected actions. Never report a restore as successful solely because database rows loaded.
