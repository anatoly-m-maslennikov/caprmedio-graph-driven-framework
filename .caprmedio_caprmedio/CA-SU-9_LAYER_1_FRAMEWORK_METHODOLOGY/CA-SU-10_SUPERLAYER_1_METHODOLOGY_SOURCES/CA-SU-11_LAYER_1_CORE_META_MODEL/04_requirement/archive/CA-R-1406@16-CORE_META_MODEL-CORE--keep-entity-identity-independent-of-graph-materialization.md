---
subjects:
  governs: Entity.Identity
  depends_on:
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/Projection
version: 16
updated_at: 2026-10-24 00:51:05 +0400
relations:
  child_of:
  - CA-R-1248
atom_id: CA-R-1406@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Keep Entity Identity Independent of Graph Materialization

## Scope

Entity identity while a Graph Projection is materialized, refreshed, or deleted.

## Claim

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.

## Details
