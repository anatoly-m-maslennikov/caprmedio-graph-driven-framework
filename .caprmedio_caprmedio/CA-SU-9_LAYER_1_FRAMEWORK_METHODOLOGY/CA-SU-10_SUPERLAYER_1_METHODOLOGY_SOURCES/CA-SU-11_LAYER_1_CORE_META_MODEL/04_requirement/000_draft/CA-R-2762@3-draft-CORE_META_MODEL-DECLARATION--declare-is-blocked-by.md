---
atom_id: CA-R-2762
ref_id: CA-R-2762@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_BLOCKED_BY
tier: 1
status: Draft
version: 3
updated_at: 2026-11-05 18:23:39 +0400
carrier_destination:
  file:
    name: CA-R-2762@3-draft-DECLARATION--declare-is-blocked-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare IS_BLOCKED_BY

## Claim

### Prose Claim

A dependent Plan may start only after each Plan it is blocked by is Done. BLOCKS is the inverse alias: the prerequisite is written before the dependent.

### Formal Claim

```CFEL
# model
Relation//BLOCKS ((IS_INVERSE_ALIAS_FOR)) Relation//IS_BLOCKED_BY;

Relation//IS_BLOCKED_BY ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$dependent[<Atom>, (.Header.Context.Role = Plan)] ((IS_BLOCKED_BY)) $prerequisite[<Atom>, (.Header.Context.Role = Plan)]
```

## Semantics

IS_BLOCKED_BY relates a dependent Plan to a prerequisite Plan.
