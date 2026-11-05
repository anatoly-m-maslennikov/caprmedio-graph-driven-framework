---
atom_id: CA-R-2762
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_BLOCKED_BY
version: 3
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
updated_at: 2026-11-05 18:23:39 +0400
carrier_destination:
  file:
    name: CA-R-2762@3-draft-CORE_META_MODEL-DECLARATION--declare-is-blocked-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare IS_BLOCKED_BY

## Claim

### Formal Claim

```CFEL
# model
Relation//BLOCKS ((IS_INVERSE_ALIAS_FOR)) Relation//IS_BLOCKED_BY;

Relation//IS_BLOCKED_BY ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$dependent[<Atom>, (.Header.Role = Plan)] ((IS_BLOCKED_BY)) $prerequisite[<Atom>, (.Header.Role = Plan)]
```

### Prose Claim

A dependent Plan may start only after each Plan it is blocked by is Done. BLOCKS is the inverse alias: the prerequisite is written before the dependent.

## Semantics

IS_BLOCKED_BY relates a dependent Plan to a prerequisite Plan.
