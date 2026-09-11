# Experiment schema

Register before inspecting judgment outcomes.

```yaml
experiment_id: EXP-<unique>
version: <version>
candidate_ref: <ID/version/hash>
family_and_trial_ledger: <all related attempts>
question: <specific uncertainty>
hypothesis: <testable claim>
falsification: <predeclared failure result>
institutional_and_domain_refs: <pinned versions>
proposer: <actor>
independent_examiner: <actor>
data_governor_verdict: <record and permitted use>
data_manifests: <source, provenance, hashes, transformations>
research_window: <exact bounds>
validation_window: <exact bounds>
sealed_holdout: <manifest/access-controlled reference>
forward_window: <prospectively defined collection and stop rules>
freeze_record: <timestamp, hashes and issuer>
metrics_and_baselines: <definitions and units>
minimum_sample: <registered threshold>
success_failure_criteria: <exact thresholds>
cost_latency_execution: <inputs and evidence labels>
controls: <placebos, ablations, perturbations, stress and replication>
multiple_testing_policy: <trial accounting and correction>
budget_and_stopping_rules: <predeclared>
code_config_environment: <immutable references>
actual_runs: <run IDs, outputs, errors, omissions and hashes>
status: <REGISTERED, UNTESTED, BLOCKED, PASS, FAIL, INCONCLUSIVE>
evidence_and_decisions: <linked records>
```

Keep planned settings separate from observed outputs. Missing criteria block execution as a promotion test; exploratory runs must be labelled exploratory. Failed holdouts remain consumed. New versions cannot silently reuse their results as untouched validation.
