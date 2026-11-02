---
subjects:
  governs: Entity
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity
  - Entity
  - Entity/Object/Continuant/Term
  - Entity/Graph Syntax > Relation
version: 28
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1275@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Subject

## Claim scope

Things or topics an Atom governs or depends on.

## Claim

a Subject names the thing or topic an Atom governs or depends on.

## Details

- GOVERNS and DEPENDS_ON are separate connected relations. Each relation connects an Atom to a target in the Subject graph.
- a Subject names the target; it is not the relation, an intermediate Subject object, or a copied target. A target may be a classification axis or another topic without being a separate entity kind.
- the set of Subjects forms a graph, and a full canonical Subject path names a target in that graph.
- `Subject/CAPRMEDIO/...` names shared framework vocabulary. `Subject/<Project Name>/...` names project-specific concepts. The namespace is part of the full logical canonical path; it is not an entity kind or a Scope Unit.
- an Atom's owning Scope Unit does not determine its Subject namespace. Choose the namespace from the meaning being addressed, not from the Atom's owner, folder or Carrier.
