---
atom_id: CA-R-2828
ref_id: CA-R-2828@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_VALUE_CONSTRAINT
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 16:41:12 +0400
carrier_destination:
  file:
    name: CA-R-2828@1-draft-DECLARATION--declare-has-value-constraint.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare HAS_VALUE_CONSTRAINT

## Claim

### Prose Claim

The Host is the qualified model Subject or instance to which the constraint applies. The Target is constraint data, including a Format or cardinality constraint, not a model Node. For the same qualified Subject, all applicable HAS_VALUE_CONSTRAINT expressions, including inherited expressions, combine by AND. If none applies, that group contributes true. Final admissibility combines this AND group with the applicable HAS_ALLOWED_VALUE OR group. `x :: [string]` and `x :: {::1}` may be written together as `x :: [string]{::1}`.

### Formal Claim

```CFEL
# model
$relation[<Relation>, (.Name = HAS_VALUE_CONSTRAINT)];

$inverse[<Relation>, (.Name = IS_VALUE_CONSTRAINT_OF)];

$relation ((HAS_INVERSE)) $inverse;

$relation ((HAS_CLASSIFICATION)) Derivation == Direct;

alias($relation) == "::";

$host ((HAS_VALUE_CONSTRAINT)) $target
```

## Semantics

HAS_VALUE_CONSTRAINT expresses the direct value rule.
