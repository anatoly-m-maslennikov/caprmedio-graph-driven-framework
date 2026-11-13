---
atom_id: CA-R-2254
ref_id: CA-R-2254
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/datetime
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: active
version: 8
updated_at: '2026-11-13T05:16:34.014125+00:00'
carrier_destination:
  file:
    name: CA-R-2254-CORE_META_MODEL-DECLARATION--define-datetime-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define datetime Value Format

## Claim

### Prose Claim


The datetime Value Format admits date-and-time values. It does not set a
timezone convention, precision, cardinality, uniqueness, or carrier
representation.



### Formal Claim

```python
# model
composition(container='CFEL', parts=('Format/datetime',))
relation(source='Format/datetime', name='NARROWER_THAN', target='Format')
```

## Semantics

datetime is the value domain selected by a `[datetime]` annotation on one
direct Property value.
