---
atom_id: CA-R-2625
ref_id: CA-R-2625@3
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Semantic Resolution
    Threshold
tier: 3
status: archived
version: 3
updated_at: 2026-11-04 09:36:36 +0400
carrier_destination:
  file:
    name: CA-R-2625@3-CORE_META_MODEL-DECLARATION--define-semantic-resolution-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
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

