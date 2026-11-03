---
atom_id: CA-R-1979
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Confidence
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---
## Summary

Define Project.Framework Settings.Confidence

## Claim scope

the Confidence grouping in the Project's Framework Settings.

## Claim

```CFEL
Project.Settings.Confidence{:0..1}: []{:0};
Project.Settings.Confidence.*[in (Necessary Information Threshold, Semantic Resolution Threshold)]{:0..2}
```

## Details

Evidence: CA-R-1652 defines the necessary-information threshold default; CA-R-380 defines the semantic-resolution threshold default. These define the child settings, not the parent grouping. Candidate #6 decision 8 retains Settings as the default source, and decision 18 distinguishes Project settings from the framework's name. This grouping adds no threshold, override layer or mandatory value. Concrete CAPRMEDIO setting definitions belong in Project Configuration.
