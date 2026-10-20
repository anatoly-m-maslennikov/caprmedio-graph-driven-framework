---
subjects:
  governs: "Entity.Identity"
  depends_on:
    ["Entity", "Entity/Node/Continuant/Projection"]
version: 13
updated_at: "2026-10-19 15:52:59 +0400"
relations:
  child_of:
    - CA-R-1248
atom_id: "CA-R-1406"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Keep Entity Identity Independent of Graph Materialization

## Scope

Entity identity while a Graph Projection is materialized, refreshed, or deleted.

## Claim

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.

## Details
