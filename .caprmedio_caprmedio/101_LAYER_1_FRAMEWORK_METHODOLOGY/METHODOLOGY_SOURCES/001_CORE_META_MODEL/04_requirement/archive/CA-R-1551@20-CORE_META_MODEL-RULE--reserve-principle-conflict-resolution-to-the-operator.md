---
subjects:
  governs: Entity/Object/Continuant/Actor
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Principle Universe
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
version: 20
updated_at: 2026-10-29 07:17:17 +0400
relations:
  child_of:
  - CA-R-1058
atom_id: CA-R-1551@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
