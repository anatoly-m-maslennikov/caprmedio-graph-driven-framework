---
atom_id: CA-R-2762
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_BLOCKED_BY
version: 2
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
updated_at: 2026-11-04 16:52:59 +0400
carrier_destination:
  file:
    name: CA-R-2762-CORE_META_MODEL-DECLARATION--declare-is-blocked-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2762-CORE_META_MODEL-DECLARATION--declare-is-blocked-by.md
  source_atom_id: CA-R-2762
  source_atom_revision: 2
  source_sha256: 6620239782cc317abe88ee6d70794e60727a197cfbb9dc959327b7483283cbc9
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---

## Summary

Declare IS_BLOCKED_BY

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_BLOCKED_BY ((HAS_INVERSE)) Relation//BLOCKS;

Relation//IS_BLOCKED_BY ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: Plan)//$dependent ((IS_BLOCKED_BY)) Atom/(.Header.Role: Plan)//$prerequisite
```

### Prose Claim

A dependent Plan may start only after each Plan it is blocked by is Done.

## Semantics

IS_BLOCKED_BY relates a dependent Plan to a prerequisite Plan.
