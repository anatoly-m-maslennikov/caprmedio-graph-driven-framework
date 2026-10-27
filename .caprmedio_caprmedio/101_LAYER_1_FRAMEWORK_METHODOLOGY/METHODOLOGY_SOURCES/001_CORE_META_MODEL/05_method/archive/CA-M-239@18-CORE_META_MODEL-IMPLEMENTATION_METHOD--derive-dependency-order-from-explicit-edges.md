---
subjects:
  governs: 'Subject/Graph/Relation/Type: depends_on'
  depends_on:
  - 'Subject/Graph/Relation/Type: DEPENDS_ON'
  - DERIVED_FROM
  - Subject/Graph/Relation
  - Subject/Domain/Node/Continuant/Term//Artifact
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
version: 18
updated_at: 2026-10-24 11:58:20 +0400
relations:
  child_of:
  - CA-M-120
atom_id: CA-M-239@18
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Implementation Method
---
# Summary

Derive Dependency Order from Explicit Edges

## Scope

non-Plan Artifact dependency order derivation from explicit edges.

## Claim

**to** derive one non-Plan Artifact dependency order, the resolver **must**:

1. construct one directed graph from direct `relations.depends_on` edges from **every** dependent Artifact **to** **every** prerequisite Artifact;
2. derive its `required_by` inverse view **without** authoring inverse edges;
3. calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker; **and**
4. reject a cycle.

the resolver **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge.

## Details

Plan readiness follows `BLOCKS` under CA-R-1580: **all** blockers **must** be Done, **and** independent ready Plans **may** execute concurrently subject **to** their permissions; navigation order **must not** add blocking.
