---
atom_id: CA-D-505
ref_id: CA-D-505
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CARRIES
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-505-CORE_META_MODEL-DECISION--define-the-entity-carrier-binding.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-505-CORE_META_MODEL-ENG_DECISION--define-the-entity-carrier-binding.md
  source_atom_id: CA-D-505
  source_atom_revision: 18
  source_sha256: 8087175fb475a40a3bc57a9fc146e410917097347393f11ec4cd7403a8775343
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define the Entity Carrier binding

## Claim

### Prose Claim


Carrier bindings of Entities.


the Carrier Property of an Entity **means** its binding **to** the Carrier that stores **or** represents it.

## Details

- write this Property as `(Entity).Carrier`, using the actual Entity path, such as `Atom.Carrier` **or** `Scope Unit.Carrier`.
- the binding follows IS_CARRIED_BY.
- the Property refers **to** a Carrier; the referenced Carrier remains a Primary Entity.
