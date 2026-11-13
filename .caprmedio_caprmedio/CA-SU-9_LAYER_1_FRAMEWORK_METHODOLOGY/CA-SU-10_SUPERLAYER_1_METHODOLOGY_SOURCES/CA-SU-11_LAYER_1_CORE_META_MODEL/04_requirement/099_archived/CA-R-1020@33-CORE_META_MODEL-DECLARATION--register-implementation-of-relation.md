---
atom_id: CA-R-1020
ref_id: CA-R-1020@33
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//implementation_of
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: archived
version: 33
updated_at: 2026-11-04 22:00:28 +0400
carrier_destination:
  file:
    name: CA-R-1020@33-CORE_META_MODEL-DECLARATION--register-implementation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
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

