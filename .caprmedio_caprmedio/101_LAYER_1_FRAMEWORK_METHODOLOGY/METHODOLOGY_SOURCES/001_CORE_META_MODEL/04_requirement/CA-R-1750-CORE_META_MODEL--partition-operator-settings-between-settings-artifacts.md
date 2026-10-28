---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Project Name
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Atom Prefix
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 34
updated_at: 2026-10-27 20:00:02 +0400
relations: {}
atom_id: CA-R-1750
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Partition Operator Settings Between Settings Artifacts

## Scope

Operator-selected settings and their authoritative Settings Artifacts.

## Claim

an Operator-selected setting **must** have **`=1`** authoritative owner: Project Settings for Project initialization inputs, including Project Name **and** Project Atom prefix; Framework Instance Settings for CAPRMEDIO behavior, configuration choices, **and** Authority Mode defaults; **or** Project Structure for an explicit per-Scope-Unit Authority Mode override. Atoms define permitted parameters, constraints, **and** applicability **without** fixing **or** duplicating current selected values **or** Default Settings values. definitions **and** storage rules for Project Name **and** Project Atom prefix belong **to** CORE_META_MODEL.

## Details
