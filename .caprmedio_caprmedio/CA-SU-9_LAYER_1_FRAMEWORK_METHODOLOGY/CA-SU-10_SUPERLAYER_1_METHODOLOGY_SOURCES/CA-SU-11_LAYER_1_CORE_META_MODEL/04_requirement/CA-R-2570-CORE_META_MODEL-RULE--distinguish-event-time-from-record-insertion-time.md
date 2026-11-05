---
atom_id: CA-R-2570
ref_id: CA-R-2570
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2570-CORE_META_MODEL-RULE--distinguish-event-time-from-record-insertion-time.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Distinguish event time from record insertion time

## Claim

### Prose Claim


- Event Record.happened_at is the time the recorded event happened.
- Event Record.inserted_at is the time the record was added to its Journal.
- Delayed insertion does not replace happened_at with inserted_at.
