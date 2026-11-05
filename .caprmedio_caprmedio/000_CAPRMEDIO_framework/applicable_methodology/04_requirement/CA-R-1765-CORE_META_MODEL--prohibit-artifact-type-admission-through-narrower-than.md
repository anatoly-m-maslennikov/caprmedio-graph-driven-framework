---
atom_id: CA-R-1765
ref_id: CA-R-1765
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
tier: 1
status: Active
version: 35
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1765-CORE_META_MODEL-RULE--prohibit-artifact-type-admission-through-narrower-than.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1765-CORE_META_MODEL--prohibit-artifact-type-admission-through-narrower-than.md
  source_atom_id: CA-R-1765
  source_atom_revision: 35
  source_sha256: 0918c7eb05ad41b6cf928525f5a3dba9cf51f428c6e5e68f19c6bb446ce33d33
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Prohibit Artifact Type admission through NARROWER_THAN

## Claim

### Prose Claim


Artifact Type values.


an Artifact Type value **must not** use NARROWER_THAN **to** establish its admission as an Artifact.
