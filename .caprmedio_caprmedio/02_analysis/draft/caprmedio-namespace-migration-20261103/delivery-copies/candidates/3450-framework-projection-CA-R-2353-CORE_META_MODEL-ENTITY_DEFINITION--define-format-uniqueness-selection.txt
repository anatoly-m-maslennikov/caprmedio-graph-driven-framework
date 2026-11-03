---
atom_id: CA-R-2353
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Format.Uniqueness Selection
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2353-CORE_META_MODEL-ENTITY_DEFINITION--define-format-uniqueness-selection.md
  source_atom_id: CA-R-2353
  source_atom_revision: 4
  source_sha256: c1f11a6487cf52a4ba89eba4eab9b416908036f9ea5071163901db62100d8ba3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Format Uniqueness Selection

## Claim

Format Uniqueness Selection identifies the comparison population for a
Property uniqueness check. It is optional and does not itself impose
uniqueness. It does not define a notation.


```CFEL
Format.Uniqueness Selection{:0..1}: [string]{:1};
Format.Uniqueness Selection.*[]{:0}
```

## Details

Source meaning: CA-R-2248. Scope-specific constraints remain in the governing
Format Definition.
