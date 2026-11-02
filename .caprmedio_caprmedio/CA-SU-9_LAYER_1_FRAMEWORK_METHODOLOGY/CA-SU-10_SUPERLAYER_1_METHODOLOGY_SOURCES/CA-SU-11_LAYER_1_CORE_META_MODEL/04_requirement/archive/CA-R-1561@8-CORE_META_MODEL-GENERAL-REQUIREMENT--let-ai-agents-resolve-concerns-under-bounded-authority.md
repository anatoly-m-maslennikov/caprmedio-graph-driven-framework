---
subjects:
  governs: 'Entity/Node/Continuant/Actor/Type: AI Agent'
  depends_on:
  - 'Entity/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Concern'
  - Subject/Domain/Node/Continuant/Atom
  - 'Entity/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - AI Agent Delegation
  - AI Agent Confidence
  - Autonomous Confidence Threshold
version: 8
updated_at: 2026-10-23 03:06:32 +0400
relations: {"child_of":["CA-R-846","CA-P-034"],"relates_to":["CA-R-1058","CA-R-815","CA-R-846","CA-R-1552"]}
atom_id: CA-R-1561@8
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Let AI Agents resolve Concerns under bounded authority

## Scope

AI Agent resolution of Concerns under active delegated authority.

## Claim

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.

## Details
