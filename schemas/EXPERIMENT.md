# Experiment schema

Register before inspecting judgment outcomes.

Four fields are mandatory and separate. Do not collapse them into `status`.

```yaml
experiment_id: EXP-<unique> | EC-<date>-<slug>
version: <n>

# 1. Admission — is this specified and permitted?
admission: DRAFT | ADMITTED | RETURNED | BAN | NEEDS_DATA
admission_by: <Auditor or Governor>
admission_reason: <text>

# 2. Execution — has work started, paused, or finished?
execution: NOT_STARTED | IN_FLIGHT | PAUSED | FINISHED

# 3. Evidence — what did the test establish, on what population?
evidence_verdict: UNTESTED | BLOCKED | PASS | FAIL | INCONCLUSIVE | KEEP | KILL | REVISE
evidence_scope: <population, window, instrument>
claims_tested:
  - claim: <exact sentence>
    population: <who/what>
    baseline: <comparison>
    primary_outcome: <metric>
    denominator: <unit>
    window: <observation window>
    result: <observed or dash>
    label: "[V]|[I]|[E]|[H]|[A]|[U]"

# 4. Authority — what may the system do next?
authority: NONE | BUILD_INSTRUMENT | SHADOW | LIMITED_PILOT | REPEATABLE_COMMERCIAL | EXPAND | RESTRICT | RETIRE
authority_expiry: <date or none>
revocation: <what evidence removes this authority>

candidate_ref: <ID/version/hash>
family_and_trial_ledger: <related attempts>
question: <specific uncertainty>
hypothesis: <testable claim>
falsification: <predeclared failure result>
institutional_and_domain_refs: <pinned versions>
proposer: <actor>
independent_examiner: <actor>
responsible_builder: <actor>
data_governor_verdict: <record and permitted use>
data_manifests: <source, provenance, hashes, transformations>
research_window: <exact bounds>
validation_window: <exact bounds>
sealed_holdout: <manifest/access-controlled reference>
forward_window: <prospectively defined collection and stop rules>
freeze_record: <timestamp, hashes and issuer>
metrics_and_baselines: <definitions and units>
minimum_sample: <registered threshold>
sample_rationale: <why this n>
stopping_rules: <predeclared>
success_failure_criteria: <exact thresholds>
cost_latency_execution: <inputs and evidence labels>
controls: <placebos, ablations, assigned comparisons>
multiple_testing_policy: <trial accounting and correction>
budget:
  sunk: <already-paid>
  new_commitments: <requires Treasurer>
  categories: <postage, data, certificates, labor, other>
budget_and_stopping_rules: <predeclared>
change_control: <what requires a new version>
required_deliverables: <completion conditions>
code_config_environment: <immutable references>
actual_runs: <run IDs, outputs, errors, omissions and hashes>
human_workload:
  minutes_per_deliverable: <observed or dash>
  fixed_hours_per_week: <observed or dash>
  pct_no_intervention: <observed or dash>
  exception_rate: <observed or dash>
  absolute_hours_cap: <for the authority requested>
evidence_and_decisions: <linked records>
```

Keep planned settings separate from observed outputs. Missing criteria block execution as a promotion test; exploratory runs must be labelled exploratory. Failed holdouts remain consumed. New versions cannot silently reuse their results as untouched validation.

Admission is not evidence. Evidence KEEP is not authority to expand.
