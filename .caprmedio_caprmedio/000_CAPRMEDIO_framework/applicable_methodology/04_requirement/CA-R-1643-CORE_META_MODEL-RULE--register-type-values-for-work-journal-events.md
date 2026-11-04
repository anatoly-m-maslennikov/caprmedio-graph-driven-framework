---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Journal
version: 41
updated_at: 2026-11-03 23:25:51 +0400
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
  source_atom_revision: 41
  source_sha256: 77eb76f156c671e13eef5b7417582e4aee7ec8eed4cee1d2af6125440dbc114b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Type Values for Work Journal Events

## Claim

### Prose Claim


legacy Work Journal execution-observation category labels in serialized Journal Carrier Main Content.


the Main Content of a serialized Journal Carrier **must** preserve a supplied legacy Work Journal execution-observation category label as one of (Started, Progressed, Completed, Failed, Interrupted, Abandoned, Recovered).

this is a Carrier representation constraint. It does **not** create a logical Event Record Property, prescribe an Event Record business Action, or make these legacy observation labels model-level action values.
