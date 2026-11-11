---
atom_id: CA-R-1020
ref_id: CA-R-1020
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//implementation_of
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 33
updated_at: 2026-11-04 22:00:28 +0400
carrier_destination:
  file:
    name: CA-R-1020-DECLARATION--register-implementation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1020-CORE_META_MODEL-DECLARATION--register-implementation-of-relation.md
  source_atom_id: CA-R-1020
  source_atom_revision: 33
  source_sha256: 945236390226e3864d89a994080ba29c047a5754769beff12b774f567a780327
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register implementation_of relation

## Claim

### Prose Claim

implementation_of is the direct Relation owned by a governed Implementation Carrier. The Host is that governed Implementation Carrier and each tuple targets the specification Atom it implements.

### Formal Claim

```CFEL
# model
Relation//implementation_of ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Carrier//$implementation_carrier ((implementation_of)) Atom//$specification_atom
```

