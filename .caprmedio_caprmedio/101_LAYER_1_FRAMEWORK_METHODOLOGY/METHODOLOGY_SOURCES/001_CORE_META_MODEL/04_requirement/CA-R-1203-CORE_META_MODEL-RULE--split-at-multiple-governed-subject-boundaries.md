---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: GOVERNS'
  - Subject
  - Subject/CAPRMEDIO/Graph/Node
version: 28
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1203
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Split at Multiple Governed Subject Boundaries

## Scope

an Atom Claim governing canonical Entities through GOVERNS Subject Relations.

## Claim

an Atom **must** be split **if** its Claim governs **`>1`** canonical Entities through GOVERNS Subject Relations.

## Details
