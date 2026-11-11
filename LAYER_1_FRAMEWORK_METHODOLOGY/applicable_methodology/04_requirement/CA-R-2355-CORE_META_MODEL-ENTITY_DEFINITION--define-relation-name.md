---
atom_id: CA-R-2355
ref_id: CA-R-2355
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Name
tier: 1
status: Active
version: 7
updated_at: 2026-11-04 22:00:28 +0400
carrier_destination:
  file:
    name: CA-R-2355-DECLARATION--define-relation-name.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2355-CORE_META_MODEL-ENTITY_DEFINITION--define-relation-name.md
  source_atom_id: CA-R-2355
  source_atom_revision: 7
  source_sha256: 95dc399cbfd48e1fa81602bfa3dda2df327c050f8e71dfd123c7a53560b2a5a6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Relation Name

## Claim

### Prose Claim


Relation Name is the canonical name of a reusable Relation Type.
### Formal Claim

```CFEL
# model
Relation.Name{::1}:: [string]{::1};

Relation.Name.*[]{::0}
```

