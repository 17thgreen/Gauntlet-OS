# Gauntlet-OS

> AI proposes. Code measures. Evidence promotes. Risk governs. Outcomes decide.

Gauntlet-OS is the reusable institutional architecture for a governed multi-agent organization. It defines how independent specialists produce atomic claims, how code tests them, how independent authorities block unsafe or unsupported action, and how outcomes become institutional memory.

**Lifecycle (ratified 2026-09-16):** Discover → Experiment → Operate. Each stage earns a specific next authority. See [constitution/LIFECYCLE.md](constitution/LIFECYCLE.md).

## Repository boundary

- **Institutional protocol:** [17thgreen/Gauntlet-OS](https://github.com/17thgreen/Gauntlet-OS).
- **Crypto proving ground:** [17thgreen/GrokBot---The-GauntletV2-](https://github.com/17thgreen/GrokBot---The-GauntletV2-). Keep its active research, code, domain rules, experiment records, and operational state there.
- **ALMANAC proving ground:** [17thgreen/ClaudeCodeInsuranceOS](https://github.com/17thgreen/ClaudeCodeInsuranceOS). Bind via [domain-packs/almanac-ga](domain-packs/almanac-ga/README.md).
- **Opportunity registry (tax appeal and siblings):** [17thgreen/AI-Venture-Capital-System](https://github.com/17thgreen/AI-Venture-Capital-System/blob/main/REGISTRY.md).
- The live proving ground should link back to Gauntlet-OS and pin the exact institutional commit it adopts. Publication here does not silently amend an existing frozen experiment or the live lab's constitution.

This repository documents an operating protocol. It does not implement a running agent system, deterministic test engine, enforced permissions, or an approved capital deployment. Those controls must be implemented and verified in each domain.

## Start here

1. Read the [constitution](constitution/GAUNTLET_PROTOCOL_V2.md), [lifecycle](constitution/LIFECYCLE.md), [authority model](constitution/AUTHORITY_MODEL.md), [communication rules](constitution/COMMUNICATION_RULES.md), [evidence standard](constitution/EVIDENCE_STANDARD.md), and [promotion protocol](constitution/PROMOTION_PROTOCOL.md).
2. Assign accountable actors using the [role charters](roles/conductor.md), [Challenger](roles/challenger.md), [Operate](roles/operate.md), and [specialist template](roles/specialist-template.md).
3. Register claims using [Atomic Ideas](schemas/ATOMIC_IDEA.md), [Evidence Cards](schemas/EVIDENCE_CARD.md), [Experiments](schemas/EXPERIMENT.md) (four status fields), [Failure Records](schemas/FAILURE_RECORD.md), and [Decision Records](schemas/DECISION_RECORD.md).
4. Apply [routing](protocols/ROUTING.md), [Challenge](protocols/CHALLENGE.md), [Red Team review](protocols/RED_TEAM.md), [deterministic gates](protocols/DETERMINISTIC_GATES.md), [Cemetery rules](protocols/CEMETERY.md), and [versioning](protocols/VERSIONING.md).
5. Bind a [domain pack](domain-packs/template/README.md). Reference packs: [crypto alpha](domain-packs/crypto-alpha/README.md), [almanac-ga](domain-packs/almanac-ga/README.md).
6. Complete the [adoption record](records/BASELINE.md) to reconcile a live lab with this record.
7. Park uncommissioned ideas in [records/FUTURE_IDEAS.md](records/FUTURE_IDEAS.md). Do not treat that file as a backlog of approved work.

## Core operating pattern

Objective → Discover (Challenge) or Experiment Conductor commissions bounded work → independent specialists → atomic registry → optional Architect synthesis → deterministic Examiner → Red Team → governors → staged authority → observed outcomes → Archivist → next cycle.

Failures, vetoes, and demotions remain in the record. Agreement is not evidence. The proposer never grades its own claim. Abstention is a successful outcome when evidence or permission is missing.

## Baseline and provenance

This documentation seed originally codified architecture from the referenced “Pokémon Card Arbitrage” conversation. Lifecycle ratification 2026-09-16 adds Discover/Experiment/Operate, four-field experiment status, and the ALMANAC pack binding. It contains no asserted experiment results.

See [source and adoption notes](records/BASELINE.md), [DR-20260916-ALMANAC-PRIMARY](records/strategy/DR-20260916-ALMANAC-PRIMARY.md), and [future ideas](records/FUTURE_IDEAS.md).

Store governance, small audit artifacts, manifests, hashes, provenance, and acquisition instructions in Git. Keep raw market archives, bulk datasets, secrets, keys, and credential-bearing URLs on appropriately controlled storage.
