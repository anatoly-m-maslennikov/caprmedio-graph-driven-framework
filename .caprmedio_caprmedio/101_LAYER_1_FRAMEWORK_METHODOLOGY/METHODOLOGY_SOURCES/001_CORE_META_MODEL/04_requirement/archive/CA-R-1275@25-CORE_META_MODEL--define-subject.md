---
subjects:
  governs: Subject
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node
  - Subject
  - Subject/Graph Node/Domain/Continuant/Term
  - Subject/Graph Relation
version: 25
updated_at: 2026-10-26 05:25:17 +0400
relations: {}
atom_id: CA-R-1275@25
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Subject

## Scope

Things or topics an Atom governs or depends on.

## Claim

a Subject names the thing or topic an Atom governs or depends on.

## Details

- GOVERNS and DEPENDS_ON are separate connected relations. Each relation connects an Atom to a node in the Subject graph.
- a Subject names the target; it is not the relation, an intermediate Subject object, or a copied target.
- the set of Subjects forms a graph, and a canonical Subject path names a target in that graph.
