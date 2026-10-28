---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Concern'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
version: 22
updated_at: 2026-10-27 19:59:57 +0400
relations:
  child_of:
  - CA-R-846
  - CA-R-2158
atom_id: CA-R-1561
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
