---
atom_id: CA-D-559
ref_id: CA-D-559
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Journal
  dependencies:
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication"
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 19
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-D-559-CORE_META_MODEL-DECISION--deliver-runtime-journals-to-configured-sinks.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-559-CORE_META_MODEL-ENG_DECISION--deliver-runtime-journals-to-configured-sinks.md
  source_atom_id: CA-D-559
  source_atom_revision: 19
  source_sha256: efabd2ff050d839af2071c2d8f12bf336c98156f8af2643e19bf09d30cbedba1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Deliver runtime Journals to configured sinks

## Claim

### Prose Claim


technical and business runtime Journal Carriers.


runtime technical **and** business Journals **may** be delivered **to** an explicitly configured local database, remote database, **or** governed logging sink. these Carriers **need not** reside under `.caprmedio_<project_name>/_journal/` **or** `.caprmedio_runtime/`.

## Details

Journal classification and recorded-history authority are independent of storage technology. The configuration identifies the intended sink; applicable production logging policy remains in force. The shared Project-control Work Journal and persistent view Projections retain their separate _journal and _projection locations. Runtime cleanup and sink migration must preserve accepted Journal history; this Delivery does not authorize history deletion or change retention policy.
