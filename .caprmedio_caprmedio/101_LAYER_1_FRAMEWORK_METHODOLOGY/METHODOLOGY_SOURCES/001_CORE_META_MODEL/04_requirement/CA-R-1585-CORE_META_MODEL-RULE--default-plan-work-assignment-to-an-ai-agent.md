---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
version: 19
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1585
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Default Plan work assignment to an AI Agent

## Scope

a Plan Atom with its own work and no explicit Assignee.

## Claim

**if** a Plan Atom has its own work **and** no explicit Assignee, **then** its effective Assignee **must** be **=1** AI Agent selected **to** execute that work.

## Details
