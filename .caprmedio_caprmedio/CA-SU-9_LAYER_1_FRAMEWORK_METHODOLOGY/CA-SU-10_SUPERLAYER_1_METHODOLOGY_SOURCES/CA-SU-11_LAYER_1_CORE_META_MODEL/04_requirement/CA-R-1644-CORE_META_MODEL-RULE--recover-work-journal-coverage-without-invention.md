---
atom_id: CA-R-1644
ref_id: CA-R-1644
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Journal
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Actor
tier: 1
status: Active
version: 39
updated_at: 2026-11-05 04:04:00 +0400
carrier_destination:
  file:
    name: CA-R-1644-CORE_META_MODEL-RULE--recover-work-journal-coverage-without-invention.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Recover Work Journal coverage without invention

## Claim

### Prose Claim


recovered observations retained by a Journal.


a Journal **may** retain an Event Record recovered from evidence **only** for facts established by **any** of:

- observed Carrier state;
- preserved history;
- Artifact movement;
- native targets;
- review records; **or**
- bounded session state.

the Journal **must** preserve unresolved Actor, time, intent, scope, **or** outcome as explicit uncertainty rather than fabricated history.
