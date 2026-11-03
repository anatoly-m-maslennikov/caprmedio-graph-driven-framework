---
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Name
  passive:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom
version: 30
updated_at: 2026-11-02 19:46:47 +0400
relations:
  child_of:
  - CA-D-366
atom_id: CA-D-375
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 7
role: Delivery
form: Decision
---
## Summary

Serialize Project initialization identity

## Claim scope

the Operator-selected Project Name in the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact nonempty lowercase TOML string value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.

## Details

validation **must** preserve the selected value exactly; it **must not** trim **or** convert its case. the complete supported field signature is governed by CA-D-366.

### Current source provenance

Current source: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-375-CORE_META_MODEL-ENG_DECISION--serialize-project-initialization-identity.md`, CA-D-375@27, SHA-256 `d86d451d292b2af19c799152c03940cf96f3693edad8f90fbca028d47f55303f`.
