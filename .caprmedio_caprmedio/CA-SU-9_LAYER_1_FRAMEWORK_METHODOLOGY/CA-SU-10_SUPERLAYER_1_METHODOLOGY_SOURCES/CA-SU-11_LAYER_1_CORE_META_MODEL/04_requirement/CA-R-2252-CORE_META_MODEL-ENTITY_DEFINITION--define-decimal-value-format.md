---
atom_id: CA-R-2252
ref_id: CA-R-2252
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/decimal
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: Active
version: 7
updated_at: '2026-11-11 16:04:42 +0400'
carrier_destination:
  file:
    name: CA-R-2252-CORE_META_MODEL-DECLARATION--define-decimal-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define decimal Value Format

## Claim

### Prose Claim


The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.



### Formal Claim

```CFEL
# model
CFEL <+ Format/decimal;

Format/decimal ((NARROWER_THAN)) Format;
```

## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
Property value.
