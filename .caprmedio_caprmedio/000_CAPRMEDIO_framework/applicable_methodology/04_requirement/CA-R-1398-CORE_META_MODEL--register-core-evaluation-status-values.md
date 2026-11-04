---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Status'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1398
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1398-CORE_META_MODEL--register-core-evaluation-status-values.md
  source_atom_id: CA-R-1398
  source_atom_revision: 24
  source_sha256: 485e7d516f83ad84e487db10cf7c83981ee8110b2b18fd07c5eb6eedfda001ec
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Evaluation Status Values

## Claim

### Prose Claim


the Core Evaluation Status model.


the Core allowed values of Evaluation Status **must** be exactly (Draft, Active, Archived).
