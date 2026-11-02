---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Target Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom.Target Scope Unit", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Atom/Content Role: Plan.Label"]
version: 11
updated_at: "2026-10-19 15:53:37 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-D-482"]}
atom_id: "CA-R-1588"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Default Plan target to the enclosing Scope Unit

## Scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of decomposition **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.

## Details
