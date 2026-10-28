---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Actor
version: 31
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
atom_id: CA-R-1644
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Recover Work Journal coverage without invention

## Scope

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

## Details
