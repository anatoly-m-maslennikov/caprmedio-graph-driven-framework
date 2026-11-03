---
atom_id: CA-D-505
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: CFEL <+ Relation//CARRIES
  passive:
  - Entity
  - Term//Property
  - Carrier
  - CFEL <+ Relation
relations: {}
tier: 1
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-505-CORE_META_MODEL-ENG_DECISION--define-the-entity-carrier-binding.md
  source_atom_id: CA-D-505
  source_atom_revision: 18
  source_sha256: 69794815098f830ac31f40f9789426b5afe69e3abbf2068db4d4c2a90945ef3d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define the Entity Carrier binding

## Claim scope

Carrier bindings of Entities.

## Claim

the Carrier Property of an Entity **means** its binding **to** the Carrier that stores **or** represents it.

## Details

- write this Property as `(Entity).Carrier`, using the actual Entity path, such as `Atom.Carrier` **or** `Scope Unit.Carrier`.
- the binding follows IS_CARRIED_BY.
- the Property refers **to** a Carrier; the referenced Carrier remains a Primary Entity.
