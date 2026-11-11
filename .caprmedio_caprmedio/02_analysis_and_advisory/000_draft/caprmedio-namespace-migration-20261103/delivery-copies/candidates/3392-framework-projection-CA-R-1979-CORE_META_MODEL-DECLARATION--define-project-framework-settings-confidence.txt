---
atom_id: CA-R-1979
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Confidence
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1979-CORE_META_MODEL-DECLARATION--define-project-framework-settings-confidence.md
  source_atom_id: CA-R-1979
  source_atom_revision: 15
  source_sha256: 68d8dbbc7be8bf332eeebb1900852cf172521d63e80d5e9592d6859fe3c28779
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
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
