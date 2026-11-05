---
atom_id: CA-D-376
ref_id: CA-D-376
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Prefix
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 7
relations:
  child_of:
  - CA-D-366
status: Active
version: 28
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-D-376-CORE_META_MODEL-DECISION--serialize-the-project-atom-prefix.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize the Project Atom prefix

## Claim

### Prose Claim


the Operator-selected Atom prefix in the Project Settings TOML Carrier.


the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix as its exact nonempty uppercase TOML string value under CA-D-378 **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.

## Details

validation **must** preserve the selected prefix exactly; it **must not** trim **or** automatically uppercase it. the complete supported field signature is governed by CA-D-366.
