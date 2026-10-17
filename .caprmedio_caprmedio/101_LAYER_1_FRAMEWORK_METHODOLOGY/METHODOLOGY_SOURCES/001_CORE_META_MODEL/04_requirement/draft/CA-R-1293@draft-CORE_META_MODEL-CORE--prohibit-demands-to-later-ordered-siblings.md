---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit.Local Order", "Entity/Continuant/Node/Scope Unit/Type: Ordered"]
version: 16
updated_at: "2026-10-17 23:21:45 +0000"
relations: {}
atom_id: "CA-R-1293@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Prohibit Demands to Later Ordered Siblings

## Scope

Demand Atoms owned by Ordered Scope Units.

## Claim

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.

## Details
