---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom
version: 15
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1574
  - CA-R-1579
atom_id: CA-R-1590@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Permit standalone Plans

## Scope

Plan Atoms.

## Claim

a Plan Atom **may** exist **without** an incoming `DECOMPOSES_INTO` Relation; its Label **must not** require a containing Plan.

## Details
