---
atom_id: CA-R-1398
ref_id: CA-R-1398
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
tier: 2
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1398-CORE_META_MODEL-RULE--register-core-evaluation-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1398-CORE_META_MODEL--register-core-evaluation-status-values.md
  source_atom_id: CA-R-1398
  source_atom_revision: 24
  source_sha256: ca7e956a8f696aed85c19c2f6cf46bbced6ae4dfd004155290c589d7d093bd22
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Evaluation Status Values

## Claim

### Prose Claim


the Core Evaluation Status model.


the Core allowed values of Evaluation Status **must** be exactly (Draft, Active, Archived).
