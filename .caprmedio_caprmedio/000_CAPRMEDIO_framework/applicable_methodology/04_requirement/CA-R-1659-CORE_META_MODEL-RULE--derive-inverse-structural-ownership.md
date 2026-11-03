---
subjects:
  active: CFEL <+ Relation
version: 31
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1756
atom_id: CA-R-1659
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1659-CORE_META_MODEL-RULE--derive-inverse-structural-ownership.md
  source_atom_id: CA-R-1659
  source_atom_revision: 31
  source_sha256: 19e7e36d952ed6a5e0d91ce68351250ea041ea0096dacde175d09479e4163c8a
  original_relations_sha256: 7f6ad774f4a8dbcb06ed291239fe4f8c20c3c04d6c9490bdc10c6fb2680d87fd
---
## Summary

Derive inverse structural ownership

## Claim scope

the inverse `structural_children` view derived from stored `structural_parent` relations.

## Claim

CAPRMEDIO **must** derive the inverse `structural_children` view from stored `structural_parent` relations **and** **must not** persist that inverse separately.
