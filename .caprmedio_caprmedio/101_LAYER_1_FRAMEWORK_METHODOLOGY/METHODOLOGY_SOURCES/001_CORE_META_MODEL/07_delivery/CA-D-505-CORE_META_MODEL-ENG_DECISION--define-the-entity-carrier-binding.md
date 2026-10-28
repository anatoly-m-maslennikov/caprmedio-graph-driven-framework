---
atom_id: CA-D-505
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 14
updated_at: 2026-10-27 19:59:26 +0400
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: CARRIES'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Relation
relations: {}
tier: 1
type: Eng Decision
---
# Summary

Define the Entity Carrier binding

## Scope

Carrier bindings of Entities.

## Claim

the Carrier Property of an Entity **means** its binding **to** the Carrier that stores **or** represents it.

## Details

- write this Property as `(Entity)/Carrier`, using the actual Entity path, such as `Atom/Carrier` **or** `Scope Unit/Carrier`.
- the binding follows IS_CARRIED_BY.
- the Property refers **to** a Carrier; the referenced Carrier remains a Primary Entity.
