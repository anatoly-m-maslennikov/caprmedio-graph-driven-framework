---
subjects:
  governs: Subject/Domain/Node/Continuant/Actor
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom.Tier: Principle'
  - Subject/Engineering/AI Agent Delegation
  - Subject/Engineering/Autonomous Confidence Threshold
version: 15
updated_at: 2026-10-24 20:51:15 +0400
relations:
  child_of:
  - CA-R-1058
atom_id: CA-R-1551@15
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
