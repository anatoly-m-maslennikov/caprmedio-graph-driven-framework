---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 16
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1536@16
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
