---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 18
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1590
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Permit standalone Plans

## Scope

Plan Atoms.

## Claim

a Plan Atom **may** exist **without** an `IS_CONTAINED_BY` connection to a containing Plan; its Label **must not** require a containing Plan.

## Details
