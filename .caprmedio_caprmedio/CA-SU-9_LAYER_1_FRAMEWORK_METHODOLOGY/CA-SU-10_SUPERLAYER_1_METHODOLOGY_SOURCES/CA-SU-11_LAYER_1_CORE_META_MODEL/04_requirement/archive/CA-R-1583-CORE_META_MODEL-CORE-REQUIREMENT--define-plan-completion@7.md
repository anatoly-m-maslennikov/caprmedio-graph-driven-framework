---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Status: Done"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Atom/Content Role: Plan.Definition of Done", "Entity/Carrier/File Carrier", "Hub Atom"]
version: 7
updated_at: "2026-10-15 18:44:42 +0000"
relations: {"relates_to": ["CA-R-1575", "CA-R-1579", "CA-R-1599", "CA-R-1539"]}
atom_id: "CA-R-1583"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Plan completion

## Scope

Plan completion.

## Claim

Plan Status Done **means** that **all** applicable completion conditions hold:

- the Plan satisfies CA-R-1575; absence of work **and** decomposition **must not** count as completion.
- its own work, **if** present, is complete.
- **every** directly decomposed Plan is Done.
- its Definition of Done falsifying Condition Expression evaluates **to** false.

a Hub requires its own Definition of Done **and** completion of its decomposed Plans; Canceled **or** Archived work does **not** satisfy Done.

## Details
