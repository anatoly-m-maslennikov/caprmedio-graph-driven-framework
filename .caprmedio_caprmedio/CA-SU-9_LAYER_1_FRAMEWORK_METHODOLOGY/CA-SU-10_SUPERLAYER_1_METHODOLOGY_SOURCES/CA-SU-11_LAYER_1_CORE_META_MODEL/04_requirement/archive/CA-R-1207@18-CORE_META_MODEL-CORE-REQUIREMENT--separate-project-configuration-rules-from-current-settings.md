---
subjects:
  governs: Project Configuration
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Extension
  - Subject/Domain/Node/Continuant/Project.Framework Settings
version: 18
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-R-1207@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Separate Project Configuration Rules from Current Settings

## Scope

Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.

## Claim

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.

## Details
