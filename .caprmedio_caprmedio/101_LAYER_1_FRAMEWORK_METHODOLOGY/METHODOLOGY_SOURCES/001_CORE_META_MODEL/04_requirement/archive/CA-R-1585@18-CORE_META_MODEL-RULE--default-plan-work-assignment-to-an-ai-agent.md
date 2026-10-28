---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
version: 18
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1585@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
