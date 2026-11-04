---
atom_id: CA-R-2170
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_DERIVED_RELATION_OF
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 10
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
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
  source_atom_revision: 10
  source_sha256: cce56d07fa656084df11f1bf77aab9e0e357a74ac1ca2281cead891cc1d37510
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

IS_DERIVED_RELATION_OF relates a derived Relation Type instance to its source Relation Type instance. It does not itself specify the endpoint transformation or any qualification. A direct Declaration's inverse binding entails the bound inverse's IS_DERIVED_RELATION_OF link to the direct Relation. This inferred metadata is not repeated in the minimal derived Declaration. A qualified derivation must retain its explicit qualification; it must not be normalized to an unconditional inverse. This Relation is distinct from DERIVED_FROM between Artifact Revisions.
