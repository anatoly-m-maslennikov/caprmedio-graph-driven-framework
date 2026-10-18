---
subjects:
  governs: "Entity/Continuant/Node/History/Journal.Record"
  depends_on:
    ["Entity/Continuant/Node/History/Journal", "Entity/Carrier", "Entity/Continuant/Node/History", "Entity/Continuant/Node/Actor"]
version: 21
updated_at: "2026-10-18 03:33:47 +0400"
relations: {}
atom_id: "CA-R-1644"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
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
