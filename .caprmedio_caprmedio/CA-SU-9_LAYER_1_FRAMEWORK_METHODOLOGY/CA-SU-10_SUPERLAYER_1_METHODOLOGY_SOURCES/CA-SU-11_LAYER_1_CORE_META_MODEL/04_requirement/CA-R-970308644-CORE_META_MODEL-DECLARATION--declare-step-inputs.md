---
atom_id: CA-R-970308644
ref_id: CA-R-970308644
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step.Inputs
tier: 3
status: Active
version: 2
updated_at: '2026-11-11 16:04:42 +0400'
carrier_destination:
  file:
    name: CA-R-970308644-CORE_META_MODEL-DECLARATION--declare-step-inputs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Step.Inputs

## Claim

### Prose Claim

Step Inputs are optional. They identify the input values used by the Step; bindings supply values.

### Formal Claim

```CFEL
# model
Step.Inputs ((IS_PROPERTY_OF)) Step;
```
