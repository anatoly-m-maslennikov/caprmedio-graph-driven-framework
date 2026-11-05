---
atom_id: CA-R-2352
ref_id: CA-R-2352
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format.Data Type
tier: 1
status: Active
version: 5
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2352-CORE_META_MODEL-DECLARATION--define-format-data-type.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2352-CORE_META_MODEL-ENTITY_DEFINITION--define-format-data-type.md
  source_atom_id: CA-R-2352
  source_atom_revision: 5
  source_sha256: 7d8bf7346a6714e6e0248ebf68e64c49883b4e7bc8f068df4622050a364512a1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Format Data Type

## Claim

### Prose Claim


Format Data Type names the admissible value domain of a direct Property value.
It is separate from cardinality. The initial vocabulary is provisional; list,
map and reference semantics remain with the governing Format definition.



### Formal Claim

```CFEL
# model
Format.Data Type{::1}:: [string]{::1};

Format.Data Type.*[]{::0}
```

