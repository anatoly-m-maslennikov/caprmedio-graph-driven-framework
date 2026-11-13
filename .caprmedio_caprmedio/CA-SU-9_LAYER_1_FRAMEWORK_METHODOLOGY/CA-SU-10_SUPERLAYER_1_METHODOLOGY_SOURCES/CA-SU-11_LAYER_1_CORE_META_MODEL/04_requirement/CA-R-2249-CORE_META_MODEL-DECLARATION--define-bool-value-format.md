---
atom_id: CA-R-2249
ref_id: CA-R-2249
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: active
version: 8
updated_at: '2026-11-13T05:16:13.736930+00:00'
carrier_destination:
  file:
    name: CA-R-2249-CORE_META_MODEL-DECLARATION--define-bool-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define bool Value Format

## Claim

### Prose Claim


The bool Value Format admits the Boolean values true and false. It does not set a
property's cardinality, default, nullability, or carrier representation.



### Formal Claim

```python
# model
composition(container='CFEL', parts=('Format/bool',))
relation(source='Format/bool', name='NARROWER_THAN', target='Format')
```

## Semantics

bool is the value domain selected by a `[bool]` annotation on one direct
Property value.
