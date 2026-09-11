# Atomic Idea schema

Use one independently testable claim per record. Crypto calls this an Atomic Edge Card.

```yaml
idea_id: IDEA-<unique>
version: <version>
family_id: <mechanism family>
author: <actor>
created_at_utc: <timestamp>
institutional_ref: <commit/version>
domain_ref: <commit/version>
status: HYPOTHESIS
claim: <precise falsifiable statement>
claim_label: "[H]"
scope: <domain, population/instrument, horizon, conditions>
mechanism_or_rationale: <labelled explanation>
required_data: <manifest IDs, fields, timing and access>
operational_definition: <formula or unambiguous procedure>
action_entry: <exact rule>
exit_or_completion: <exact rule>
abstention: <exact no-action rule>
parameters: <names, values, ranges, count>
cost_and_latency_inputs: <values with labels, or unknown>
expected_failure_conditions: <where and why it may fail>
alternative_explanation: <competing account>
falsification_test: <result that kills claim>
placebo_and_robustness: <registered controls and perturbations>
dependencies: <idea IDs and exact versions>
prior_failures: <Cemetery links; novelty justification>
experiment_refs: []
evidence_refs: []
decision_refs: []
```

Confidence may be recorded as subjective [I], never as certification. Replace placeholders before testing; unknown required inputs block the relevant gate. Preserve previous versions and parent links.
