---
atom_id: CA-R-2567
ref_id: CA-R-2567
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2567-CORE_META_MODEL-RULE--record-business-property-changes-in-one-update-event-record.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Record business Property changes in one update Event Record

## Claim

### Prose Claim


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
