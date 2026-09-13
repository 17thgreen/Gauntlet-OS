# Portable contracts specification

Date: 2026-09-13. Status: DESIGN DRAFT. This document specifies semantic contracts; JSON Schema and database migrations are B01/B02 deliverables, not supplied executable validators.

## Common record envelope

All durable records require schema_version, record_id, record_version (positive integer), mission_id, created_at_utc, authenticated_actor_id, and immutable payload reference/hash. References use record_id + version + content hash. Mutable entity projections also carry revision for compare-and-swap.

UTC timestamps must include timezone. Money uses integer minor units and explicit currency; resource units are explicit. Unknown values use null plus an unresolved reason, never a fabricated zero. Planned values and observed values occupy different fields.

Unknown required fields block only the operation that requires them. They need not prevent drafting or exploratory work clearly labeled as such.

## MissionSpec

| Field | Type / constraint |
|---|---|
| objective | Nonempty outcome statement |
| completion_scope | artifact, empirical_claim, operation, or explicit combination |
| institutional_ref | Repository + exact commit + adoption record reference |
| domain_bindings | Nonempty list of pack IDs, versions and hashes |
| workflow_ref | Template ID, version and hash |
| context_refs | Source and company-context references with applicability |
| deliverables | Artifact type, acceptance criteria, reviewer and evidence requirements |
| claim_refs | Atomic Idea versions; empty when no empirical claim is submitted |
| experiment_refs | Existing Experiment records for promotion tests |
| authority_bindings | Required function → authenticated accountable actor; no missing required actor |
| task_graph | Task IDs and dependency edges; acyclic |
| budget | Currency, spend cap, worker limits, wall-clock deadline, intervention policy |
| authorization_refs | Existing action envelopes; may be empty for internal-only work |
| stop_rules | Structured conditions and responsible issuer |
| unresolved | Field, reason, affected operation and resolution owner |
| applicability | Domain/population/time scope and excluded uses |

Mission freezing produces a manifest of all referenced versions. Editing a frozen specification creates a new version and an explicit transition; it does not mutate the earlier freeze.

## DomainPack

Required fields: pack_id, version, compatible_core_schema_versions, vocabulary, source requirements, role mandates, artifact schemas, workflow bindings, measurement definitions, applicable gate IDs, claim promotion mapping, action classes, abstention state, fixtures, capability dependencies and policy references.

A pack must explain what success does and does not establish. It cannot mark a constitutional requirement optional. A task producing an artifact without promoting a hypothesis does not use artifact acceptance to bypass the existing claim ladder.

Pack composition is restrictive: intersect permitted actions, preserve all required reviews, reject conflicting metric units or authority bindings. The compiler flags contradictions; it does not choose the permissive interpretation.

## TaskSpec and TaskAttempt

TaskSpec: task_id, mission version, kind, owner function, allowed worker identity, input_refs, dependency_ids, capability_refs, expected_outputs, acceptance_rule_refs, reviewer binding, effects, resource envelope, timeout, retry policy, stop condition.

TaskAttempt: attempt_id, task_id/version, lease_token, lease_expiry, started/ended timestamps, worker configuration, tool-call references, output_refs, observed usage, result and failure classification.

Task kind: CODE, AGENT, HUMAN_REVIEW, GATE, EXTERNAL_ACTION. A new attempt never erases an earlier failed attempt. Duplicate output submissions resolve using a stable request id and payload digest.

A dependency defaults to predecessor ACCEPTED, not merely worker-finished. Alternative dependency conditions must be explicit in a registered workflow.

## ArtifactManifest

artifact_id/version; media_type; location; SHA-256; byte_count; producer attempt; source_refs; extraction/version information; created time; confidentiality/access scope; acceptance_status; reviewer record; limitations.

Artifact statuses: SUBMITTED, ACCEPTED, REJECTED, SUPERSEDED. Acceptance points to a review of exact bytes. A later change invalidates that review for the new version.

## Evidence and experiment compatibility

Use the existing [Atomic Idea](../../schemas/ATOMIC_IDEA.md), [Evidence Card](../../schemas/EVIDENCE_CARD.md), [Experiment](../../schemas/EXPERIMENT.md), [Failure Record](../../schemas/FAILURE_RECORD.md) and [Decision Record](../../schemas/DECISION_RECORD.md) as semantic authorities.

Runtime manifests wrap and reference these records; they do not replace their scientific fields. Preserve [V], [I], [A], [H], [U] labels. A fixture value is explicitly synthetic. Sealed data refs are opaque to unauthorized workers.

## ReviewRecord and GateResult

ReviewRecord: subject refs, reviewer identity, reviewer mandate, method, criteria version, verdict, findings and supporting evidence. The reviewer cannot be the subject's author for independent certification.

GateResult: gate_id/version, subject/version, policy and freeze refs, input hashes, evaluator code/config/environment refs, run ref, result, scope, limitations, issuer and validity interval when relevant.

Gate results: PASS, FAIL, BLOCKED, INCONCLUSIVE, UNTESTED. Only PASS satisfies a required scientific gate. A negative business recommendation may still satisfy the separate artifact-delivery criteria.

Freshness is gate-specific. A report source can remain valid while a quote used for an action expires. Do not infer freshness from file modification time.

## AuthorizationEnvelope and ActionReceipt

AuthorizationEnvelope requires issuer identity, mandate reference, mission version, allowed action types, exact target scope, payload restrictions, maximum quantity and spend, currency, valid interval, prerequisites, revocation status and approval evidence. It must encode actual prior authorization, never a worker's claim that approval exists.

ActionReceipt requires action_id, request key, canonical payload digest, envelope reference, budget reservation, provider, external reference, request/response references with secrets redacted, timestamps, actual effect/cost, and status.

Statuses: PREPARED, AUTHORIZED, DISPATCHING, CONFIRMED, FAILED, UNKNOWN, CANCELLED. UNKNOWN is not retry permission.

Approval is bound to payload or explicit permitted variation. Changed target, price beyond approved range, mission version or content outside that variation requires a new authorization.

## Event envelope

event_id; sequence; entity_id; previous_revision; new_revision; event_type; UTC time; actor; payload_ref; causation_id; correlation_id; request_id.

A uniqueness constraint on actor/request_id rejects conflicting retries. Event ordering uses server sequence and revisions; client timestamps do not decide winners.

## Compilation rejection codes

SCHEMA_INVALID, UNRESOLVED_REQUIRED_FIELD, POLICY_CONFLICT, MISSING_AUTHORITY, DUTY_CONFLICT, DEPENDENCY_CYCLE, CAPABILITY_UNAVAILABLE, BUDGET_UNBOUND, EVALUATION_UNBOUND, REFERENCE_MISMATCH.

Compilation returns all detectable errors with affected paths and blocking scope. No repair is silently applied to authoritative input.

## Venture Challenge extension

MissionSpec additionally binds operating_mode=VENTURE_CHALLENGE, selection_criteria, asset_inventory_ref, candidate_register_ref, human_dependency_envelope, and spending_policy=HUMAN_APPROVAL_BEFORE_SPEND. Capital ceiling and authorization are distinct fields. Each paid dispatch must reference an actual human-issued authorization envelope. An automated Treasurer can validate or veto a purchase but cannot supply the required human approval. Candidate selection, task routing and free preparation remain delegated within the mission. See [Venture Challenge](VENTURE_CHALLENGE.md).
