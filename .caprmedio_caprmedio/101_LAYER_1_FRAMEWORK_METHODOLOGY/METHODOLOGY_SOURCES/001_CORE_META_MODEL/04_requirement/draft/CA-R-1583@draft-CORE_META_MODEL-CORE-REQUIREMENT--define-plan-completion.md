---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan.Status: Done"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Atom/Content Role: Plan/Type: Plan.Definition of Done", "File Carrier", "Hub Atom"]
version: 6
updated_at: "2026-10-15 12:13:48 +0000"
relations: {"relates_to": ["CA-R-1575", "CA-R-1579", "CA-R-1599", "CA-R-1539"]}
atom_id: "CA-R-1583@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
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
