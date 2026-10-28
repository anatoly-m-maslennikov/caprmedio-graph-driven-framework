---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
version: 22
updated_at: 2026-10-27 19:59:54 +0400
relations:
  child_of:
  - CA-R-1248
atom_id: CA-R-1406
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Keep Entity Identity Independent of Graph Materialization

## Scope

Entity identity while a Graph Projection is materialized, refreshed, or deleted.

## Claim

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.

## Details
