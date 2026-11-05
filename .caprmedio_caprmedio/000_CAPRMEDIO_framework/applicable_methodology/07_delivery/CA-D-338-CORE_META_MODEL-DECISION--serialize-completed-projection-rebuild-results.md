---
atom_id: CA-D-338
ref_id: CA-D-338
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Projection
tier: 2
status: Active
version: 30
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-338-CORE_META_MODEL-DECISION--serialize-completed-projection-rebuild-results.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-338-CORE_META_MODEL-DECISION--serialize-completed-projection-rebuild-results.md
  source_atom_id: CA-D-338
  source_atom_revision: 30
  source_sha256: f330ec894e86f1e68c93cfb05d0f181ca364c0cec7cbb9f43eca0427351c0893
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Completed Projection Rebuild Results

## Claim

### Prose Claim


encoded completed Projection Rebuild Event Record results.


the Main Content that encodes a completed Projection Rebuild Event Record **must** serialize the published Projection Updated At value, output Carrier reference, **and** content digest.
