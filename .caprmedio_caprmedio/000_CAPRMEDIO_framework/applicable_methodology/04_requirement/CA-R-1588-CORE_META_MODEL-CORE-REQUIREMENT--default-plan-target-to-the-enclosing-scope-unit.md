---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Atom.Target Scope Unit", "Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Atom/Content Role: Plan.Label"]
version: 10
updated_at: "2026-10-18 03:33:43 +0400"
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
  source_atom_revision: 10
  source_sha256: 59e5a44e737e1a4f806deae516d35c1f3a5c05ea35fa623ddbf8d3fe182a5213
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Default Plan target to the enclosing Scope Unit

## Scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of decomposition **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.

## Details
