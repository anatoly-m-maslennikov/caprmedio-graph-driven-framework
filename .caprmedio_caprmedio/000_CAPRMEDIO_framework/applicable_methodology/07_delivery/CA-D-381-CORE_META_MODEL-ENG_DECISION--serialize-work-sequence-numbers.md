---
atom_id: CA-D-381
ref_id: CA-D-381
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-381-CORE_META_MODEL-DECISION--serialize-work-sequence-numbers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-381-CORE_META_MODEL-ENG_DECISION--serialize-work-sequence-numbers.md
  source_atom_id: CA-D-381
  source_atom_revision: 23
  source_sha256: 435262f0a89c01f5a8dc32c780c7e61894a7104db8d43635f5643522fcd34bc3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Work Sequence Numbers

## Claim

### Prose Claim


Carrier renderings of a Work Sequence Number.


**every** Carrier rendering of a Work Sequence Number **must** use decimal digits.
