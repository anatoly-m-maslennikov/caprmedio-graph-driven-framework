---
atom_id: CA-D-310
ref_id: CA-D-310
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Updated At
tier: 3
status: Active
version: 26
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-D-310-CORE_META_MODEL-DECISION--serialize-projection-updated-at.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-310-CORE_META_MODEL-ENG_DECISION--serialize-projection-updated-at.md
  source_atom_id: CA-D-310
  source_atom_revision: 26
  source_sha256: e1cc76a65c8cac278d2095a3dc9a438cd35003ba14ae1883ed67c415cb955d85
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Projection Updated At

## Claim

### Prose Claim


Projection Carrier latest completed rebuild times.


**every** Projection Carrier **must** serialize the time of its latest completed rebuild as `updated_at` **in** Project time **without** treating that value alone as proof of currentness.
