---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Actor
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Principle Universe
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
version: 19
updated_at: 2026-10-27 19:59:57 +0400
relations:
  child_of:
  - CA-R-1058
atom_id: CA-R-1551
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Reserve Principle-conflict resolution to the Operator

## Scope

conflicts between active Project Principles **and** an AI Agent's delegated conflict resolution.

## Claim

- **only** an Operator **may** resolve a conflict between active Project Principles, **and** an Operator's decision to resolve that conflict is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for a conflict between active Project Principles but **must not** choose a resolution for a conflict between active Project Principles.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project Principles **only** **when** the AI Agent's active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.

## Details
