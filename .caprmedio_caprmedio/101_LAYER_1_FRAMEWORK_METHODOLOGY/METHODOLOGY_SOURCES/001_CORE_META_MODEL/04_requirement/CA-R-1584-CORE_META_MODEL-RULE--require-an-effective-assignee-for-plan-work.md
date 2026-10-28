---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Actor
version: 19
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1584
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Require an effective Assignee for Plan work

## Scope

Plan Atoms with their own work content, excluding pure Hubs **without** their own work.

## Claim

**every** Plan Atom with its own work content **must** have **`=1`** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.

## Details
