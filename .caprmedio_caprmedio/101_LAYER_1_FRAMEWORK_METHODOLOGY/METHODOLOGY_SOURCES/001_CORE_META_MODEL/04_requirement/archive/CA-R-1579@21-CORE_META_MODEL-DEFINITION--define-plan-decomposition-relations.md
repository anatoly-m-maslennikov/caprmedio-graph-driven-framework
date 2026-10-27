---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Label'
  - Subject/Graph Relation/Type
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Status'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 21
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1579@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Plan decomposition Relations

## Scope

Plan-decomposition Relations in the Plan Graph.

## Claim

**in** the Plan Graph, `A DECOMPOSES_INTO B` **means** that completing Plan `B` contributes required work **to** completing Plan `A`; `B IS_DECOMPOSITION_OF A` is the inverse view of the same fact.

- the source **and** target are distinct Plan Atoms, independently of their Labels.
- decomposition is an all-of relation: **all** decomposed Plans are required for completion under CA-R-1583.
- decomposition concerns planned work, **not** Claim containment, Scope Unit parentage, **or** Type inheritance.
- the decomposing Plan owns the direct `IS_DECOMPOSITION_OF` declaration under CA-D-481; derive `DECOMPOSES_INTO` from that same fact, **not** from folder placement.

## Details

### relation admission

- owning graph kind: Plan Graph under CA-R-1593; endpoints are Plan Atom references **in** that graph, **not** native nodes of a different graph.
- Status: the Relation Kind is Active; endpoint Plan Revisions use the admitted Plan Status model, **without** requiring every historical **or** pending endpoint **to** be Active.
- authority effect: retain the existing endpoint identities, Claims, Scope Units, **and** tiers; this Relation does **not** transfer authority.
- cardinality: **`<=1`** authored `IS_DECOMPOSITION_OF` target **and** **`>=0`** derived `DECOMPOSES_INTO` targets per Plan.
- transitivity: the direct Relation is **not** transitively materialized; recursive reachability is derived under CA-R-1537.
