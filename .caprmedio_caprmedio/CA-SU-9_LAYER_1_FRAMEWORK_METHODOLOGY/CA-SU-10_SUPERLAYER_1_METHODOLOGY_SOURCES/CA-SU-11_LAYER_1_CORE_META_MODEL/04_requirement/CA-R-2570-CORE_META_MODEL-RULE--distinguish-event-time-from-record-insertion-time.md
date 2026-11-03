---
atom_id: CA-R-2570
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Distinguish event time from record insertion time

## Claim

- Event Record.happened_at is the time the recorded event happened.
- Event Record.inserted_at is the time the record was added to its Journal.
- Delayed insertion does not replace happened_at with inserted_at.
