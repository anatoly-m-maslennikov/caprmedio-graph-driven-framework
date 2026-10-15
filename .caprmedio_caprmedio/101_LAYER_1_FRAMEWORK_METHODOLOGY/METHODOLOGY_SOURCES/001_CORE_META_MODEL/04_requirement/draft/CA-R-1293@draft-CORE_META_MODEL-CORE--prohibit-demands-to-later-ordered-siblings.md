---
subjects:
  governs: "Demand Direction"
  depends_on:
    ["Local Order", "Entity/Continuant/Object/Scope Unit/Type: Ordered"]
version: 14
updated_at: "2026-10-15 18:13:46 +0000"
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
