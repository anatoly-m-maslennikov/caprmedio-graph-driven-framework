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
