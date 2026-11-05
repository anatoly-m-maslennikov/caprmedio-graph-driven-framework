---
atom_id: CA-D-341
ref_id: CA-D-341
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
tier: 1
status: Active
version: 29
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-341-CORE_META_MODEL-DECISION--separate-persistent-authority-from-runtime-state.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Separate Persistent Authority from Runtime State

## Claim

### Prose Claim


persistent Carriers holding canonical authority or retained history, in relation to runtime cleanup.


runtime cleanup **must not** remove persistent Carriers holding canonical authority or retained history.

## Details

Delivery placement and retention rules must keep that content outside the cleanup target set. This protection does not require a Carrier.Ownership Class or Carrier.Storage Boundary property, and it does not classify a Carrier as disposable merely because a runtime uses it.
