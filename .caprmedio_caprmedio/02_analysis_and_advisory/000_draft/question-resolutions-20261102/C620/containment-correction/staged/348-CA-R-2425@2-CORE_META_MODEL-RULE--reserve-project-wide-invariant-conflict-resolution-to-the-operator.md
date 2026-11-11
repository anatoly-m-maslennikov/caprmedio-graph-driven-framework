---
subjects:
  active: Actor
  passive:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
  - Project
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1058
atom_id: CA-R-2425@2
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Requirement
form: Rule
---
## Summary

Reserve Project-wide invariant conflict resolution to the Operator

## Claim scope

conflicts between active Project-wide foundational invariants **and** an AI Agent's delegated conflict resolution.

## Claim

- **only** an Operator **may** resolve a conflict between active Project-wide foundational invariants, **and** an Operator's decision to resolve that conflict is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for a conflict between active Project-wide foundational invariants but **must not** choose a resolution for a conflict between active Project-wide foundational invariants.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project-wide foundational invariants **only** **when** the AI Agent's active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.
