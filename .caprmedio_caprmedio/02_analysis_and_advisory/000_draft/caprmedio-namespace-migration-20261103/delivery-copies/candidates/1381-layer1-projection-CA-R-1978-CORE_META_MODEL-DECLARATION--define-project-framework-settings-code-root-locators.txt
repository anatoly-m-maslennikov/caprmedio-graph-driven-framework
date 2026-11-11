---
atom_id: CA-R-1978
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Code-Root Locators
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1978-CORE_META_MODEL-DECLARATION--define-project-framework-settings-code-root-locators.md
  source_atom_id: CA-R-1978
  source_atom_revision: 15
  source_sha256: d89ab4a49afc2763ebc5394e7b6d630b7cc5628637991874064ab2919c2708c5
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Code-Root Locators

## Claim scope

the code-root references in the Project's Framework Settings.

## Claim

```CFEL
Project.Settings.Code-Root Locators{:0..1}: [string]{:1+};
Project.Settings.Code-Root Locators.*[]{:0}
```

## Details

Evidence: CA-D-371 requires code-root locators in Framework Settings. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no discovery procedure, new root or locator count.
