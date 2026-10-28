---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: depends_on'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: DEPENDS_ON'
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
version: 21
updated_at: 2026-10-27 19:59:41 +0400
relations:
  child_of:
  - CA-M-120
atom_id: CA-M-239
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
