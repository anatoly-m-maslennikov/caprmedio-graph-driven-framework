---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Concern'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Engineering/AI Agent Delegation
  - Subject/Graph Node/Engineering/Confidence Threshold
  - Subject/Graph Node/Engineering/Autonomous Confidence Threshold
version: 19
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-R-846
  - CA-R-2158
  relates_to:
  - CA-R-1058
  - CA-R-815
  - CA-R-1552
atom_id: CA-R-1561@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Let AI Agents resolve Concerns under bounded authority

## Scope

AI Agent resolution of Concerns under active delegated authority.

## Claim

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.

## Details
