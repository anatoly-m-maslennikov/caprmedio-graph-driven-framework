---
atom_id: CA-R-2965
ref_id: CA-R-2965
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL/CFEL/Relation//IS_ORDERED_RIGHT_AFTER
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2965-CORE_META_MODEL-RELATION_DECLARATION--declare-is-ordered-right-after.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare IS_ORDERED_RIGHT_AFTER

## Claim

### Prose Claim

The Host and Target are declared model Properties of the same immediate bearer, selected from the applicable Atom.Header or Atom.Content Property structure. The Host follows the Target immediately in the declared sibling order. Ordering is acyclic; each Property has at most one immediate predecessor and at most one immediate successor. The inverse alias IS_ORDERED_RIGHT_BEFORE reverses that reading; it denotes the same ordering fact.

`x ;> y` means x is immediately before y, in the order x; y. `x <; y` means x is immediately after y, in the order y; x. These Relations specify model Property order; they do not create runtime Property instances or copy facts.

### Formal Claim

```CFEL
# model
$host ((IS_ORDERED_RIGHT_AFTER)) $target;

Relation//IS_ORDERED_RIGHT_BEFORE ((IS_INVERSE_ALIAS_FOR)) Relation//IS_ORDERED_RIGHT_AFTER;

alias(Relation//IS_ORDERED_RIGHT_AFTER) == "<;";

alias(Relation//IS_ORDERED_RIGHT_BEFORE) == ";>"
```

## Semantics

IS_ORDERED_RIGHT_AFTER relates a model Property to its immediately preceding sibling Property.
