---
atom_id: CA-R-2327
ref_id: CA-R-2327
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Cardinality
tier: 1
status: active
version: 7
updated_at: '2026-11-13T06:26:02.151784+00:00'
carrier_destination:
  file:
    name: CA-R-2327-CORE_META_MODEL-DECLARATION--define-cardinality.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Cardinality

## Claim

### Prose Claim


Cardinality is CFEL syntax for expressing the allowed number of direct values,
dependent Properties, Relation instances or contained parts.



The forms are `{:n}`, `{:n+}` and `{:n..m}` with non-negative integer bounds.

### Formal Claim

```python
# model
composition(container='CFEL', parts=('Cardinality',))
```

