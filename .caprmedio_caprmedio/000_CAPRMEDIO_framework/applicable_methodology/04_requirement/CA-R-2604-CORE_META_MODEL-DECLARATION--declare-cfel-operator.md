---
atom_id: CA-R-2604
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL<+Operator//InstanceBinding
version: 3
updated_at: 2026-11-04 21:11:03 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2604-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2604-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
  source_atom_id: CA-R-2604
  source_atom_revision: 3
  source_sha256: f2b03e857aa8bc2e30beba8bac5f4b9b78d12af35061ab865d3c8e3ff07bdc5d
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---

## Summary

Declare CFEL operator $

## Claim

### Formal Claim

```CFEL
# model
Operator//InstanceBinding == "$"
```

## Semantics

Bind an existing selected instance or read its bound Property; it creates nothing. A variable introduced by a standalone typed instance selector such as `Kind//$x;` remains in scope for following statements in the same CFEL fenced block. A variable introduced in an IF condition is in scope within that condition and its matching THEN group only; it is not in scope in following statements. If an outer variable is already bound, a new binding inside IF must use a different variable name; references to the outer variable retain its existing identity.
