---
atom_id: CA-R-2352
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format.Data Type
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2352-CORE_META_MODEL-ENTITY_DEFINITION--define-format-data-type.md
  source_atom_id: CA-R-2352
  source_atom_revision: 4
  source_sha256: 3a72c8046ec99c344ff115d37f23f07ffd97dd384d356c35e1705aad06b6b888
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Format Data Type

## Claim

Format Data Type names the admissible value domain of a direct Property value.
It is separate from cardinality. The initial vocabulary is provisional; list,
map and reference semantics remain with the governing Format definition.


```CFEL
Format.Data Type{:1}: [string]{:1};
Format.Data Type.*[]{:0}
```

## Details

Source meaning: CA-R-2248. Scope-specific constraints remain in the governing
Format Definition.
