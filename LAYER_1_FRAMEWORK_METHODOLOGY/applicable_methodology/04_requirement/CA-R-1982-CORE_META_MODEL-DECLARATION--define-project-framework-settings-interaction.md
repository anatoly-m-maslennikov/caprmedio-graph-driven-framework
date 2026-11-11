---
atom_id: CA-R-1982
ref_id: CA-R-1982
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Interaction
tier: 3
relations:
  child_of:
  - CA-R-1176
status: Active
version: 15
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1982-CORE_META_MODEL-DECLARATION--define-project-framework-settings-interaction.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1982-CORE_META_MODEL-DECLARATION--define-project-framework-settings-interaction.md
  source_atom_id: CA-R-1982
  source_atom_revision: 15
  source_sha256: 2b3ee397067640a764fbcc8ab330365405cd4c0e7c3062695fb1ab02614a19c3
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Interaction

## Claim

### Prose Claim


the Interaction grouping in the Project's Framework Settings.



### Formal Claim

```CFEL
# model
Project.Settings.Interaction{::0..1}:: []{::0};

Project.Settings.Interaction.*[in (Reporting Mode)]{::1}
```

## Details

Evidence: CA-R-1628 defines reporting-mode values; CA-R-1439 limits effects to presentation; CA-R-1440 preserves mandatory information. These define the child setting and its constraints, not the parent grouping. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This grouping adds no authorization, workflow, validation or safety behavior.
