---
atom_id: CA-R-2767
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_SPECIALIZED_BY
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
version: 2
updated_at: 2026-11-04 19:46:41 +0400
carrier_destination:
  file:
    name: CA-R-2767-CORE_META_MODEL-DECLARATION--declare-is-specialized-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2767-CORE_META_MODEL-DECLARATION--declare-is-specialized-by.md
  source_atom_id: CA-R-2767
  source_atom_revision: 2
  source_sha256: 023fa028948d0bbc9e0c6351e290027bce7c51075ef7f3a187c0c3da7d80ae33
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---

## Summary

Declare IS_SPECIALIZED_BY

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_SPECIALIZED_BY <((HAS_INVERSE)) Relation//SPECIALIZES;

Relation//IS_SPECIALIZED_BY ((HAS_CLASSIFICATION)) Derivation == Derived;

# instances
Atom//$parent ((IS_SPECIALIZED_BY)) Atom//$child
```

## Semantics

IS_SPECIALIZED_BY relates an Atom to an Atom whose Claim specializes its Claim.
