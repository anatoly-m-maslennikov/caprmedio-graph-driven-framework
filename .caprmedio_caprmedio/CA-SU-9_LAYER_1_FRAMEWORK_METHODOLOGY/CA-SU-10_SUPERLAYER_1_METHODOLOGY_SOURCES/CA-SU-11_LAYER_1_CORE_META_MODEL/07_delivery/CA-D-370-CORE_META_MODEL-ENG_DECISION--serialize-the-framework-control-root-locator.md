---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Framework Control-Root Locator
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Carrier/Directory
version: 27
updated_at: 2026-11-04 09:30:21 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-370
ref_id: CA-D-370
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-370-CORE_META_MODEL-DECISION--serialize-the-framework-control-root-locator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
container:
  scope_unit: CA-SU-11
---
## Summary

Serialize the framework control-root locator

## Claim

### Prose Claim


an explicitly selected framework control-root locator in the Project's Framework Settings TOML Carrier.


when the framework control-root locator is explicitly selected, the Framework Settings TOML Carrier **must** encode it and it **must** resolve **to** the Directory Carrier prescribed by CA-D-317 **without** selecting a different authority root.
