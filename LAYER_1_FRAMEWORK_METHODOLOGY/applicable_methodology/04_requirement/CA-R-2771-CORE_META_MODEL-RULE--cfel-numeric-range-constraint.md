---
atom_id: CA-R-2771
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 2
updated_at: 2026-11-04 20:33:16 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2771-CORE_META_MODEL-RULE--cfel-numeric-range-constraint.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2771-CORE_META_MODEL-RULE--cfel-numeric-range-constraint.md
  source_atom_id: CA-R-2771
  source_atom_revision: 2
  source_sha256: f4381a01fd67e8b87a221c3467f3b87253332ae0713420ed3f10b1c454450382
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

CFEL numeric range constraint

## Claim

### Formal Claim

```CFEL
# model
p: [0..100]{:value count}
```

### Prose Claim

Inside a square-bracket value Format annotation, `lower..upper` is a closed numeric interval: both endpoints are included. It constrains each direct Property value and does not state Property occurrence or value cardinality. This square-bracket value constraint is distinct from the existing curly-brace cardinality range `{:n..m}`.
