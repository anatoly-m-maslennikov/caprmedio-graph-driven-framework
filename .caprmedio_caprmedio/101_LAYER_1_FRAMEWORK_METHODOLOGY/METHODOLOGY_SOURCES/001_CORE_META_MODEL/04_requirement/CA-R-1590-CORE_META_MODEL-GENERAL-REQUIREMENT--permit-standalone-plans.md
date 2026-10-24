---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Atom
version: 11
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1574
  - CA-R-1579
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

a Plan Atom **may** exist **without** an incoming `DECOMPOSES_INTO` Relation; its Label **must not** require a containing Plan.

## Details
