---
atom_id: "CA-D-505"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
global_tier: 9
status: "Active"
version: 3
updated_at: "2026-10-15 18:52:26 +0000"
author: "Anatoly Maslennikov"
subjects:
  governs: "Entity Carrier Binding"
  depends_on:
    ["Entity", "Property", "Entity/Carrier", "Primary Entity", "Atom Carrier Binding", "Scope Unit Carrier Binding", "IS_CARRIED_BY"]
relations: {}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-505-CORE_META_MODEL-CORE--define-the-entity-carrier-binding.md
  source_atom_id: CA-D-505
  source_atom_revision: 3
  source_sha256: 2241cbe68529223ed53ad19c3dee237841414fdad85cd721312e425715a9997f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
