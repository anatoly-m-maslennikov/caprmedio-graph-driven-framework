---
subjects:
  governs: Project Configuration
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Extension
  - Subject/Domain/Node/Continuant/Project.Framework Settings
version: 19
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1207@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Separate Project Configuration Rules from Current Settings

## Scope

Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.

## Claim

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.

## Details
