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
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-368-CORE_META_MODEL-ENG_DECISION--serialize-the-necessary-information-confidence-default.md
  source_atom_id: CA-D-368
  source_atom_revision: 30
  source_sha256: 6998e8781c7dd054277c0165ce00d2aa6c4eccc3691fb1e6f1a64a4648e9bd14
  original_relations_sha256: c126554c6620d4d2e8da667cb2f65c2c9e2c5a0c53b0a9e77a8b3a2112416a03
---
## Summary

Serialize the necessary-information confidence default

## Claim

### Prose Claim


an explicit necessary-information confidence default in the Project's existing `caprmedio_framework_settings.toml` Carrier.


an explicit necessary-information confidence default **in** the Project's existing `caprmedio_framework_settings.toml` Carrier **must** use the integer-percentage field `confidence.necessary_information_threshold_percent`.
