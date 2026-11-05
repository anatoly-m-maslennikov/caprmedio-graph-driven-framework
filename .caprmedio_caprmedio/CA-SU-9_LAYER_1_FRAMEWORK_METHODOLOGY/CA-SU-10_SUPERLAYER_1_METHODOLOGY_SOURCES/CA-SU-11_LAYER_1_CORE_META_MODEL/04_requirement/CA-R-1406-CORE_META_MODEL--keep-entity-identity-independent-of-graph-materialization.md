---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Projection
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2462
atom_id: CA-R-1406
ref_id: CA-R-1406
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1406-CORE_META_MODEL-RULE--keep-entity-identity-independent-of-graph-materialization.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Keep Entity Identity Independent of Graph Materialization

## Claim

### Prose Claim


Entity identity while a Graph Projection is materialized, refreshed, or deleted.


materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
