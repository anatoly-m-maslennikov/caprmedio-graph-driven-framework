---
atom_id: CA-R-2625
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Semantic Resolution Threshold
version: 3
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 09:36:36 +0400
carrier_destination:
  file:
    name: CA-R-2625-CORE_META_MODEL-DECLARATION--define-semantic-resolution-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2625-CORE_META_MODEL-DECLARATION--define-semantic-resolution-threshold.md
  source_atom_id: CA-R-2625
  source_atom_revision: 3
  source_sha256: 4f1b15e5987e74114dafe7533030b130471d694e8dd8d319e63b187913a8e66d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Define Semantic Resolution Threshold

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.Confidence.Semantic Resolution Threshold: {:0..1};

Project.Settings.Confidence.Semantic Resolution Threshold.*[]{:0}
```

### Prose Claim


A present threshold value is an integer-percentage override. An absent override uses the governed default.

