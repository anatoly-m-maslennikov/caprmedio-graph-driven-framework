---
subjects:
  active: CAPRMEDIO_MODEL <+ Journal
  passive:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ History
  - CAPRMEDIO_MODEL <+ Actor
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1644
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
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
