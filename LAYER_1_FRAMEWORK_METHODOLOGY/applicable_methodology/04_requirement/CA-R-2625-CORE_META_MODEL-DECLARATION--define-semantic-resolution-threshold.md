---
atom_id: CA-R-2625
ref_id: CA-R-2625
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Semantic Resolution Threshold
tier: 3
status: Active
version: 3
updated_at: 2026-11-04 09:36:36 +0400
carrier_destination:
  file:
    name: CA-R-2625-CORE_META_MODEL-DECLARATION--define-semantic-resolution-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2625-CORE_META_MODEL-DECLARATION--define-semantic-resolution-threshold.md
  source_atom_id: CA-R-2625
  source_atom_revision: 3
  source_sha256: d1dee02df7981db20fbd18d940fe9989953884281155f5c7f7aedb90ff0a2e60
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Define Semantic Resolution Threshold

## Claim

### Prose Claim


A present threshold value is an integer-percentage override. An absent override uses the governed default.

### Formal Claim

```CFEL
# model
Project.Settings.Confidence.Semantic Resolution Threshold:: {::0..1};

Project.Settings.Confidence.Semantic Resolution Threshold.*[]{::0}
```

