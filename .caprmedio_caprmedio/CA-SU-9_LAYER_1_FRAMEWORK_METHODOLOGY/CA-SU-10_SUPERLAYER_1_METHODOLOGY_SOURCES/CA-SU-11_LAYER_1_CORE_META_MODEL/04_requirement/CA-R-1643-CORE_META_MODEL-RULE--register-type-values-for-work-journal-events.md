---
atom_id: CA-R-1643
ref_id: CA-R-1643
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Journal
tier: 2
status: Active
version: 41
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-1643-CORE_META_MODEL-RULE--register-type-values-for-work-journal-events.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Type Values for Work Journal Events

## Claim

### Prose Claim


legacy Work Journal execution-observation category labels in serialized Journal Carrier Main Content.


the Main Content of a serialized Journal Carrier **must** preserve a supplied legacy Work Journal execution-observation category label as one of (Started, Progressed, Completed, Failed, Interrupted, Abandoned, Recovered).

this is a Carrier representation constraint. It does **not** create a logical Event Record Property, prescribe an Event Record business Action, or make these legacy observation labels model-level action values.
