---
atom_id: CA-R-1609
ref_id: CA-R-1609
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 22
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1609-CORE_META_MODEL-RULE--distinguish-projected-representations-from-represented-entities.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1609-CORE_META_MODEL-RULE--distinguish-projected-representations-from-represented-entities.md
  source_atom_id: CA-R-1609
  source_atom_revision: 22
  source_sha256: 4b29bf7b5938f6f359086a6aa1a9b0a7ab30d0ae3e4354e45b336a676d439a52
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Distinguish projected representations from represented Entities

## Claim

### Prose Claim


Representations inside a Projection and the Entities they represent.


a representation inside a Projection **must** remain distinct from the Entity it represents.

- depicting an existing Artifact **or** Scope Unit does **not** create another authoritative Artifact **or** Scope Unit.
- a representation **may** identify a source Entity **or** a derived element admitted by the Projection specification; source identities **and** traceability remain governed by CA-R-2535.
- this boundary introduces no separate Projection Element Term, lifecycle, **or** independently maintained authority.
