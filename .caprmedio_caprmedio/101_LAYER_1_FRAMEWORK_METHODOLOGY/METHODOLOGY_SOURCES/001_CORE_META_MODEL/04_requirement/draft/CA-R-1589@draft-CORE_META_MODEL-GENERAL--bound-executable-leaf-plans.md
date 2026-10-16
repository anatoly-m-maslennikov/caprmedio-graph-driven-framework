---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Actor/Type: AI Agent", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Atom/Content Role: Plan.Label"]
version: 8
updated_at: "2026-10-16 11:59:20 +0000"
relations: {"relates_to": ["CA-R-1575", "CA-R-1584"]}
atom_id: "CA-R-1589@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Bound executable leaf Plans

## Scope

executable Plans with **none** direct decompositions.

## Claim

**every** executable Plan with **none** direct decompositions **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a composite Plan **may** have a larger roll-up estimate. the rule applies independently of Label.

## Details
