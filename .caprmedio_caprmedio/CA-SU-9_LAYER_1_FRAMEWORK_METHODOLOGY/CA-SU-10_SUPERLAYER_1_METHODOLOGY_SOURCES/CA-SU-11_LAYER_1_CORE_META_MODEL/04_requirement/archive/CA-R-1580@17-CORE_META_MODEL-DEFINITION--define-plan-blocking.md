---
subjects:
  governs: 'Subject/Graph Relation/Type: BLOCKS'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Status: Done'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Relation/Type: DEPENDS_ON'
version: 17
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1580@17
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Plan blocking

## Scope

Plan-blocking Relations in the Plan Graph.

## Claim

**in** the Plan Graph, `A BLOCKS B` **means** that Plan `B` **may** start **only** **after** Plan `A` is Done.

- a Plan **may** block **>=0** other Plans **and** have **>=0** blockers.
- **all** blockers **must** be Done **before** the blocked work starts.
- navigation order, a shared Hub, **and** `DECOMPOSES_INTO` do **not** establish `BLOCKS`.
- an inverse lookup is derived from the same explicit fact, **not** separately authored; Subject DEPENDS_ON remains a different Relation Kind.

## Details

### relation admission

- owning graph kind: Plan Graph under CA-R-1593; endpoints are Plan Atom references **in** that graph, **not** native nodes of a different graph.
- Status: the Relation Kind is Active; endpoint Plan Revisions use the admitted Plan Status model, **without** requiring every historical **or** pending endpoint **to** be Active.
- authority effect: retain the existing endpoint identities, Claims, Scope Units, **and** tiers; this Relation does **not** transfer authority.
- cardinality: **>=0** distinct direct targets **and** **>=0** distinct incoming blockers; inverse direction is blocked Plan **to** blocker.
- transitivity: retain **only** explicit direct edges; prerequisite reachability **may** be derived for readiness **and** cycle checks **without** creating authored transitive edges.
