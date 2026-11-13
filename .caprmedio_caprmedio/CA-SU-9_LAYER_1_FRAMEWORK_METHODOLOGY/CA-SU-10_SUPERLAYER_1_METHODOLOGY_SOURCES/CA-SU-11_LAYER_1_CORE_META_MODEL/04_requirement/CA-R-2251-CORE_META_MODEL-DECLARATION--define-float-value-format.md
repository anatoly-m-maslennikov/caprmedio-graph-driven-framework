---
atom_id: CA-R-2251
ref_id: CA-R-2251
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/float
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: active
version: 8
updated_at: '2026-11-13T05:16:19.063289+00:00'
carrier_destination:
  file:
    name: CA-R-2251-CORE_META_MODEL-DECLARATION--define-float-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
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

```python
# model
composition(container='CFEL', parts=('Format/float',))
relation(source='Format/float', name='NARROWER_THAN', target='Format')
```

## Semantics

float is the value domain selected by a `[float]` annotation on one direct
Property value.
