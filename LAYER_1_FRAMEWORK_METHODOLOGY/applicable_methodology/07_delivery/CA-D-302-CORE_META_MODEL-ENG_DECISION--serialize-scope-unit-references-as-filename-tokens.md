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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-302-CORE_META_MODEL-ENG_DECISION--serialize-scope-unit-references-as-filename-tokens.md
  source_atom_id: CA-D-302
  source_atom_revision: 29
  source_sha256: a9db14879e0e85260e7f6417efc80296755364794eefceeca6ff7feac656cd51
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary
Serialize Scope Unit References as Filename Tokens

## Claim

### Prose Claim

Scope Unit references serialized **in** Atom filenames.


**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.
