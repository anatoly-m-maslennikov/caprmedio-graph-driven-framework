---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity
  - Entity/Term
  - Entity/Graph Syntax <+ Relation
version: 31
updated_at: 2026-10-30 16:15:53 +0400
relations: {}
atom_id: CA-R-1275@31
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define Subject

## Claim scope

Things or topics an Atom governs or depends on.

## Claim


An Atom.Subjects target must name the thing or topic the Atom governs or depends on; it is not a copied target, intermediate Subject object, or a requirement for a separate entity kind.

## Details

- GOVERNS and DEPENDS_ON are separate connected relations. Each relation connects an Atom to a target in the Subject graph.
- a Subject names the target; it is not the relation, an intermediate Subject object, or a copied target. A target may be a classification axis or another topic without being a separate entity kind.
- the set of Subjects forms a graph, and a full canonical Subject path names a target in that graph.
- Entity is the canonical expression root. Its direct branches follow the governing Entity Definition in CA-R-1248; this Rule does not enumerate a closed branch set. Object specializes into Continuant and Occurrent. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.
- An Atom's Local Scope Unit does not determine its Subject. Name the governed thing or topic rather than copying that Scope Unit.
