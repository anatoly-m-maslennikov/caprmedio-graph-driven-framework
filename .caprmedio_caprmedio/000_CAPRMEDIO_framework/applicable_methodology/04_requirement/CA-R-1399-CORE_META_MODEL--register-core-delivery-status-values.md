---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery).Header.Status'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1399
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1399-CORE_META_MODEL--register-core-delivery-status-values.md
  source_atom_id: CA-R-1399
  source_atom_revision: 24
  source_sha256: 60279a9958fc5a7445f640dfe67f9d661998c3eb6fd2661f565eadaa224fce1e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Delivery Status Values

## Claim

### Prose Claim


the Core Delivery Status model.


the Core allowed values of Delivery Status **must** be exactly (Draft, Active, Archived).
