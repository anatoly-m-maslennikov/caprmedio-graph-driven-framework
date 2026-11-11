---
atom_id: CA-R-2570
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Event Record
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2570-CORE_META_MODEL-RULE--distinguish-event-time-from-record-insertion-time.md
  source_atom_id: CA-R-2570
  source_atom_revision: 2
  source_sha256: 97de7a66486602f1ba2c9adb81d839d8f168811b0b0256bd30e521743ac63f28
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Distinguish event time from record insertion time

## Claim

- Event Record.happened_at is the time the recorded event happened.
- Event Record.inserted_at is the time the record was added to its Journal.
- Delayed insertion does not replace happened_at with inserted_at.
