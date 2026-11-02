---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit.Local Order", "Entity/Continuant/Object/Scope Unit/Type: Ordered"]
version: 15
updated_at: "2026-10-16 12:08:19 +0000"
relations: {}
atom_id: "CA-R-1293"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
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
