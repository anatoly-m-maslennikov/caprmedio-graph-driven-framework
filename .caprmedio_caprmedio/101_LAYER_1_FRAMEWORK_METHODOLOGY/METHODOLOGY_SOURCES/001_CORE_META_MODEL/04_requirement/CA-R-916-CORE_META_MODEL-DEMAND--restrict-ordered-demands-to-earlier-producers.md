---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
version: 31
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-932
atom_id: CA-R-916
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 5
type: Demand
---
# Summary
Restrict ordered Demands to earlier Producers

## Scope

Demand Atoms whose Consumer Atom Scope Unit and Producer Claim Target Scope Unit are ordered siblings.

## Claim

**if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.

## Details
