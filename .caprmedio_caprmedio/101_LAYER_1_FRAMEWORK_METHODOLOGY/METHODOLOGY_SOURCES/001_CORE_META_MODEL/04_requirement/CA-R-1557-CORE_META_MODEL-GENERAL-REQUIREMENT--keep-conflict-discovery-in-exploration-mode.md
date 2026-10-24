---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Exploration Mode
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Concern'
version: 12
updated_at: 2026-10-24 01:37:42 +0400
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
