# Failure Record schema

```yaml
failure_id: FAIL-<unique>
created_at_utc: <timestamp>
candidate_ref: <ID/version>
family_id: <searchable mechanism family>
proposer: <actor>
why_it_looked_promising: <original rationale and labels>
experiment_and_run_refs: <including failed and incomplete runs>
observed_result: <actual evidence or UNTESTED>
failure_class: <claim falsified, data invalid, execution, risk, inconclusive, retired, other>
cause: <labelled observed cause or inference>
conditions_and_parameters: <frozen configuration and scope>
red_team_findings: <IDs>
veto_and_decision_refs: <IDs>
lesson: <what is supported, without overgeneralizing>
reopening_conditions: <material new evidence or corrected dependency>
replacement_or_child_refs: []
archivist: <actor>
```

A data-invalid or inconclusive experiment does not establish that the underlying idea is false. Keep these distinct from measured falsification. Retain the original record when a candidate is reopened; add a linked new version with a reason.
