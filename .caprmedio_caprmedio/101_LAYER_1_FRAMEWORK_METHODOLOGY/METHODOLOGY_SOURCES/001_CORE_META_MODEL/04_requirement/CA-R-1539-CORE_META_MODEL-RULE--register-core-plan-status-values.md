---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Status'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status
version: 18
updated_at: 2026-10-27 19:59:57 +0400
relations: {}
atom_id: CA-R-1539
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Register Core Plan Status Values

## Scope

Core Plan Status values.

## Claim

the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

## Details
