---
atom_id: CA-R-2771
ref_id: CA-R-2771@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: archived
version: 2
updated_at: 2026-11-04 20:33:16 +0400
carrier_destination:
  file:
    name: CA-R-2771@2-CORE_META_MODEL-RULE--cfel-numeric-range-constraint.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

CFEL numeric range constraint

## Claim

### Prose Claim

Inside a square-bracket value Format annotation, `lower..upper` is a closed numeric interval: both endpoints are included. It constrains each direct Property value and does not state Property occurrence or value cardinality. This square-bracket value constraint is distinct from the existing curly-brace cardinality range `{:n..m}`.
### Formal Claim

```CFEL
# model
p:: [0..100]{:value count}
```

