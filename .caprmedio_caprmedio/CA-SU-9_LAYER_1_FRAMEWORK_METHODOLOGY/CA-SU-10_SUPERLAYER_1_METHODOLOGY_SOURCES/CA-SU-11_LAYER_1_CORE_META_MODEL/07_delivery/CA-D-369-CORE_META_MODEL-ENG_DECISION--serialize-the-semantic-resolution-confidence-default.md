---
atom_id: CA-D-369
ref_id: CA-D-369
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Semantic Resolution Threshold
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
tier: 6
relations:
  child_of:
  - CA-D-361
status: Active
version: 29
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-D-369-CORE_META_MODEL-DECISION--serialize-the-semantic-resolution-confidence-default.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize the semantic-resolution confidence default

## Claim

### Prose Claim


an explicit semantic-resolution confidence default in the Project's existing `caprmedio_framework_settings.toml` Carrier.


an explicit semantic-resolution confidence default **in** the Project's existing `caprmedio_framework_settings.toml` Carrier **must** use the integer-percentage field `confidence.semantic_resolution_threshold_percent`.
