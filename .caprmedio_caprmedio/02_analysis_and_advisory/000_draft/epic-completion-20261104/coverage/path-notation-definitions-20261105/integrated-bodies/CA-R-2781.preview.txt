---
atom_id: CA-R-2781
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Operator//Containment
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 05:13:56 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2781@1-draft-CORE_META_MODEL-DECLARATION--declare-cfel-containment-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare CFEL containment operator /

## Claim

### Formal Claim

```CFEL
# model
Operator//Containment == "/"
```

### Prose Claim

`Whole/Part` expresses the immediate `CONTAINS` Relation from Whole to Part. Its corresponding direct `IS_CONTAINED_BY` fact runs from Part to Whole. Containment does not imply narrowing or inheritance.

When directional cardinality slots are present, the slot before `/` counts outgoing `CONTAINS` links per Whole, and the slot after `/` counts reverse `IS_CONTAINED_BY` links per Part. Omitted slots remain unspecified. A Relation declaration or an applicable endpoint permission supplies its own bounds.

## Semantics

`/` expresses immediate containment from a Whole to a Part.
