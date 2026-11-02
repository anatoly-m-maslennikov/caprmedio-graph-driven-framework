---
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent
  depends_on:
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent.Permissions
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern'
version: 20
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-R-1702
atom_id: CA-R-1557@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Keep conflict discovery in Exploration Mode

## Claim scope

AI Agent discovery of conflicts in Exploration Mode.

## Claim

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.
