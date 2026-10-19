---
subjects:
  governs: "Entity/Node/Continuant/Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Structural Level", "Entity/Node/Continuant/Scope Unit.Parent", "Entity/Node/Continuant/Scope Unit.Children", "Entity/Node/Continuant/Scope Unit.Label", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Project.Structure"]
version: 24
updated_at: "2026-10-19 11:42:14 +0000"
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
