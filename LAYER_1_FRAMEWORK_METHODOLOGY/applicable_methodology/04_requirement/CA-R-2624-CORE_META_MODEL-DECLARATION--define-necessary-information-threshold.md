---
atom_id: CA-R-2624
ref_id: CA-R-2624
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence.Necessary Information Threshold
tier: 3
status: Active
version: 3
updated_at: 2026-11-04 09:36:36 +0400
carrier_destination:
  file:
    name: CA-R-2624-CORE_META_MODEL-DECLARATION--define-necessary-information-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2624-CORE_META_MODEL-DECLARATION--define-necessary-information-threshold.md
  source_atom_id: CA-R-2624
  source_atom_revision: 3
  source_sha256: 594f6cc8a89a360f7bd61a554ba91b1e1dca7680d910ba90517e04d593380c2f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Define Necessary Information Threshold

## Claim

### Prose Claim


A present threshold value is an integer-percentage override. An absent override uses the governed default.

### Formal Claim

```CFEL
# model
Project.Settings.Confidence.Necessary Information Threshold:: {::0..1};

Project.Settings.Confidence.Necessary Information Threshold.*[]{::0}
```

