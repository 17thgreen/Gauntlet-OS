# Deterministic gates

This file is an enforcement specification, not a claim that gate software is installed.

## Required gate categories

| Gate | Inputs | Blocking conditions |
|---|---|---|
| Data integrity | Approved manifest, source hashes, timing/quality verdict | Missing approval, unsuitable data, unresolved leakage |
| Specification/freeze | Candidate, experiment, code/config and policy refs | Missing criteria, version mismatch, unauthorized post-freeze change |
| Measurement | Executed code, raw outputs, metrics, sample and uncertainty | Failure, insufficient evidence, unavailable execution |
| Robustness | Registered controls, stresses, ablations and trial accounting | Required tests fail or are absent |
| Protected evaluation | Access record and frozen holdout protocol | Contamination, unauthorized tuning, consumed window relabelled as untouched |
| Replication/forward | Independent-context results and prospectively collected outcomes | Domain prerequisites missing or failed |
| Execution | Verified feasible actions, costs, delays and operational controls | Impossible execution or unresolved operational veto |
| Risk | Approved limits, eligibility and required governor permissions | Active veto, missing/expired approval or limit breach |
| Transition/audit | Matching records and all prerequisites | Stale evidence, conflicting state, missing audit references |

## Evaluation contract

For each gate register ID/version, exact predicate, required inputs, thresholds, applicable stage, responsible authority and output format. Outputs include PASS, FAIL, BLOCKED, INCONCLUSIVE or UNTESTED plus reason and evidence references.

Only PASS satisfies a required scientific gate. A domain may define a limited data approval, but it must encode its restrictions explicitly; it is not unrestricted permission.

Transitions must validate all gate and authorization versions against the current frozen candidate, reject stale or conflicting updates, record the prior/new state atomically and retain an audit record. Deterministic risk stops operate within approved limits without waiting for a team vote.

## Implementation acceptance

Before operational use, demonstrate that missing data, failed gates, stale evidence, active vetoes, unauthorized holdout access and changed candidate versions cannot promote a candidate. Demonstrate that valid complete records permit the intended transition and that halt/demotion records remain recoverable.

A Markdown checklist or language-model assertion alone does not enforce these controls.
