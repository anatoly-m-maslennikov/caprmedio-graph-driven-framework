---
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings"
  depends_on:
    ["Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Project.Settings", "Entity/Node/Continuant/Project.Structure", "Default Settings", "Project Name", "Entity/Node/Continuant/Project.Settings.Atom Prefix", "Entity/Node/Continuant/Atom"]
version: 24
updated_at: "2026-10-19 15:53:58 +0400"
relations:
  relates_to:
    - "CA-R-1740"
atom_id: "CA-R-1750"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Partition Operator Settings Between Settings Artifacts

## Scope

Operator-selected settings and their authoritative Settings Artifacts.

## Claim

an Operator-selected setting **must** have **`=1`** authoritative owner: Project Settings for Project initialization inputs, including Project Name **and** Project Atom prefix; Framework Instance Settings for CAPRMEDIO behavior, configuration choices, **and** Authority Mode defaults; **or** Project Structure for an explicit per-Scope-Unit Authority Mode override. Atoms define permitted parameters, constraints, **and** applicability **without** fixing **or** duplicating current selected values **or** Default Settings values. definitions **and** storage rules for Project Name **and** Project Atom prefix belong **to** CORE_META_MODEL.

## Details
