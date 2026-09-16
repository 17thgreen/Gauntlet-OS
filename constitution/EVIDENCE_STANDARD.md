# Evidence standard

Every material claim uses an explicit label:

| Label | Meaning | Required handling |
|---|---|---|
| [V] | Observed / verified | Cite an inspectable source or executed run, scope, date and verification method |
| [I] | Inference | State the reasoning and linked premises; separate inference from direct observation |
| [A] | Assumption | Declare the unobserved input, rationale, sensitivity and permitted use |
| [H] | Hypothesis | State a falsifiable claim and what would disprove it |
| [E] | Estimate / scenario | Explicit model or forecast; list inputs, formula, and that it is not an observed outcome |
| [U] | Unknown | State what is missing and the next observation needed |

Labels apply at the claim/input level. An Evidence Card may contain all six. A measured result conditional on assumed costs can be [V] as a simulation output while the costs remain [A]; it is not verified executable performance.

## Observed results vs estimates

Front-door metrics and Examiner totals contain **observed** outcomes only. Unobserved claimed results are dashes or UNTESTED.

Estimates, synthetic demonstrations, and scenario models are permitted when:

- labeled `[E]`, `[H]`, or `[A]`;
- assumptions are listed;
- they cannot be copied into an economics or learning aggregate;
- DEMO / synthetic rows stay bound to a DEMO label.

## Measurement requirements

Quantitative claims require the experiment and candidate version, approved dataset manifest/hash, code commit, configuration, environment, run ID, actual outputs and independent Examiner verdict. Record exclusions, uncertainty, sample size, costs and failed attempts. Retain original output files on controlled storage with immutable references.

Use **UNTESTED** when code was not executed, **BLOCKED** when prerequisites are missing, and **INCONCLUSIVE** when evidence cannot support a determination. None is a pass. These are evidence-verdict values, not admission or authority.

Never invent performance, fills, prices, fees, latency, counts, customer outcomes, or completed approvals. Model confidence is opinion, not a measured probability unless separately calibrated and evidenced.

## Scope discipline

A statistical association does not verify its proposed causal mechanism. Success in one instrument family cannot establish another without the appropriate evidence. A historical holdout does not prove future performance. Replication does not make evidence universal outside the measured conditions.

Provisional tests remain provisional until real inputs and domain prerequisites are verified and the required tests rerun. Preserve the assumption-versus-reality comparison.

Consensus, argument quality, and a proposer's own judgment cannot certify a claim. See the [Evidence Card](../schemas/EVIDENCE_CARD.md) and [Lifecycle](LIFECYCLE.md).
