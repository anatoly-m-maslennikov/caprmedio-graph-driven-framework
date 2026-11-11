---
atom_id: CA-R-2829
ref_id: CA-R-2829@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_VALUE_CONSTRAINT_OF
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 16:41:12 +0400
carrier_destination:
  file:
    name: CA-R-2829@1-draft-DECLARATION--declare-is-value-constraint-of.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare IS_VALUE_CONSTRAINT_OF

## Claim

### Prose Claim

The Host is constraint data and the Target is the qualified model Subject or instance. This is the inverse view of HAS_VALUE_CONSTRAINT.

### Formal Claim

```CFEL
# model
$relation[<Relation>, (.Name = IS_VALUE_CONSTRAINT_OF)];

$inverse[<Relation>, (.Name = HAS_VALUE_CONSTRAINT)];

$relation <((HAS_INVERSE)) $inverse;

$relation ((HAS_CLASSIFICATION)) Derivation == Derived;

$host ((IS_VALUE_CONSTRAINT_OF)) $target
```

## Semantics

IS_VALUE_CONSTRAINT_OF expresses the derived inverse view.
