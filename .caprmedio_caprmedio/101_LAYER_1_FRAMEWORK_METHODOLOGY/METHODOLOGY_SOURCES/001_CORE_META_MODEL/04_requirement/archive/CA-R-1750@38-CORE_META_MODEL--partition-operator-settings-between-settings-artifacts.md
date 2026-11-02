---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Governing Objects/Governing Configuration
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Prefix
  - Entity/Object/Continuant/Governing Objects/Atom
version: 38
updated_at: 2026-10-30 17:19:52 +0400
relations: {}
atom_id: CA-R-1750@38
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Partition Operator Settings Between Settings Artifacts

## Claim scope

Operator-selected settings and their authoritative Settings Artifacts.

## Claim

an Operator-selected setting **must** have **`=1`** authoritative owner: Project Settings for Project initialization inputs, including Project Settings Name **and** Project Settings Prefix; Framework Instance Settings for CAPRMEDIO behavior, configuration choices, **and** Authority Mode defaults; **or** Project Structure for an explicit per-Scope-Unit Authority Mode override. Atoms define permitted parameters, constraints, **and** applicability **without** fixing **or** duplicating current selected values **or** Default Settings values. definitions **and** storage rules for Project Settings Name **and** Project Settings Prefix belong **to** CORE_META_MODEL.

### Current source pin

Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1750-CORE_META_MODEL--partition-operator-settings-between-settings-artifacts.md`, CA-R-1750@37, SHA-256 `a9222939e3847db6a2c5da16b55122c4108b4f467d8609452dc581088ea9d77c`. Current bytes remain unchanged; this Draft performs no promotion or runtime change.
