---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent.Permissions'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Concern'
version: 17
updated_at: 2026-10-27 19:59:57 +0400
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
