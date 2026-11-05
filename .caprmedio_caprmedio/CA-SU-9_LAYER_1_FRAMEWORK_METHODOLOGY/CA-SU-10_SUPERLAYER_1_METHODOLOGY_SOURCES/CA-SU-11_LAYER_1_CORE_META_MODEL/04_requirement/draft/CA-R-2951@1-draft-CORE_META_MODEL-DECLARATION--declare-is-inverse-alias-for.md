---
atom_id: CA-R-2951
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_INVERSE_ALIAS_FOR
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 18:23:39 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2951@1-draft-CORE_META_MODEL-DECLARATION--declare-is-inverse-alias-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare IS_INVERSE_ALIAS_FOR

## Claim

### Formal Claim

```CFEL
# model
$host ((IS_INVERSE_ALIAS_FOR)) $target
```

### Prose Claim

IS_INVERSE_ALIAS_FOR binds an inverse alias model address to its canonical Relation model address. The inverse alias is introduced by the canonical Relation Declaration and is not a separate Relation entity or Declaration. Normalizing an inverse alias to its canonical Relation swaps the written endpoints and their cardinality slots, preserving the numeric bounds. Explicit reverse writing of an inverse alias reverses its endpoints and slots again. Both writings refer to the same fact. This binding infers no bounds, grants no endpoint permission and creates no second authored Relation fact.

## Semantics

IS_INVERSE_ALIAS_FOR relates an inverse alias address to its canonical Relation address.
