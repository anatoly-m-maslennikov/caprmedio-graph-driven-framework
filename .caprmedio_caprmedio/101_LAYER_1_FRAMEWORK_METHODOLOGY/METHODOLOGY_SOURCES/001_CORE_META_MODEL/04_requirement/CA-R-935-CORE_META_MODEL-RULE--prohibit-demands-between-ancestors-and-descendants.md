---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
version: 31
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-932
atom_id: CA-R-935
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
