---
atom_id: CA-R-2567
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
---
## Summary

Record business Property changes in one update Event Record

## Claim

Event Records with action create or update describe accepted, completed business creations or updates. No-op, failed, unaccepted, archive and Carrier-only events do not use these actions.

One accepted business update has one update Event Record.

- Its change delta contains only changed logical Properties.
- Atom.Content and all its descendants are excluded from Event Records for now.
- Each recorded change identifies the Property by its complete path and records its old and new value or absence.
- Promotion is an update; Version and Status are included when they change.
- Updated At may be included when changed. Its new value follows the maximum of happened_at over accepted create and update Event Records for that object through this record’s happened_at.
- This recorded copy is audit evidence. It does not supply that maximum or constitute another business update.
- Carrier filename and directory changes are excluded from the delta.
- A Carrier-only rename or move creates no update Event Record.
