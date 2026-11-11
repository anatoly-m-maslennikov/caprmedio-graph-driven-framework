---
atom_id: CA-R-2250
ref_id: CA-R-2250@6
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/int
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: Archived
version: 6
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2250@6-CORE_META_MODEL-ENTITY_DEFINITION--define-int-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define int Value Format

## Claim

### Prose Claim


The int Value Format admits integer numeric values with no fractional part. It
does not set a numeric range, cardinality, uniqueness rule, or carrier
representation.



### Formal Claim

```CFEL
# model
CFEL <+ Format/int
```

## Semantics

int is the value domain selected by an `[int]` annotation on one direct
Property value.
