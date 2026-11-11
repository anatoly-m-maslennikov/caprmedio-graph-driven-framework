---
atom_id: CA-R-2251
ref_id: CA-R-2251@6
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/float
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: Archived
version: 6
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2251@6-CORE_META_MODEL-ENTITY_DEFINITION--define-float-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define float Value Format

## Claim

### Prose Claim


The float Value Format admits floating-point numeric values. It does not set
precision, a numeric range, cardinality, uniqueness, or carrier
representation.



### Formal Claim

```CFEL
# model
CFEL <+ Format/float
```

## Semantics

float is the value domain selected by a `[float]` annotation on one direct
Property value.
