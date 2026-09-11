# Decision Record schema

```yaml
decision_id: DEC-<unique>
timestamp_utc: <timestamp>
decision_type: <promotion, demotion, veto, clearance, freeze, amendment, other>
candidate_or_policy_ref: <ID/version>
prior_state: <state>
requested_state: <state>
decision: <approved, rejected, blocked, suspended>
rule_refs: <exact adopted policy and gate versions>
evidence_refs: <actual evidence IDs>
gate_results: <all required gates and their status>
active_vetoes: <IDs or explicitly none after checking>
independence_check: <proposer, examiner, authorizers>
decision_authorities: <actual actors, mandates, authorizations and times>
reason: <evidence-linked rationale>
dissent_and_alternatives: <retained findings>
conditions_limits_expiry: <binding scope>
actions: <owner, required output, deadline>
supersedes: <prior record or none>
```

For an amendment add the required chain:

**RULE → REASON → EVIDENCE → APPROVER → DATE → VERSION**

Include old/new text, effective scope/date, affected records, migration and rollback treatment. Preserve frozen experiments under their recorded version. An empty approver field is not approval; a Conductor summary is not a governor's signature.
