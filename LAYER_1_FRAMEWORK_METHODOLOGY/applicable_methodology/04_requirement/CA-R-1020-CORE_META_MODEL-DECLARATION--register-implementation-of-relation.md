---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//implementation_of
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 33
updated_at: 2026-11-04 22:00:28 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-1020
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1020-CORE_META_MODEL-DECLARATION--register-implementation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1020-CORE_META_MODEL-DECLARATION--register-implementation-of-relation.md
  source_atom_id: CA-R-1020
  source_atom_revision: 33
  source_sha256: ada8da157faca9804f4f79e3bf35aea8bdd1e33e967f9c6fc8c2dfb489aad143
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Register implementation_of relation

## Claim

### Formal Claim

```CFEL
# model
Relation//implementation_of ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Carrier//$implementation_carrier ((implementation_of)) Atom//$specification_atom
```

### Prose Claim

implementation_of is the direct Relation owned by a governed Implementation Carrier. The Host is that governed Implementation Carrier and each tuple targets the specification Atom it implements.

