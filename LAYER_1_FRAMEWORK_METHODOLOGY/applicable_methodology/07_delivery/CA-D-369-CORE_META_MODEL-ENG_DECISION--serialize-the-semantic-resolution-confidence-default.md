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
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-369-CORE_META_MODEL-ENG_DECISION--serialize-the-semantic-resolution-confidence-default.md
  source_atom_id: CA-D-369
  source_atom_revision: 29
  source_sha256: a66142395497c30bf07a7113ba67c6091c67b5ca166a114be4b931cfb857cd21
  original_relations_sha256: c126554c6620d4d2e8da667cb2f65c2c9e2c5a0c53b0a9e77a8b3a2112416a03
---
## Summary

Serialize the semantic-resolution confidence default

## Claim

### Prose Claim


an explicit semantic-resolution confidence default in the Project's existing `caprmedio_framework_settings.toml` Carrier.


an explicit semantic-resolution confidence default **in** the Project's existing `caprmedio_framework_settings.toml` Carrier **must** use the integer-percentage field `confidence.semantic_resolution_threshold_percent`.
