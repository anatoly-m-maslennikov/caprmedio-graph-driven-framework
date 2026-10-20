---
subjects:
  governs: "Entity/Node/Continuant/Atom.Substance"
  depends_on:
    ["Atom Scope", "Entity/Node/Continuant/Atom.Substance", "Claim Value Set", "Property", "IS_ALLOWED_VALUE_OF"]
version: 16
updated_at: "2026-10-19 15:52:53 +0400"
relations:
  child_of:
    - CA-R-918
    - CA-R-1596
atom_id: "CA-R-1358"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1358-CORE_META_MODEL-GENERAL--consolidate-single-value-claims-as-one-value-set-claim.md
  source_atom_id: CA-R-1358
  source_atom_revision: 16
  source_sha256: df9ce8db22c891a4f07632b50afef6462adbdc921a6031560c572d17556ac154
  original_relations_sha256: 76c3beb05ab71c7f3fb555e25cf340c6946d6ed275fb430f9bb136e49c7be086
---
# Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Scope

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.

## Claim

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.

## Details
