---
atom_id: CA-R-1045
ref_id: CA-R-1045
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
tier: 2
relations:
  child_of:
  - CA-R-1044
status: Active
version: 27
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1045-CORE_META_MODEL-RULE--restrict-autonomous-confidence-threshold-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1045-CORE_META_MODEL-RULE--restrict-autonomous-confidence-threshold-values.md
  source_atom_id: CA-R-1045
  source_atom_revision: 27
  source_sha256: 3406a8e2de633a55983aa318b8e313d2b50d04a23c2861c2d67d0e9c8a345eeb
  original_relations_sha256: 6f0d7042bafec03f41aba93d9d29bcd1833719ec8a8174a03378838fd5da89fd
---
## Summary

Restrict Autonomous Confidence Threshold values

## Claim

### Prose Claim


Autonomous Confidence Threshold values.


**every** Autonomous Confidence Threshold **must** be an integer percentage **`>=0`** **and** **`<=100`**. resolve its effective value from the applicable source under CA-M-271; the methodology **must not** restrict that value **to** a closed list of preferred percentages.
