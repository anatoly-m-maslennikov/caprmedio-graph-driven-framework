---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Assignee'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Actor
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1584
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Require an effective Assignee for Plan work

## Claim scope

Plan Atoms with their own work content, excluding pure Hubs **without** their own work.

## Claim

**every** Plan Atom with its own work content **must** have **`=1`** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.
