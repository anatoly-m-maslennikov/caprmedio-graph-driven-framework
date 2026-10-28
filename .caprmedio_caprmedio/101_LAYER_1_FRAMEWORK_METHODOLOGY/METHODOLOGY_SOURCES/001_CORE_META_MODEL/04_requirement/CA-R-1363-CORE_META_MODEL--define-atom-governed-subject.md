---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Governed Subject
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: GOVERNS'
  - Subject
  - Subject/CAPRMEDIO/Graph/Relation/Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
version: 24
updated_at: 2026-10-27 19:59:53 +0400
relations:
  child_of:
  - CA-R-1269
  - CA-R-1199
  - CA-R-2100
  - CA-R-1202
atom_id: CA-R-1363
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
---
# Summary

Define Atom Governed Subject

## Scope

an Atom's governed Subject relation.

## Claim

an Atom Governed Subject **means** the Atom's optional **`0..1`** Subject Relation whose Relation Kind is GOVERNS. when present, its target is the canonical Subject Target governed by the Atom's role/Type-specific Content or operative formal rule; the Relation **and** its target are distinct.

## Details
