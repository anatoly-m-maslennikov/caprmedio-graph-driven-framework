---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Local Order
  - 'Subject/Graph Node/Domain/Continuant/Scope Unit/Type: Ordered'
version: 23
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1293
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Prohibit Demands to Later Ordered Siblings

## Scope

Demand Atoms owned by Ordered Scope Units.

## Claim

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.

## Details
