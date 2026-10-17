---
subjects:
  governs: "Entity/Continuant/Object/Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit.Structural Level", "Entity/Continuant/Object/Scope Unit.Parent", "Entity/Continuant/Object/Scope Unit.Children", "Entity/Continuant/Object/Scope Unit.Label", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Project.Structure"]
version: 22
updated_at: "2026-10-16 12:08:40 +0000"
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
  source_atom_revision: 22
  source_sha256: 64a4620c08edc01a02fa9b6c45646514529f2d46bf780af83fc3a5ae66dc7db4
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
