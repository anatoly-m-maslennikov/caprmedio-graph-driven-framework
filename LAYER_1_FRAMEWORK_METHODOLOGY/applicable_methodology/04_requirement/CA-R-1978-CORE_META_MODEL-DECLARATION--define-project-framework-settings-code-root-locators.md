---
atom_id: CA-R-1978
ref_id: CA-R-1978
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Code-Root Locators
tier: 3
relations:
  child_of:
  - CA-R-1176
status: Active
version: 15
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1978-CORE_META_MODEL-DECLARATION--define-project-framework-settings-code-root-locators.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1978-CORE_META_MODEL-DECLARATION--define-project-framework-settings-code-root-locators.md
  source_atom_id: CA-R-1978
  source_atom_revision: 15
  source_sha256: db8ff80f323b703b91ff58db59d51c504af43f051e67c41677763109046bc728
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Code-Root Locators

## Claim

### Prose Claim


the code-root references in the Project's Framework Settings.



### Formal Claim

```CFEL
# model
Project.Settings.Code-Root Locators{::0..1}:: [string]{::1+};

Project.Settings.Code-Root Locators.*[]{::0}
```

## Details

Evidence: CA-D-371 requires code-root locators in Framework Settings. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no discovery procedure, new root or locator count.
