---
atom_id: CA-D-505@5
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 5
updated_at: 2026-10-24 00:38:25 +0400
author: Anatoly Maslennikov
subjects:
  governs: Entity Carrier Binding
  depends_on:
  - Entity
  - Property
  - Subject/Engineering/Carrier
  - Primary Entity
  - Atom Carrier Binding
  - Scope Unit Carrier Binding
  - IS_CARRIED_BY
relations: {}
tier: 1
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
