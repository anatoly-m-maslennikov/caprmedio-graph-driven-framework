---
atom_id: CA-R-2951
ref_id: CA-R-2951
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_INVERSE_ALIAS_FOR
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2951-CORE_META_MODEL-RELATION_DECLARATION--declare-is-inverse-alias-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2951-CORE_META_MODEL-RELATION_DECLARATION--declare-is-inverse-alias-for.md
  source_atom_id: CA-R-2951
  source_atom_revision: 1
  source_sha256: e3d4b41f967387061299baf404c3e168187043c44aca690657f3365f913ca59a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare IS_INVERSE_ALIAS_FOR

## Claim

### Prose Claim

IS_INVERSE_ALIAS_FOR binds an inverse alias model address to its canonical Relation model address. The inverse alias is introduced by the canonical Relation Declaration and is not a separate Relation entity or Declaration. Normalizing an inverse alias to its canonical Relation swaps the written endpoints and their cardinality slots, preserving the numeric bounds. Explicit reverse writing of an inverse alias reverses its endpoints and slots again. Both writings refer to the same fact. This binding infers no bounds, grants no endpoint permission and creates no second authored Relation fact.

### Formal Claim

```CFEL
# model
$host ((IS_INVERSE_ALIAS_FOR)) $target
```

## Semantics

IS_INVERSE_ALIAS_FOR relates an inverse alias address to its canonical Relation address.
