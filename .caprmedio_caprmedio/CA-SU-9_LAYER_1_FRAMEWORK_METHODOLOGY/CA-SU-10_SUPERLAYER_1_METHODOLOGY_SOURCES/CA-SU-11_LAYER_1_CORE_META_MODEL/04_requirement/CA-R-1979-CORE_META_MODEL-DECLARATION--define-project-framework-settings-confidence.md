---
atom_id: CA-R-1979
ref_id: CA-R-1979
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Confidence
relations:
  child_of:
  - CA-R-1176
version: 16
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1979-CORE_META_MODEL-DECLARATION--define-project-framework-settings-confidence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Project.Framework Settings.Confidence

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.Confidence{::0..1}:: []{::0};

Project.Settings.Confidence.*[in (Necessary Information Threshold, Semantic Resolution Threshold)]{::0..2};

Project.Settings.Confidence.*:: [int]
```

### Prose Claim


the Confidence grouping in the Project's Framework Settings.



## Details

Evidence: CA-R-1652 defines the necessary-information threshold default; CA-R-380 defines the semantic-resolution threshold default. These define the child settings, not the parent grouping. Candidate #6 decision 8 retains Settings as the default source, and decision 18 distinguishes Project settings from the framework's name. This grouping adds no threshold, override layer or mandatory value. Concrete CAPRMEDIO setting definitions belong in Project Configuration.
