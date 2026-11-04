---
atom_id: CA-R-2354
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Meaning
version: 5
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2354-CORE_META_MODEL-ENTITY_DEFINITION--define-relation-meaning.md
  source_atom_id: CA-R-2354
  source_atom_revision: 5
  source_sha256: 605da11f69acff5cd94a7c5772fb07a869b21e782a0aca802aa556061edc4fd7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Relation Meaning

## Claim

### Formal Claim

```CFEL
# model
Relation.Meaning{:1}: [string]{:1};

Relation.Meaning.*[]{:0}
```

### Prose Claim


Relation Meaning is the canonical meaning of a reusable Relation Type.
Direction and transitivity describe the Type. An optional derived inverse is a
view of the direct tuple, not another authored edge. Actual source and target
endpoints remain tuple facts.



