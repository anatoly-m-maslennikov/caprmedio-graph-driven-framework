---
atom_id: CA-R-2772
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 2
updated_at: 2026-11-04 20:33:17 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2772-CORE_META_MODEL-RULE--cfel-format-constraint-intersection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2772-CORE_META_MODEL-RULE--cfel-format-constraint-intersection.md
  source_atom_id: CA-R-2772
  source_atom_revision: 2
  source_sha256: ede1863121a6b8b03095bcf71bd74e448e68c1d2e3636cb6a8b968d28ed1abd2
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

CFEL Format constraint intersection

## Claim

### Formal Claim

```CFEL
# model
p: [int, 0..100]{:value count}
```

### Prose Claim

A comma inside one square-bracket value Format annotation combines constraints by intersection. Each direct value must satisfy every listed constraint. Thus `[int, 0..100]` admits integer values from 0 through 100 inclusive. An empty or incompatible intersection admits no values. Existing curly-brace occurrence and value-cardinality annotations keep their current meanings and remain independent.
