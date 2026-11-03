---
subjects:
  active: Projection
  passive:
  - Entity
  - Projection
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2462
atom_id: CA-R-1406
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Keep Entity Identity Independent of Graph Materialization

## Claim scope

Entity identity while a Graph Projection is materialized, refreshed, or deleted.

## Claim

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
