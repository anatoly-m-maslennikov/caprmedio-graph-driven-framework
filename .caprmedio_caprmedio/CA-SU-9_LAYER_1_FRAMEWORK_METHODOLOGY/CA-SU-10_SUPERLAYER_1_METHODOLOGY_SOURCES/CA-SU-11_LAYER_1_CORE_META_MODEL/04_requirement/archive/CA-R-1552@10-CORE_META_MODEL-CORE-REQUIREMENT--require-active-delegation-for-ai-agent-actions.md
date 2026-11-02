---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Entity/Node/Continuant/Actor/Type: AI Agent.Permissions'
version: 10
updated_at: 2026-10-23 03:14:50 +0400
relations:
  child_of:
  - CA-P-034
atom_id: CA-R-1552@10
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Require active delegation for AI Agent actions

## Scope

AI Agent actions under active Operator-issued delegation.

## Claim

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** **when** an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.

## Details
