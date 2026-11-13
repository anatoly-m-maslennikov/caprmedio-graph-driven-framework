---
atom_id: CA-R-3063
ref_id: CA-R-3063@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step.Fixed Parameters
tier: 3
status: archived
version: 2
updated_at: 2026-11-11 16:04:42 +0400
carrier_destination:
  file:
    name: CA-R-3063@2-CORE_META_MODEL-DECLARATION--declare-step-fixed-parameters.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Step.Fixed Parameters

## Claim

### Prose Claim

A Step may declare fixed parameter values for its invocation. A fixed value is one permitted source of a binding.

### Formal Claim

```CFEL
# model
Step.Fixed Parameters ((IS_PROPERTY_OF)) Step;
```
