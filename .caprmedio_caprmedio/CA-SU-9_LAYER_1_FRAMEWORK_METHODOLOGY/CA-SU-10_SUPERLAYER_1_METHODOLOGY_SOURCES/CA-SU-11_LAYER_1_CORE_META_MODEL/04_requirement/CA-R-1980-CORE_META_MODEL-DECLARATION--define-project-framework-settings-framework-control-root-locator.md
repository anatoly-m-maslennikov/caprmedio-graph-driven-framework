---
atom_id: CA-R-1980
ref_id: CA-R-1980
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Framework Control-Root Locator
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
    name: CA-R-1980-CORE_META_MODEL-DECLARATION--define-project-framework-settings-framework-control-root-locator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Project.Framework Settings.Framework Control-Root Locator

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.Framework Control-Root Locator:: [string]{::0..1};

Project.Settings.Framework Control-Root Locator.*[]{::0}
```

### Prose Claim


the Project's framework control-root reference in Framework Settings.



## Details

Evidence: CA-D-370 requires the locator to resolve to the Directory Carrier prescribed by CA-D-317 without selecting another authority root. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no path or alternative authority root; those remain Delivery rules.
