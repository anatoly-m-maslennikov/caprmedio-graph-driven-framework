---
atom_id: CA-D-371
ref_id: CA-D-371
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Code-Root Locators
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
tier: 6
relations:
  child_of:
  - CA-D-361
status: Active
version: 25
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-D-371-CORE_META_MODEL-DECISION--serialize-framework-code-root-locators.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-371-CORE_META_MODEL-ENG_DECISION--serialize-framework-code-root-locators.md
  source_atom_id: CA-D-371
  source_atom_revision: 25
  source_sha256: d00ae4ce8570c10398fc73b2d93c67d77f34ba02e78ea7a06e3666b7ef6d17b8
  original_relations_sha256: c126554c6620d4d2e8da667cb2f65c2c9e2c5a0c53b0a9e77a8b3a2112416a03
---
## Summary

Serialize framework code-root locators

## Claim

### Prose Claim


explicitly selected code-root locators in the Project's Framework Settings TOML Carrier.


when code-root locators are explicitly selected, the Framework Settings TOML Carrier **must** encode their declared values for the Project.
