---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
version: 17
updated_at: 2026-10-27 19:59:57 +0400
relations: {}
atom_id: CA-R-1554
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Bound Scripted Migrations

## Scope

AI Agent participation in Scripted Migrations.

## Claim

an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.

## Details
