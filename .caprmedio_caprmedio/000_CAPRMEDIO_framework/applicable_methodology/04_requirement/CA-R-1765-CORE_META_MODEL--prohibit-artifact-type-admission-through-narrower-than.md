---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
version: 35
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1765
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1765-CORE_META_MODEL--prohibit-artifact-type-admission-through-narrower-than.md
  source_atom_id: CA-R-1765
  source_atom_revision: 35
  source_sha256: 46e9c3b5ae07f4aeb2463ff31fb58cd5aa04c57e990dc012f908006a586e5dbb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Prohibit Artifact Type admission through NARROWER_THAN

## Claim

### Prose Claim


Artifact Type values.


an Artifact Type value **must not** use NARROWER_THAN **to** establish its admission as an Artifact.
