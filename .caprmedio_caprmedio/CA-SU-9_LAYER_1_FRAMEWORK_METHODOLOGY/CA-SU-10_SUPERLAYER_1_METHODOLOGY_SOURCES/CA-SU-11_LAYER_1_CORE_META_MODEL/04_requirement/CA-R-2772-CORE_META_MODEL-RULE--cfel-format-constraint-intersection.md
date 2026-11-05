---
atom_id: CA-R-2772
ref_id: CA-R-2772
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 2
updated_at: 2026-11-04 20:33:17 +0400
tier: 1
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2772-RULE--cfel-format-constraint-intersection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

CFEL Format constraint intersection

## Claim

### Formal Claim

```CFEL
# model
p:: [int, 0..100]{:value count}
```

### Prose Claim

A comma inside one square-bracket value Format annotation combines constraints by intersection. Each direct value must satisfy every listed constraint. Thus `[int, 0..100]` admits integer values from 0 through 100 inclusive. An empty or incompatible intersection admits no values. Existing curly-brace occurrence and value-cardinality annotations keep their current meanings and remain independent.
