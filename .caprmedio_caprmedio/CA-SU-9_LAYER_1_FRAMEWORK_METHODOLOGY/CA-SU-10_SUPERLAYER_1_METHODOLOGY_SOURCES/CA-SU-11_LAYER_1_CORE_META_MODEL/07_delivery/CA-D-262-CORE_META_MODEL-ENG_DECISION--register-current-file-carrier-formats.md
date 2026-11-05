---
atom_id: CA-D-262
ref_id: CA-D-262
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 3
status: Active
version: 28
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-262-CORE_META_MODEL-DECISION--register-current-file-carrier-formats.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary
Register Current File Carrier Formats

## Claim

### Prose Claim

registration of File Carrier Formats.


the Core Meta-Model **must** permit registered File Carrier Formats including Markdown, TOML, YAML, **and** JSON while Extensions **and** Project Configuration **may** register additional Carrier Formats.
