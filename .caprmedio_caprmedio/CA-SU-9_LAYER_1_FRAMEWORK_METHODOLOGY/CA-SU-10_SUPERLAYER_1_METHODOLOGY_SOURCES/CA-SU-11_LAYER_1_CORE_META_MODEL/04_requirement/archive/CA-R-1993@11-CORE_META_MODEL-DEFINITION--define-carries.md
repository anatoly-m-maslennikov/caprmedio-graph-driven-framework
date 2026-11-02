---
atom_id: CA-R-1993@11
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Relation/Type: CARRIES'
  depends_on:
  - Subject/Graph Node/Carrier
  - Subject/Graph Node
  - Subject/Graph Relation
relations:
  child_of:
  - CA-R-1174
version: 11
updated_at: 2026-10-27 06:04:45 +0400
tier: 1
type: Definition
---
# Summary

Define CARRIES

## Scope

Carrier bindings of non-ephemeral Entities.

## Claim

CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.

## Details

IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity to its Carrier. The Entity/Carrier binding exposes this inverse direction; it is not a separately authored primitive Relation fact. This preserves the existing meaning defined by CA-D-257. Neither direction requires a separately registered binding for each YAML field or Markdown section, a new Carrier, a snapshot or a historical record. The applicable D policy specifies how the represented Entity is bound and represented. No additional endpoint class, graph ownership, cardinality or inference permission is introduced by moving this definition to R.
