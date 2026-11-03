---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//DEPENDS_ON
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  - CAPRMEDIO <+ MODEL <+ Term//Artifact
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)/(.Type: Plan)'
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
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-239-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-dependency-order-from-explicit-edges.md
  source_atom_id: CA-M-239
  source_atom_revision: 25
  source_sha256: 2f8ecb0b406dffcd04bfe3c3503abad28c9f3729a67611b206119bacfc50d413
  original_relations_sha256: 85c1b9412646ac53fdf3c60e22c880cb205339611c160bb327d3f477942c6f6e
---
## Summary

Derive Dependency Order from Explicit Edges

## Claim scope

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
