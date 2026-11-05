---
atom_id: CA-R-2353
ref_id: CA-R-2353
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format.Uniqueness Selection
tier: 1
status: Active
version: 6
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2353-CORE_META_MODEL-DECLARATION--define-format-uniqueness-selection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2353-CORE_META_MODEL-ENTITY_DEFINITION--define-format-uniqueness-selection.md
  source_atom_id: CA-R-2353
  source_atom_revision: 6
  source_sha256: b0bfe54983a5d0b5135992cfff3a337202d6d9b696e2b56444e36377e75cc468
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Format Uniqueness Selection

## Claim

### Prose Claim


Format Uniqueness Selection identifies the comparison population for a
Property uniqueness check. It is optional and does not itself impose
uniqueness. It does not define a notation.



### Formal Claim

```CFEL
# model
Format.Uniqueness Selection:: [string]{::0..1};

Format.Uniqueness Selection.*[]{::0}
```

