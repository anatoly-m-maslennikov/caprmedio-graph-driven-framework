---
atom_id: CA-M-239
ref_id: CA-M-239
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//depends_on
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan)/(.Header.Form: Plan)'
tier: 4
relations:
  child_of:
  - CA-M-120
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-239-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-dependency-order-from-explicit-edges.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-239-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-dependency-order-from-explicit-edges.md
  source_atom_id: CA-M-239
  source_atom_revision: 25
  source_sha256: dc128f7a8a2b3ad285cabacd0dad9b5447234215a19a0dbe15325d0ee2368db2
  original_relations_sha256: 85c1b9412646ac53fdf3c60e22c880cb205339611c160bb327d3f477942c6f6e
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
