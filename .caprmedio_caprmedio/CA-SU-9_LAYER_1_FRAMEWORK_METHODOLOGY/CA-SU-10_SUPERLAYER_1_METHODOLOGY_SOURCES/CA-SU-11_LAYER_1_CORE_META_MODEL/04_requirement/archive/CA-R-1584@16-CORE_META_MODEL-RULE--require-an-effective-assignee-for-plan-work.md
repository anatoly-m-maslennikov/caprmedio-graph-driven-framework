---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Assignee'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/Actor
version: 16
updated_at: 2026-10-24 12:35:51 +0400
relations:
  relates_to:
  - CA-R-1575
atom_id: CA-R-1584@16
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
