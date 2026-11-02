---
atom_id: CA-R-1993@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Relation//CARRIES
  depends_on:
  - Entity/Carrier
  - Entity
  - Entity/Graph Syntax > Relation
relations:
  child_of:
  - CA-R-1174
version: 16
updated_at: 2026-10-29 10:13:49 +0400
tier: 1
type: Relation Definition
---
## Summary
Define CARRIES

## Claim scope
Carrier bindings of non-ephemeral Entities.

## Claim

CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.

### Formal claim

```text
Entity/Graph Syntax > Relation//CARRIES
Entity/Graph Syntax > Relation//IS_CARRIED_BY
```

## Details

IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity to its Carrier. The Entity/Carrier binding exposes this inverse direction; it is not a separately authored primitive Relation fact. This preserves the existing meaning defined by CA-D-257. Neither direction requires a separately registered binding for each YAML field or Markdown section, a new Carrier, a snapshot or a historical record. The applicable D policy specifies how the represented Entity is bound and represented. No additional endpoint class, graph ownership, cardinality or inference permission is introduced by moving this definition to R.
