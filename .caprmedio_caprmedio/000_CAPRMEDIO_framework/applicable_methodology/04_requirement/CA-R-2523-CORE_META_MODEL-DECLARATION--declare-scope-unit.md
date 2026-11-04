---
atom_id: CA-R-2523
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
version: 3
updated_at: 2026-11-04 11:00:07 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2523-CORE_META_MODEL-DECLARATION--declare-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2523-CORE_META_MODEL-DECLARATION--declare-scope-unit.md
  source_atom_id: CA-R-2523
  source_atom_revision: 3
  source_sha256: d5656fcb6fdc9497abac2f3e08b7d7fdda49af4300ea1cdbc3e3fe6d68ad48a5
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---

## Summary

Declare Scope Unit

## Claim

### Formal Claim

```CFEL
# model
Scope Unit >| (Container == yes);

Scope Unit ((NARROWER_THAN)) Continuant;

# instances
Scope Unit//$scope_unit {:0+}((CONTAINS)) Atom//$atom;

Scope Unit//$scope_unit{:0..1}((IS_CONTAINED_BY)) Scope Unit//$scope_unit_2;

Scope Unit//$scope_unit_3{:0+}((CONTAINS)) Scope Unit//$scope_unit_4;

IF (Scope Unit//$unit not in (Scope Unit/Project//$scope_unit_5))
THEN ($unit {==1}((IS_CONTAINED_BY)) Scope Unit//$scope_unit_6);
```

## Semantics

A Scope Unit defines a boundary of responsibility for Atoms.
