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
