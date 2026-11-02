---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 13
updated_at: 2026-10-24 10:48:25 +0400
relations:
  relates_to:
  - CA-R-1576
  - CA-R-1579
  - CA-R-1590
atom_id: CA-R-1536@13
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Restrict Direct Plan Decomposition

## Scope

direct `DECOMPOSES_INTO` relations between Plan Atoms.

## Claim

`DECOMPOSES_INTO` **must** connect **only** distinct Plan Atoms; **any** Plan **may** decompose into other Plans regardless of their Labels, **without** requiring incoming decomposition.

## Details
