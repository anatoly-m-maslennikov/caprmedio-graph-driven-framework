---
atom_id: CA-R-2354
ref_id: CA-R-2354
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Meaning
tier: 1
status: Active
version: 7
updated_at: 2026-11-04 22:00:28 +0400
carrier_destination:
  file:
    name: CA-R-2354-DECLARATION--define-relation-meaning.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2354-CORE_META_MODEL-ENTITY_DEFINITION--define-relation-meaning.md
  source_atom_id: CA-R-2354
  source_atom_revision: 7
  source_sha256: 8059eca3ff9f3421e2914ff2220fb8ebd23bd62af0d62f15727049974ca2cc6a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Relation Meaning

## Claim

### Prose Claim


Relation Meaning is the canonical meaning of a reusable Relation Type.
### Formal Claim

```CFEL
# model
Relation.Meaning{::1}:: [string]{::1};

Relation.Meaning.*[]{::0}
```

