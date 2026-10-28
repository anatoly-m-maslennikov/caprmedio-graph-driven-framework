---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Extension Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//CORE_META_MODEL
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
version: 28
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1218
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Project Configuration

## Scope

Project-owned Methodology Source authority that expands the Core Meta-Model.

## Claim

Project Configuration **means** Project-owned Methodology Source authority whose prerequisite Methodology Source is the Core Meta-Model and that expands the Core Meta-Model with Project-specific rules, constraints, **and** defaults **without** replacing CORE_META_MODEL authority at **any** numeric Tier **or** duplicating current values owned by Settings Artifacts. For governing RMED endpoint ordering, this definition declares exactly the directed logical-role prerequisite Project Configuration → Core Meta-Model. It declares no reverse **or** transitive prerequisite and no prerequisite for the Project root, the Methodology Sources owner, an Extension, **or** a descendant Scope Unit.

## Details
