---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Actor/Type: AI Agent", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Atom/Content Role: Plan.Label"]
version: 10
updated_at: "2026-10-19 15:53:38 +0400"
relations: {"relates_to": ["CA-R-1575", "CA-R-1584"]}
atom_id: "CA-R-1589"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
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
