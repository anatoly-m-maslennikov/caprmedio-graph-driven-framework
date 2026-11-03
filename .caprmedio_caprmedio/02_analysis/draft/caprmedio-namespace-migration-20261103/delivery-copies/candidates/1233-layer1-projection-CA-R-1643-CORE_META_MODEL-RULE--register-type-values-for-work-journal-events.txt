---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Main Content
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Journal
version: 40
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1643
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1643-CORE_META_MODEL-RULE--register-type-values-for-work-journal-events.md
  source_atom_id: CA-R-1643
  source_atom_revision: 40
  source_sha256: 0d9253a3ecdb85f101c378ff2e7d3ce4a010476900c79141c4fb985065d7d914
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Type Values for Work Journal Events

## Claim scope

legacy Work Journal execution-observation category labels in serialized Journal Carrier Main Content.

## Claim

the Main Content of a serialized Journal Carrier **must** preserve a supplied legacy Work Journal execution-observation category label as one of (Started, Progressed, Completed, Failed, Interrupted, Abandoned, Recovered).

this is a Carrier representation constraint. It does **not** create a logical Event Record Property, prescribe an Event Record business Action, or make these legacy observation labels model-level action values.
