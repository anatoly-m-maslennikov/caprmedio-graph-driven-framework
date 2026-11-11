---
atom_id: CA-D-505
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//CARRIES
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Term//Property
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
relations: {}
tier: 1
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-505-CORE_META_MODEL-ENG_DECISION--define-the-entity-carrier-binding.md
  source_atom_id: CA-D-505
  source_atom_revision: 18
  source_sha256: aa95b938899bc6d83a0473e0ac6696c977cfb969fdceaa92d0e9f5b05bd80f2f
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
