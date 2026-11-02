---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project.Structure
  - Default Settings
  - Subject/Domain/Node/Continuant/Project.Settings.Project Name
  - Subject/Domain/Node/Continuant/Project.Settings.Atom Prefix
  - Subject/Domain/Node/Continuant/Atom
version: 29
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1740
atom_id: CA-R-1750@29
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
