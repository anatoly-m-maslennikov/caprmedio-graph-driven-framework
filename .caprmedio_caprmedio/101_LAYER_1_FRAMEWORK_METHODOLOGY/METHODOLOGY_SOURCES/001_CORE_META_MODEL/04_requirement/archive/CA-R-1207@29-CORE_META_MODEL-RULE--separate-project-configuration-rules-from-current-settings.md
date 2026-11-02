---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Selection//Extension Sources
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 29
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1207@29
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Separate Project Configuration Rules from Current Settings

## Claim scope

Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.

## Claim

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.

## Details
