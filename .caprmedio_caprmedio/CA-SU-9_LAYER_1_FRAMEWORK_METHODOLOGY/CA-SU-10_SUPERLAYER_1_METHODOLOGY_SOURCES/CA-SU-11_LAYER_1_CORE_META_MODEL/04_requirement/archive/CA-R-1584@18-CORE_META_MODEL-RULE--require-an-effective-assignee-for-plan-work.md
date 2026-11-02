---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - Subject/Graph Node/Domain/Continuant/Actor
version: 18
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1584@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
