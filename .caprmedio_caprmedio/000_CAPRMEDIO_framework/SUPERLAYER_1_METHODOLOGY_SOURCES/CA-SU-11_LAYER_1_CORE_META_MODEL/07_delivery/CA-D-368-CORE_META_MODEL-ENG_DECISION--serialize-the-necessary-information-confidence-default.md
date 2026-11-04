---
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Necessary Information Threshold
  passive:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - CAPRMEDIO_MODEL <+ Carrier
version: 30
updated_at: 2026-11-04 09:30:21 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-368
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-368-CORE_META_MODEL-ENG_DECISION--serialize-the-necessary-information-confidence-default.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Serialize the necessary-information confidence default

## Claim

### Prose Claim


an explicit necessary-information confidence default in the Project's existing `caprmedio_framework_settings.toml` Carrier.


an explicit necessary-information confidence default **in** the Project's existing `caprmedio_framework_settings.toml` Carrier **must** use the integer-percentage field `confidence.necessary_information_threshold_percent`.
