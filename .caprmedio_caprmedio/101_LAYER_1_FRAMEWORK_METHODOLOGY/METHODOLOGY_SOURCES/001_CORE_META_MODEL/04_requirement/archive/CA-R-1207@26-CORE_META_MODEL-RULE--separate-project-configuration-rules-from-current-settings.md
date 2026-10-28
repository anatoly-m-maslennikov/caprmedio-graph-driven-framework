---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Selection//Extension Sources
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
version: 26
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1207@26
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Separate Project Configuration Rules from Current Settings

## Scope

Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.

## Claim

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.

## Details
