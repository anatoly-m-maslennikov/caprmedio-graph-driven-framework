---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
version: 32
updated_at: 2026-10-29 07:17:21 +0400
relations:
  child_of:
  - CA-R-932
atom_id: CA-R-935@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Rule
---
# Summary
Prohibit Demands between ancestors and descendants

## Scope

Demand Atoms.

## Claim

a Demand Atom's Claim Target Scope Unit **must not** be an ancestor **or** descendant of its Consumer Scope Unit.

## Details
