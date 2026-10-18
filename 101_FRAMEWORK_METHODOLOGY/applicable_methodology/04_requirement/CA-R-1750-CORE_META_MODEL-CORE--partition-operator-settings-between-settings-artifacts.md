---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings"
  depends_on:
    ["Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Project.Settings", "Entity/Continuant/Object/Project.Structure", "Default Settings", "Project Name", "Entity/Continuant/Object/Project.Settings.Atom Prefix", "Entity/Continuant/Object/Atom"]
version: 23
updated_at: "2026-10-15 18:45:44 +0000"
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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1750-CORE_META_MODEL-CORE--partition-operator-settings-between-settings-artifacts.md
  source_atom_id: CA-R-1750
  source_atom_revision: 23
  source_sha256: 57c636884b0f47b243d54871de567d5744762a80212bd5d255cd2782116090e5
  original_relations_sha256: 4e823082688e17e42d7889dacdc356b5f8822d57bcf2f4501c09225f60722871
---
# Summary

Partition Operator Settings Between Settings Artifacts

## Scope

Operator-selected settings and their authoritative Settings Artifacts.

## Claim

an Operator-selected setting **must** have **`=1`** authoritative owner: Project Settings for Project initialization inputs, including Project Name **and** Project Atom prefix; Framework Instance Settings for CAPRMEDIO behavior, configuration choices, **and** Authority Mode defaults; **or** Project Structure for an explicit per-Scope-Unit Authority Mode override. Atoms define permitted parameters, constraints, **and** applicability **without** fixing **or** duplicating current selected values **or** Default Settings values. definitions **and** storage rules for Project Name **and** Project Atom prefix belong **to** CORE_META_MODEL.

## Details
