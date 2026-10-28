---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//CORE_META_MODEL
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
version: 17
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1466
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Keep Git integration in an Extension

## Scope

Git integration in the Core Meta-Model.

## Claim

Git integration **must** be optional Extension authority, **not** a prerequisite of the Core Meta-Model. Git commit policies, commit-message encodings, hooks, **and** event-to-commit references belong **to** that Extension; selecting it **must not** replace the authoritative Journal **or** make Git history an independent source for the same recorded facts. the Core Meta-Model **must** remain applicable **without** Git integration.

## Details
