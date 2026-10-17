---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom.Target Scope Unit", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom/Content Role: Plan.Label"]
version: 9
updated_at: "2026-10-16 12:08:34 +0000"
relations: {"relates_to": ["CA-R-1574", "CA-D-482"]}
atom_id: "CA-R-1588"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1588-CORE_META_MODEL-CORE-REQUIREMENT--default-plan-target-to-the-enclosing-scope-unit.md
  source_atom_id: CA-R-1588
  source_atom_revision: 9
  source_sha256: 7e7d09c36fdd6575d88fffadec02a02128554c60ef37c89ab464d0c2ae6070c6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Default Plan target to the enclosing Scope Unit

## Scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of decomposition **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.

## Details
