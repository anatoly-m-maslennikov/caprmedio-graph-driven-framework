---
atom_id: CA-R-2170
ref_id: CA-R-2170
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_DERIVED_RELATION_OF
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 12
updated_at: 2026-11-04 23:01:11 +0400
carrier_destination:
  file:
    name: CA-R-2170-DECLARATION--define-is-derived-relation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define is derived relation of relation

## Claim

### Prose Claim

IS_DERIVED_RELATION_OF relates a derived Relation Type instance to its source Relation Type instance. It does not itself specify the endpoint transformation or any qualification. A direct Declaration's inverse binding entails the bound inverse's IS_DERIVED_RELATION_OF link to the direct Relation. A qualified derivation must retain its explicit qualification; it must not be normalized to an unconditional inverse.
### Formal Claim

```CFEL
# model
Relation//$relation ((IS_DERIVED_RELATION_OF)) Relation//$relation_2;

Relation//IS_DERIVED_RELATION_OF ((HAS_CLASSIFICATION)) Derivation == Direct
```

