---
atom_id: CA-R-2771
ref_id: CA-R-2771
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: active
version: 3
updated_at: '2026-11-13T05:35:43.598645+00:00'
carrier_destination:
  file:
    name: CA-R-2771-CORE_META_MODEL-RULE--cfel-numeric-range-constraint.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

CFEL numeric range constraint

## Claim

### Prose Claim

Inside a square-bracket value Format annotation, `lower..upper` is a closed numeric interval: both endpoints are included. It constrains each direct Property value and does not state Property occurrence or value cardinality. This square-bracket value constraint is distinct from the existing curly-brace cardinality range `{:n..m}`.

## Details

```text
p:: [0..100]{:value count}
```
