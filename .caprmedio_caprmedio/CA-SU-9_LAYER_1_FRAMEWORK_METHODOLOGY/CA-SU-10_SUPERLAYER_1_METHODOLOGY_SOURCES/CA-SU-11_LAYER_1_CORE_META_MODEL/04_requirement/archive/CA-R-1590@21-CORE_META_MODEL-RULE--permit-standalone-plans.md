---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom
version: 21
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1590@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Permit standalone Plans

## Claim scope

Plan Atoms.

## Claim

a Plan Atom **may** exist **without** an `IS_CONTAINED_BY` connection to a containing Plan; its Label **must not** require a containing Plan.
