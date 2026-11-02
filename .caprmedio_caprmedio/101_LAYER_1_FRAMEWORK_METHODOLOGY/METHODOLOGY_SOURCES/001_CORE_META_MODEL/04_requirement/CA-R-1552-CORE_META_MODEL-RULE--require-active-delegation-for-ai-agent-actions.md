---
subjects:
  active: Entity/Object/Continuant/Actor/AI Agent
  passive:
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent.Permissions
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2158
atom_id: CA-R-1552
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Require active delegation for AI Agent actions

## Claim scope

AI Agent actions under active Operator-issued delegation.

## Claim

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** **when** an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.
