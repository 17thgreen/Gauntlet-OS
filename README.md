# Gauntlet-OS

> AI proposes. Code measures. Evidence promotes. Risk governs. Outcomes decide.

Gauntlet-OS is the reusable institutional architecture for a governed multi-agent organization. It defines how independent specialists produce atomic claims, how code tests them, how independent authorities block unsafe or unsupported action, and how outcomes become institutional memory.

## Repository boundary

- **Institutional protocol:** [17thgreen/Gauntlet-OS](https://github.com/17thgreen/Gauntlet-OS).
- **Live crypto proving ground:** [17thgreen/GrokBot---The-GauntletV2-](https://github.com/17thgreen/GrokBot---The-GauntletV2-). Keep its active research, code, domain rules, experiment records, and operational state there. No second Alpha-Lab repository is needed.
- The live proving ground should link back to Gauntlet-OS and pin the exact institutional commit/version it adopts. Publication here does not silently amend an existing frozen experiment or the live lab's constitution.

This repository documents an operating protocol. It does not implement a running agent system, deterministic test engine, enforced permissions, or an approved capital deployment. Those controls must be implemented and verified in each domain.

## Start here

1. Read the [constitution](constitution/GAUNTLET_PROTOCOL_V2.md), [authority model](constitution/AUTHORITY_MODEL.md), [communication rules](constitution/COMMUNICATION_RULES.md), [evidence standard](constitution/EVIDENCE_STANDARD.md), and [promotion protocol](constitution/PROMOTION_PROTOCOL.md).
2. Assign accountable actors using the [role charters](roles/conductor.md) and [specialist template](roles/specialist-template.md).
3. Register claims using [Atomic Ideas](schemas/ATOMIC_IDEA.md), [Evidence Cards](schemas/EVIDENCE_CARD.md), [Experiments](schemas/EXPERIMENT.md), [Failure Records](schemas/FAILURE_RECORD.md), and [Decision Records](schemas/DECISION_RECORD.md).
4. Apply [routing](protocols/ROUTING.md), [Red Team review](protocols/RED_TEAM.md), [deterministic gates](protocols/DETERMINISTIC_GATES.md), [Cemetery rules](protocols/CEMETERY.md), and [versioning](protocols/VERSIONING.md).
5. Bind a [domain pack](domain-packs/template/README.md). The first reference application is [crypto alpha](domain-packs/crypto-alpha/README.md).
6. Complete the [adoption record](records/BASELINE.md) to reconcile the live lab with this record.

## Core operating pattern

Objective → Conductor commissions bounded work → independent specialists → atomic registry → optional Architect synthesis → deterministic Examiner → Red Team → governors → staged operation → observed outcomes → Archivist → next cycle.

Failures, vetoes, and demotions remain in the record. Agreement is not evidence. The proposer never grades its own claim. Abstention is a successful outcome when evidence or permission is missing.

## Baseline and provenance

This initial documentation seed codifies the architecture and later refinements in the referenced “Pokémon Card Arbitrage” conversation, as explicitly requested by the repository owner. It contains no asserted experiment results. See [source and adoption notes](records/BASELINE.md).

Detailed schema field names and generic domain mappings are implementation conventions for this seed; they are not claims that identical files or deployed controls already existed in the live lab. Missing domain thresholds remain unknown until recovered from authoritative records or approved prospectively.

Store governance, small audit artifacts, manifests, hashes, provenance, and acquisition instructions in Git. Keep raw market archives, L2/trade ZIPs, bulk datasets, secrets, keys, and credential-bearing URLs on appropriately controlled storage.
