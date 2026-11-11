---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Term//Artifact
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//NARROWER_THAN
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
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1765-CORE_META_MODEL--prohibit-artifact-type-admission-through-narrower-than.md
  source_atom_id: CA-R-1765
  source_atom_revision: 35
  source_sha256: c00900b9c43d22201bba352d484b2c3ddc6c567c276a2fa6055d37b8fe3abc6c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Prohibit Artifact Type admission through NARROWER_THAN

## Claim scope

Artifact Type values.

## Claim

an Artifact Type value **must not** use NARROWER_THAN **to** establish its admission as an Artifact.
