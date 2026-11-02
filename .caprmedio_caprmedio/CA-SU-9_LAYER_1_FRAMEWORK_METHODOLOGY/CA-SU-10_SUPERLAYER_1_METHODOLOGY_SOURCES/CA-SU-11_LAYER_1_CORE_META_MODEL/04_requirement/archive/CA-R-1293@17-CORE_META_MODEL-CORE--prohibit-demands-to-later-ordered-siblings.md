---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit.Local Order", "Entity/Node/Continuant/Scope Unit/Type: Ordered"]
version: 17
updated_at: "2026-10-19 15:52:45 +0400"
relations: {}
atom_id: CA-R-1293@17
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
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
