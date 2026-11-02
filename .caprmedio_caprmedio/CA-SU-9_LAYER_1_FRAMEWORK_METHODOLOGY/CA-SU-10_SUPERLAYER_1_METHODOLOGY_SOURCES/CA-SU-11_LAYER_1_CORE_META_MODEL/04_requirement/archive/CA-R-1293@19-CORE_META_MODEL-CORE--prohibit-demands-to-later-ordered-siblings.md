---
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit.Local Order
  - 'Entity/Node/Continuant/Scope Unit/Type: Ordered'
version: 19
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1293@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Prohibit Demands to Later Ordered Siblings

## Scope

Demand Atoms owned by Ordered Scope Units.

## Claim

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.

## Details
