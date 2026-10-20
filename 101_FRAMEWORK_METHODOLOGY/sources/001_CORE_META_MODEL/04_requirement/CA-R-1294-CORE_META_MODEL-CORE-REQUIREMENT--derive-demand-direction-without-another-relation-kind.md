---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Atom.Owning Scope Unit", "Entity/Node/Continuant/Atom.Target Scope Unit"]
version: 20
updated_at: "2026-10-19 15:52:46 +0400"
relations: {}
atom_id: "CA-R-1294"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Derive Demand Direction without Another Relation Kind

## Scope

Demand Atom directions.

## Claim

a Demand Atom **must not** introduce a graph Relation Kind for its direction because its Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit references determine that direction.

## Details
