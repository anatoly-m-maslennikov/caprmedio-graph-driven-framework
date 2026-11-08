---
atom_id: CA-D-309
ref_id: CA-D-309
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
tier: 1
status: Active
version: 27
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-309-CORE_META_MODEL-DECISION--bind-materialized-representations-to-regeneration-sources.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-309-CORE_META_MODEL-ENG_DECISION--bind-materialized-representations-to-regeneration-sources.md
  source_atom_id: CA-D-309
  source_atom_revision: 27
  source_sha256: ebab74b4d396bad30d1274038cd24eeafd7593b9978d62ac47f8d1e61d347bb5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bind Materialized Representations to Regeneration Sources

## Claim

### Prose Claim


admitted materialized representation Carriers.


**every** admitted materialized representation Carrier **must** have a recoverable binding **to** its exact canonical source Revision **and** **`=1`** deterministic regeneration **or** reconciliation rule.

the binding **may** be recovered through the selected authoritative source frontier **and** governing derivation authority; it does **not** require source metadata **to** be embedded **in** **every** resulting Carrier. an applicable Carrier specification determines whether **and** how **any** explicit binding is serialized.

for Applicable Methodology projected Atom Carriers, CA-D-305 requires an explicit one-way binding **to** the original source Atom Carrier while preserving its authored content, identity, **and** Revision. that specific binding **must not** create duplicate source authority **or** impose a blanket persisted source frontier on other Projections contrary **to** CA-R-1494.
