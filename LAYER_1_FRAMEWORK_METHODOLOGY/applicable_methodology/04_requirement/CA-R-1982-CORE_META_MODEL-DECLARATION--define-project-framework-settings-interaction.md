---
atom_id: CA-R-1982
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Interaction
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1982-CORE_META_MODEL-DECLARATION--define-project-framework-settings-interaction.md
  source_atom_id: CA-R-1982
  source_atom_revision: 15
  source_sha256: 3b305c65aef7264316459a239842827003d44a81ef87866ad44c1ab81ef29c47
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Interaction

## Claim scope

the Interaction grouping in the Project's Framework Settings.

## Claim

```CFEL
Project.Settings.Interaction{:0..1}: []{:0};
Project.Settings.Interaction.*[in (Reporting Mode)]{:1}
```

## Details

Evidence: CA-R-1628 defines reporting-mode values; CA-R-1439 limits effects to presentation; CA-R-1440 preserves mandatory information. These define the child setting and its constraints, not the parent grouping. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This grouping adds no authorization, workflow, validation or safety behavior.
