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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-341-CORE_META_MODEL-ENG_DECISION--separate-persistent-authority-from-runtime-state.md
  source_atom_id: CA-D-341
  source_atom_revision: 29
  source_sha256: 1532b71eb63ae51f5651d5703fdebf8dbe9f145ea653f25781337c501d13880f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Separate Persistent Authority from Runtime State

## Claim

### Prose Claim


persistent Carriers holding canonical authority or retained history, in relation to runtime cleanup.


runtime cleanup **must not** remove persistent Carriers holding canonical authority or retained history.

## Details

Delivery placement and retention rules must keep that content outside the cleanup target set. This protection does not require a Carrier.Ownership Class or Carrier.Storage Boundary property, and it does not classify a Carrier as disposable merely because a runtime uses it.
