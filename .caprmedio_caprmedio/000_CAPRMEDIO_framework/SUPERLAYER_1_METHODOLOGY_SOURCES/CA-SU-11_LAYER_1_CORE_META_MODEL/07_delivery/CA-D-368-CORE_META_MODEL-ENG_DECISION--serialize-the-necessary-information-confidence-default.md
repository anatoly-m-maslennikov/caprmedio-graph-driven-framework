---
atom_id: CA-D-368
ref_id: CA-D-368
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Necessary Information Threshold
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
  - CAPRMEDIO_MODEL <+ Carrier
tier: 6
relations:
  child_of:
  - CA-D-361
status: Active
version: 30
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-D-368-CORE_META_MODEL-DECISION--serialize-the-necessary-information-confidence-default.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize the necessary-information confidence default

## Claim

### Prose Claim


an explicit necessary-information confidence default in the Project's existing `caprmedio_framework_settings.toml` Carrier.


an explicit necessary-information confidence default **in** the Project's existing `caprmedio_framework_settings.toml` Carrier **must** use the integer-percentage field `confidence.necessary_information_threshold_percent`.
