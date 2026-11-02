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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1406-CORE_META_MODEL-CORE--keep-entity-identity-independent-of-graph-materialization.md
  source_atom_id: CA-R-1406
  source_atom_revision: 13
  source_sha256: f6014b6446f01c43b3a7071dc9bff6e11823f9e59e1f220b2c966f05ef33b05c
  original_relations_sha256: 0f1e5f7c7498d6b33c2ed22fb4783b2833b7862d1dd85cabba8ed0441099db31
---
# Summary

Keep Entity Identity Independent of Graph Materialization

## Scope

Entity identity while a Graph Projection is materialized, refreshed, or deleted.

## Claim

materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.

## Details
