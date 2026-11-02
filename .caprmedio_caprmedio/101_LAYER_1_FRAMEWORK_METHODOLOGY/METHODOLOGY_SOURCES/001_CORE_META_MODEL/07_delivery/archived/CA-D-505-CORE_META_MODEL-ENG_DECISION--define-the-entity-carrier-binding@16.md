---
atom_id: CA-D-505
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 16
updated_at: 2026-10-29 07:45:30 +0400
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Relation//CARRIES
  depends_on:
  - Entity
  - Entity/Object/Continuant/Term//Property
  - Entity/Carrier
  - Entity/Graph Syntax > Relation
relations: {}
tier: 1
type: Decision
---
## Summary

Define the Entity Carrier binding

## Claim scope

Carrier bindings of Entities.

## Claim

the Carrier Property of an Entity **means** its binding **to** the Carrier that stores **or** represents it.

## Details

- write this Property as `(Entity)/Carrier`, using the actual Entity path, such as `Atom/Carrier` **or** `Scope Unit/Carrier`.
- the binding follows IS_CARRIED_BY.
- the Property refers **to** a Carrier; the referenced Carrier remains a Primary Entity.
