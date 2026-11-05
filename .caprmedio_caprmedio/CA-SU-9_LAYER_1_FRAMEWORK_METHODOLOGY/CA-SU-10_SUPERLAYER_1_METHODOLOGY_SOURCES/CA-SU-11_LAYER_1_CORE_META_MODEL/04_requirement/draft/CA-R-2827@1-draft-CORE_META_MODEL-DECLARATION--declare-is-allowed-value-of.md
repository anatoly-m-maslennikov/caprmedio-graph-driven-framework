---
atom_id: CA-R-2827
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_ALLOWED_VALUE_OF
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 16:41:12 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2827@1-draft-CORE_META_MODEL-DECLARATION--declare-is-allowed-value-of.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare IS_ALLOWED_VALUE_OF

## Claim

### Formal Claim

```CFEL
# model
$relation[<Relation>, (.Name = IS_ALLOWED_VALUE_OF)];

$inverse[<Relation>, (.Name = HAS_ALLOWED_VALUE)];

$relation <((HAS_INVERSE)) $inverse;

$relation ((HAS_CLASSIFICATION)) Derivation == Derived;

$host ((IS_ALLOWED_VALUE_OF)) $target
```

### Prose Claim

The Host is an admitted literal value or literal-alternative set and the Target is the qualified model Subject or instance. This is the inverse view of HAS_ALLOWED_VALUE.

## Semantics

IS_ALLOWED_VALUE_OF expresses the derived inverse view.
