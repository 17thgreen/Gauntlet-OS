# Design decision register

Date: 2026-09-13. Status: engineering recommendations for v0.1, not adopted constitutional amendments.

## Selected design assumptions

| ID | Decision | Reason | Reconsider when |
|---|---|---|---|
| D01 | Separate artifact acceptance, claim eligibility and action authorization | Prevent completed output from masquerading as commercial proof or permission | Any domain demonstrates a missing distinction |
| D02 | Domain packs and workflow templates are separate | Same domain contains research, production and operations | Composition becomes ambiguous |
| D03 | Typed mission specification precedes execution | Makes objectives, dependencies and limits inspectable | Simpler equivalent preserves all guarantees |
| D04 | One modular deployable application first | Limits operating burden | Measured scaling or isolation needs justify splitting |
| D05 | Python/PostgreSQL and LangGraph adapter as first prototype candidates | Concrete build path consistent with prior research | M2 comparison shows poor fit |
| D06 | Ledger and accepted artifacts remain runtime-independent | Preserves institution across model/framework changes | Never waive portability without explicit decision |
| D07 | Side effects use broker and reconciliation | Retries otherwise risk duplicate actions | Provider semantics support a simpler equivalent |
| D08 | Capability changes compete against baseline | Prevents skill accumulation without demonstrated improvement | Test policy evolves prospectively |
| D09 | Three synthetic/supplied fixtures before live operations | Tests domain portability without claiming demand | Fixture coverage proves inadequate |
| D10 | Core code does not encode marketing or crypto terminology | Keeps domain specialization out of scheduling and authority mechanics | A genuinely universal primitive is identified |

## Unresolved decisions

| ID | Question | Blocks | Resolution method |
|---|---|---|---|
| U01 | Where will production runtime code live? | Production implementation placement | Record repository decision respecting current protocol/domain boundaries |
| U02 | Which hosting environment provides the required identity and storage separation? | Production enforcement claim | Demonstrate service identities, protected data access and restore |
| U03 | Can the GrokBot account invoke the chosen runtime through a supported interface? | Seamless GrokBot control | Small authenticated compatibility test; file handoff remains possible |
| U04 | Which models and actual resource budgets apply? | Paid model-backed evaluation | Bind existing authorization or obtain a concrete budget decision |
| U05 | Which live business mission follows fixtures? | Live pilot | Select based on available inputs and measurable benefit; held opportunities remain held |
| U06 | What process improvement threshold merits adoption? | Improvement claim | Baseline first; preregister final criteria before judgment |
| U07 | What retention and recovery objectives apply? | Production readiness | Bind deployment-specific data policy and restore targets |
| U08 | How will non-crypto empirical claims map every required promotion stage? | Commercial claim promotion | Domain-specific adoption record; no silent stage deletion |
| U09 | Who independently reviews implementation and tests? | Independent release certification | Bind accountable reviewer distinct from author |

Unknowns block their affected operation, not continued specification work.

## Compatibility with current institution

- Existing authorities and hard vetoes are retained.
- The generic promotion ladder remains authoritative for empirical candidates.
- Workflow completion is a separate operational concept; it cannot certify a candidate.
- Existing schemas are wrapped with runtime metadata, not discarded.
- Conflicts require prospective resolution; frozen runs retain original rules.
- The strategy memo remains historical research, not dependency clearance.
- Tax Appeal OS remains held; no live crypto lab changes are part of this package.

## Evidence status

All architecture performance claims are hypotheses. Documentation review supports component selection for investigation, not effectiveness. See the [strategy memo sources](../../records/strategy/2026-09-13-portable-gauntlet-os-strategy-memo.md#sources).

Implementation acceptance, operational isolation, recovery guarantees, time savings and commercial outcomes remain UNTESTED until recorded execution.

## Follow-up requirement: Venture Challenge

Logan explicitly requested a challenge-based mode with creative business selection, distinct specialist contributions, hierarchy, multifaceted commercial assessment, a possible $500 budget, and human approval before money is spent. This is now a product requirement. D11: implement Venture Challenge as a composition of workflows, not a preset niche. D12: capital availability never substitutes for human spending authorization. U10: real mission funding, owner identity, compute allowance and external action scope remain unbound. No live venture is commissioned by this design conversation.

D13 — Asset and idea search is explicitly broad: all accessible owner GitHub repos and prior work, compatible open-source code and online content, and independently discovered ideas. This requirement comes from Logan's second follow-up. Reuse preserves source lineage, actual capability evidence and applicable rights; it does not authorize modifying original projects or bypassing existing holds.
