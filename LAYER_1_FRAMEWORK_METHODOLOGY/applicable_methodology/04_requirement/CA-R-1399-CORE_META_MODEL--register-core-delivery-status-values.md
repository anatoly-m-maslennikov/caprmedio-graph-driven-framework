---
atom_id: CA-R-1399
ref_id: CA-R-1399
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery).Header.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
tier: 2
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1399-CORE_META_MODEL-RULE--register-core-delivery-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1399-CORE_META_MODEL--register-core-delivery-status-values.md
  source_atom_id: CA-R-1399
  source_atom_revision: 24
  source_sha256: 34cc8fc7e025d55b46ac7ec405da4b88364aa381d0af538f48262d5cd354f540
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Delivery Status Values

## Claim

### Prose Claim


the Core Delivery Status model.


the Core allowed values of Delivery Status **must** be exactly (Draft, Active, Archived).
