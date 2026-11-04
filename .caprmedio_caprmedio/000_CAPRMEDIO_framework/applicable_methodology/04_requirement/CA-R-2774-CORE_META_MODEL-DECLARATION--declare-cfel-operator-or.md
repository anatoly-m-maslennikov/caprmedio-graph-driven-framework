---
atom_id: CA-R-2774
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Operator//Disjunction
version: 2
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 20:33:17 +0400
carrier_destination:
  file:
    name: CA-R-2774-CORE_META_MODEL-DECLARATION--declare-cfel-operator-or.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2774-CORE_META_MODEL-DECLARATION--declare-cfel-operator-or.md
  source_atom_id: CA-R-2774
  source_atom_revision: 2
  source_sha256: ba6201d96f4e360c018d10ceca4f0200bfd44c7cca22691cfa3026a6fb54fad4
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Declare CFEL operator OR

## Claim

### Formal Claim

```CFEL
# model
Operator//Disjunction == "OR"
```

## Semantics

At least one Boolean operand must be true. Parenthesize mixed AND/OR expressions to make grouping explicit.
