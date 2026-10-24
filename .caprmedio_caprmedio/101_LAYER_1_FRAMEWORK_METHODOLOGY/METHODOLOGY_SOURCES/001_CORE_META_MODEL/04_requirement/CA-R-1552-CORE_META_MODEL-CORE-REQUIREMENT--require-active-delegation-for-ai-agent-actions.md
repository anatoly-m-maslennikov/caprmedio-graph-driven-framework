---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent.Permissions'
version: 13
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-P-034
atom_id: CA-R-1552
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Require active delegation for AI Agent actions

## Scope

AI Agent actions under active Operator-issued delegation.

## Claim

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** **when** an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.

## Details
