---
subjects:
  governs: "Entity/Continuant/Object/Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit.Structural Level", "Entity/Continuant/Object/Scope Unit.Parent", "Entity/Continuant/Object/Scope Unit.Children", "Entity/Continuant/Object/Scope Unit.Label", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Project.Structure"]
version: 22
updated_at: "2026-10-16 11:59:36 +0000"
relations:
  child_of:
    - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
    - CA-R-1776
atom_id: "CA-R-1730@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Separate structural levels from scope labels

## Scope

Structural Levels **and** Scope Unit Labels.

## Claim

Structural Level **must** follow declared Scope Unit parentage; a retained level number **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's Structural Level, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.

## Details
