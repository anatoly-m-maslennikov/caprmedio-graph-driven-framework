---
subjects:
  governs: Entity/Object/Continuant/Projection
  depends_on:
  - Entity
  - Entity/Object/Continuant/Projection
version: 24
updated_at: 2026-10-29 07:45:26 +0400
relations:
  child_of:
  - CA-R-1248
atom_id: CA-R-1406@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Keep Entity Identity Independent of Graph Materialization

## Claim scope

Entity identity while a Graph Projection is materialized, refreshed, or deleted.

## Claim

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.

## Details
