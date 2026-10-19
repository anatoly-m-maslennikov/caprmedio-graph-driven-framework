---
subjects:
  governs: "Entity/Continuant/Node/Scope Unit"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit.Structural Level", "Entity/Continuant/Node/Scope Unit.Parent", "Entity/Continuant/Node/Scope Unit.Children", "Entity/Continuant/Node/Scope Unit.Label", "Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/Project.Structure"]
version: 23
updated_at: "2026-10-18 03:33:49 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
    - CA-R-1776
atom_id: "CA-R-1730"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1730-CORE_META_MODEL-CORE--separate-structural-levels-from-scope-labels.md
  source_atom_id: CA-R-1730
  source_atom_revision: 23
  source_sha256: 9e8cda4b34f470d4176d0f62fe49b82a2157e2ca428d3e3a8199499714dc4128
  original_relations_sha256: 02c44ffab5879f586ba20d0b697b30c3f316b274fe3e1c202318d46502c49370
---
# Summary

Separate structural levels from scope labels

## Scope

Structural Levels **and** Scope Unit Labels.

## Claim

Structural Level **must** follow declared Scope Unit parentage; a retained level number **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's Structural Level, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.

## Details
