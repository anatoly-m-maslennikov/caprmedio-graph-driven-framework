---
subjects:
  active: Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
version: 27
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1044
atom_id: CA-R-1045
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1045-CORE_META_MODEL-RULE--restrict-autonomous-confidence-threshold-values.md
  source_atom_id: CA-R-1045
  source_atom_revision: 27
  source_sha256: f5d870bb03d9e273e71808b444680740e78a1a63bf382c1d5fb30fcf534b094a
  original_relations_sha256: 6f0d7042bafec03f41aba93d9d29bcd1833719ec8a8174a03378838fd5da89fd
---
## Summary

Restrict Autonomous Confidence Threshold values

## Claim scope

Autonomous Confidence Threshold values.

## Claim

**every** Autonomous Confidence Threshold **must** be an integer percentage **`>=0`** **and** **`<=100`**. resolve its effective value from the applicable source under CA-M-271; the methodology **must not** restrict that value **to** a closed list of preferred percentages.
