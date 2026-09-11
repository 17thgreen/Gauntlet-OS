# Versioning and amendments

Pin institutional policy, domain policy, candidate, dataset, experiment, code, configuration and evidence independently. Record immutable Git commits and content hashes; branch names alone are not reproducibility anchors.

## Baseline

Capture a dedicated governance commit before changing the live lab's institutional design. The previously suggested live-lab tag is **gauntlet-v2.0-alpha**. Verify whether it already exists and what commit it identifies before creating or using it. Never move a baseline tag to hide later changes.

The initial Gauntlet-OS seed is a separate institutional record. Its publication is not evidence that the live lab's mirror, baseline tag or adoption is complete. Record an exact institutional seed commit and a separate live adoption Decision Record.

## Amendment record

Every governance change records:

**RULE → REASON → EVIDENCE → APPROVER → DATE → VERSION**

Also retain old/new wording, scope, affected roles/artifacts, effective date, rollout/rollback treatment and links to the authorizing Decision Record. Missing approvals remain explicitly pending. Cosmetic corrections should still have attributable commits; substantive authority/gate changes require an amendment.

Version identifiers must be unique and ordered within their artifact family. Existing frozen version schemes are retained; any naming migration is explicit. Never alter a frozen experiment's policy retroactively to rescue its outcome.

## Changes after evaluation

Changed hypotheses, thresholds, costs, transformations, combinations or feature definitions create new versions and identify prior trials. Any holdout-influenced revision requires a new untouched future holdout. Retain assumption-based results when real inputs replace them.

## Cross-repository adoption

The live implementation pins the institutional commit and its own domain addendum. Reconcile differences explicitly; do not automatically overwrite domain rules from the latest main branch. Submit prospective amendments for conflict resolution while preserving already frozen research.

Git stores governance and compact records. Raw data, archives and secrets remain off-repository, with controlled manifests, provenance and hashes.
