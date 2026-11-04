---
atom_id: CA-R-2170
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_DERIVED_RELATION_OF
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 12
updated_at: 2026-11-04 23:01:11 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2170-CORE_META_MODEL-DECLARATION--define-is-derived-relation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2170-CORE_META_MODEL-DECLARATION--define-is-derived-relation-of-relation.md
  source_atom_id: CA-R-2170
  source_atom_revision: 12
  source_sha256: ef0c37ed0a42722ceac6738764284d5b8ab37decb0a0dab2ab09abc59ab83db7
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Define is derived relation of relation

## Claim

### Formal Claim

```CFEL
# model
Relation//$relation ((IS_DERIVED_RELATION_OF)) Relation//$relation_2;

Relation//IS_DERIVED_RELATION_OF ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

IS_DERIVED_RELATION_OF relates a derived Relation Type instance to its source Relation Type instance. It does not itself specify the endpoint transformation or any qualification. A direct Declaration's inverse binding entails the bound inverse's IS_DERIVED_RELATION_OF link to the direct Relation. A qualified derivation must retain its explicit qualification; it must not be normalized to an unconditional inverse.
