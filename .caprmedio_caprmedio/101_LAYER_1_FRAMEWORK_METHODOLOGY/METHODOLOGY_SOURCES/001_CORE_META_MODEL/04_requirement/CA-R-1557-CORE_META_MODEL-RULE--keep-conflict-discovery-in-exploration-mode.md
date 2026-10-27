---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent.Permissions'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Concern'
version: 16
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-R-1702
atom_id: CA-R-1557
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Keep conflict discovery in Exploration Mode

## Scope

AI Agent discovery of conflicts in Exploration Mode.

## Claim

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.

## Details
