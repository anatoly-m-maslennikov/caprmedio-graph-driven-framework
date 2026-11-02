---
subjects:
  governs: Entity/Object/Continuant/History/Journal > Event Record
  depends_on:
  - Entity/Object/Continuant/History/Journal
  - Entity/Carrier
  - Entity/Object/Continuant/History
  - Entity/Object/Continuant/Actor
version: 34
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1644@34
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Recover Work Journal coverage without invention

## Claim scope

`recovered` Journal events.

## Claim

a `recovered` Journal event is admissible **only** for facts established by **any** of:

- observed Carrier state;
- preserved history;
- Artifact movement;
- native targets;
- review records; **or**
- bounded session state.

unresolved Actor, time, intent, scope, **or** outcome **must** remain explicit uncertainty rather than fabricated history.
