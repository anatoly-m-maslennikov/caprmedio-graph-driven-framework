---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Status: Done'
version: 19
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1592
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Keep Plan completion prerequisites acyclic

## Scope

Plan execution.

## Claim

Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete directly contained Plan work **before** its containing Plan can be Done **or** Canceled.

## Details
