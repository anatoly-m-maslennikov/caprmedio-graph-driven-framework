---
atom_id: CA-R-2625
ref_id: CA-R-2625
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Semantic Resolution Threshold
version: 3
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 09:36:36 +0400
carrier_destination:
  file:
    name: CA-R-2625-CORE_META_MODEL-DECLARATION--define-semantic-resolution-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---

## Summary

Define Semantic Resolution Threshold

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.Confidence.Semantic Resolution Threshold:: {::0..1};

Project.Settings.Confidence.Semantic Resolution Threshold.*[]{::0}
```

### Prose Claim


A present threshold value is an integer-percentage override. An absent override uses the governed default.

