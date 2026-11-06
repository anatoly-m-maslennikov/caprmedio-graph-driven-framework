---
atom_id: CA-R-1406
ref_id: CA-R-1406
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Projection
tier: 2
relations:
  child_of:
  - CA-R-2462
status: Active
version: 26
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1406-CORE_META_MODEL-RULE--keep-entity-identity-independent-of-graph-materialization.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1406-CORE_META_MODEL--keep-entity-identity-independent-of-graph-materialization.md
  source_atom_id: CA-R-1406
  source_atom_revision: 26
  source_sha256: a14dcd1c86fb20de9cd904da851f6f57a02c703a26c86c130fd399c4fd2e0cb0
  original_relations_sha256: 2a0810d805fe1b1cdc72c6a1211185c800aacd85bdf16e0b8da6356339219483
---
## Summary

Keep Entity Identity Independent of Graph Materialization

## Claim

### Prose Claim


Entity identity while a Graph Projection is materialized, refreshed, or deleted.


materializing, refreshing, **or** deleting a Graph Projection **must not** establish, change, **or** remove Entity identity.
