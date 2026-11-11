---
atom_id: CA-R-1399
ref_id: CA-R-1399
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery).Header.State.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
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
---
## Summary

Register Core Delivery Status Values

## Claim

### Prose Claim


the Core Delivery Status model.


the Core allowed values of Delivery Status **must** be exactly (Draft, Active, Archived).
