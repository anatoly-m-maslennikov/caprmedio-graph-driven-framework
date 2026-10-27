---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Substance
  depends_on:
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - Subject
  - Subject/Domain/Node
version: 23
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1203@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
