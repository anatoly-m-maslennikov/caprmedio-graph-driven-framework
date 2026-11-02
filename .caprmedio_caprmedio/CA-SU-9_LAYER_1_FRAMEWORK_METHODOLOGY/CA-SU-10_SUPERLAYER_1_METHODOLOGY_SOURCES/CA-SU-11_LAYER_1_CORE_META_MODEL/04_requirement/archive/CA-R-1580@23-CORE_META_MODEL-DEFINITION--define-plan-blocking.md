---
subjects:
  governs: Entity/Graph Syntax > Relation//BLOCKS
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Entity/Object/Continuant/Projection
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status: Done'
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Graph Syntax > Relation//DEPENDS_ON
version: 23
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1580@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Relation Definition
---
## Summary

Define Plan blocking

## Claim scope

Plan-blocking Relations in the Plan Graph.

## Claim

**in** the Plan Graph, `A BLOCKS B` **means** that Plan `B` may start only
after Plan `A` is Done. An inverse lookup is derived from the same explicit
fact and is not separately authored; Subject DEPENDS_ON remains distinct.

## Details

Plan endpoint admission, status, cardinality, authority and reachability belong
to the Plan Entity Definition CA-R-1338.
