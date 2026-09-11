# Evidence Card schema

Record what was actually observed and what it supports.

```yaml
evidence_id: EVID-<unique>
version: <version>
candidate_ref: <ID/version>
experiment_ref: <ID/version>
run_id: <actual run ID or UNTESTED>
claims:
  - statement: <one material claim>
    label: <[V], [I], [A], [H], or [U]>
    source_ref: <inspectable source/run output>
    scope_and_limitations: <what is and is not supported>
dataset_refs: <manifest IDs and hashes>
code_ref: <commit/hash>
configuration_ref: <immutable config/hash>
environment_ref: <runtime/dependencies/seed>
observed_at_utc: <timestamp or unknown>
metrics: <actual outputs, units, uncertainty and sample size>
assumed_inputs: <labelled assumptions and sensitivities>
exclusions_and_failed_runs: <complete references>
output_refs: <immutable locations and hashes>
examiner: <independent actor>
gate_results: <gate ID, criterion, actual result, status>
limitations: <remaining unknowns and permitted use>
supersedes: <prior record or none>
```

Use null/unknown for unavailable values; never populate sample numbers as results. Evidence labels and gate status are separate. An executed simulation under [A] inputs verifies the conditional simulation, not real-world viability.
