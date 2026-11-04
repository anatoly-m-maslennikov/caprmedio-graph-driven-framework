---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-466-CORE_META_MODEL-ENG_DECISION--place-carriers-by-applicable-status-delivery.md
  source_atom_id: CA-D-466
  source_atom_revision: 22
  source_sha256: dcd0762c4a64841de241ab40163b435eeaef9d6cbc8f6c8c467eee31b8260e31
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place Carriers by Applicable Status Delivery

## Claim

### Prose Claim


Carrier placement where an applicable qualified Artifact Status model exists or does not exist.


**when** an applicable qualified Artifact Status model exists **and** an Artifact has **`=1`** valid current Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more-specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** no applicable qualified Status model exists, Carrier placement **must not** derive a Status directory from absent Status.
