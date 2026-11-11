---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Delivery)
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
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-466-CORE_META_MODEL-ENG_DECISION--place-carriers-by-applicable-status-delivery.md
  source_atom_id: CA-D-466
  source_atom_revision: 22
  source_sha256: 8f6cded8346ae026df96023a5a3b3aa73ca6447350991bfb4c5e2bf49640e694
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place Carriers by Applicable Status Delivery

## Claim scope

Carrier placement where an applicable qualified Artifact Status model exists or does not exist.

## Claim

**when** an applicable qualified Artifact Status model exists **and** an Artifact has **`=1`** valid current Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more-specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** no applicable qualified Status model exists, Carrier placement **must not** derive a Status directory from absent Status.
