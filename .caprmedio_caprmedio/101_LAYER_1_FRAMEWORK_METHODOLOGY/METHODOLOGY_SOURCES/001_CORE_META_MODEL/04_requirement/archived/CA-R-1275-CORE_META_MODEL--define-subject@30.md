---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity
  - Entity
  - Entity/Object/Continuant/Term
  - Entity/Graph Syntax > Relation
version: 30
updated_at: 2026-10-29 17:09:47 +0400
relations: {}
atom_id: CA-R-1275
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
- Entity is the canonical expression root. Its four sibling branches are Object, Aspect, Graph Syntax and Carrier under CA-R-1248. Object specializes into Continuant and Occurrent. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.
- An Atom's Local Scope Unit does not determine its Subject. Name the governed thing or topic rather than copying that Scope Unit.
