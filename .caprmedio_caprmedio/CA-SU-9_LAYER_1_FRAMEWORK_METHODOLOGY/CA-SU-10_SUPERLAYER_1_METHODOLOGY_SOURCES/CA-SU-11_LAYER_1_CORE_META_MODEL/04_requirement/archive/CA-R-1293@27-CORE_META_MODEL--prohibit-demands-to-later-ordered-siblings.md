---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Local Order
  - 'Entity/Object/Continuant/Structural Unit/Scope Unit/Type: Ordered'
version: 27
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1293@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Prohibit Demands to Later Ordered Siblings

## Claim scope

Demand Atoms owned by Ordered Scope Units.

## Claim

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.
