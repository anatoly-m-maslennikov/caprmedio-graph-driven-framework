---
atom_id: CA-D-375
ref_id: CA-D-375
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Name
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom
tier: 7
relations:
  child_of:
  - CA-D-366
status: Active
version: 30
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-375-CORE_META_MODEL-DECISION--serialize-project-initialization-identity.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-375-CORE_META_MODEL-ENG_DECISION--serialize-project-initialization-identity.md
  source_atom_id: CA-D-375
  source_atom_revision: 30
  source_sha256: 5513db30bdb7b9694841f8fe267d1c671a0abef9272c9705a7d4fe2abcbc7ca3
  original_relations_sha256: 2a948e2a8ca98f226a4515239fa376af18890f07ccdd2ef7a0521257d70b6a6a
---
## Summary

Serialize Project initialization identity

## Claim

### Prose Claim


the Operator-selected Project Name in the Project Settings TOML Carrier.


the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details

validation **must** preserve the selected value exactly; it **must not** trim **or** convert its case. the complete supported field signature is governed by CA-D-366.

### Current source provenance

Current source: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-375-CORE_META_MODEL-ENG_DECISION--serialize-project-initialization-identity.md`, CA-D-375@27, SHA-256 `d86d451d292b2af19c799152c03940cf96f3693edad8f90fbca028d47f55303f`.
