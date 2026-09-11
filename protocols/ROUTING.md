# Routing protocol

1. **Objective → Conductor:** define a bounded uncertainty and inspect prior failures.
2. **Conductor → specialist:** send a commission with allowed inputs, artifact schema, budget and kill test.
3. **Specialist → Archivist/registry → Conductor:** register the original Atomic Idea, label claims and flag unknowns.
4. **Data → data governor:** obtain provenance, quality and timing approval before dependent measurement.
5. **Candidate → Architect when useful:** combine tested components with explicit lineage and ablations.
6. **Frozen experiment → Examiner:** execute deterministic tests on authorized data.
7. **Failure → Cemetery:** preserve results and distinguish invalid data from falsified claims.
8. **Survivor → Prosecutor:** test alternative explanations and close material findings with evidence.
9. **Eligible version → execution and risk governors:** check feasibility and permitted exposure.
10. **Decision → deterministic state registry → Archivist:** transition only when all prerequisites and authorizations match.
11. **Operation → outcome/drift monitoring → governors/Conductor:** halt or demote when required; use outcomes in the next cycle.

## Handoff envelope

Every handoff includes message/commission ID, sender, recipient, trigger, candidate/version, authoritative input refs, requested output, permitted access, constraints, deadline, and return route. Reconcile duplicate requests by ID; retain rejected or superseded submissions.

Missing input returns BLOCKED with the missing dependency and responsible actor. Silence is not approval. Urgent data, execution or risk alerts reach the responsible governor immediately and are recorded; routine scheduling cannot suppress them.

Full-team chat is not a routing mechanism. Board exceptions follow the [communication rules](../constitution/COMMUNICATION_RULES.md).
