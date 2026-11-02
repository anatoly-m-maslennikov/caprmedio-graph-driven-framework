---
atom_id: CA-D-505@10
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 10
updated_at: 2026-10-24 10:48:25 +0400
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph/Relation/Type: CARRIES'
  depends_on:
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Carrier
  - IS_CARRIED_BY
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
