---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//depends_on
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan)/(.Header.Form: Plan)'
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-120
atom_id: CA-M-239
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Method
form: Implementation Method
---
## Summary

Derive Dependency Order from Explicit Edges

## Claim

### Prose Claim


non-Plan Artifact dependency order derivation from explicit edges.


**to** derive one non-Plan Artifact dependency order, the resolver **must**:

1. construct one directed graph from direct `relations.depends_on` edges from **every** dependent Artifact **to** **every** prerequisite Artifact;
2. derive its `required_by` inverse view **without** authoring inverse edges;
3. calculate one deterministic prerequisite-first topological order with canonical identity **only** as a tie-breaker; **and**
4. reject a cycle.

the resolver **must not** use target-list position, Local Order, **or** `relations.derived_from` as a dependency edge.

## Details

Plan readiness follows `BLOCKS` under CA-R-1580: **all** blockers **must** be Done, **and** independent ready Plans **may** execute concurrently subject **to** their permissions; navigation order **must not** add blocking.
