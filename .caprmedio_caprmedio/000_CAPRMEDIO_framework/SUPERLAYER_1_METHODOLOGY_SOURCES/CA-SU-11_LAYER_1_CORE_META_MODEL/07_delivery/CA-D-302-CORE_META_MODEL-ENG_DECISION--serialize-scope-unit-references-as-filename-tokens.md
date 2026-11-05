---
atom_id: CA-D-302
ref_id: CA-D-302
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.Name
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 3
status: Active
version: 29
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-302-CORE_META_MODEL-DECISION--serialize-scope-unit-references-as-filename-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary
Serialize Scope Unit References as Filename Tokens

## Claim

### Prose Claim

Scope Unit references serialized **in** Atom filenames.


**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.
