---
atom_id: CA-M-135
ref_id: CA-M-135
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
tier: 3
status: Active
version: 32
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-135-CORE_META_MODEL-IMPLEMENTATION_METHOD--exclude-generated-only-implementation-edges.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-135-CORE_META_MODEL-IMPLEMENTATION_METHOD--exclude-generated-only-implementation-edges.md
  source_atom_id: CA-M-135
  source_atom_revision: 32
  source_sha256: 7cc6465d10c801c2f48657e6378fe4c961ababb0c3a3469eea65d4b901eaff80
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Exclude generated-only implementation edges

## Claim

### Prose Claim


provenance validation of recorded changes in the governed selection.


provenance validation inspects **every** recorded change **in** the governed selection. a change contributes an Implementation Relation, implementation coverage, **or** semantic traceability edge **only** **when** it changes **`>=1`** non-generated governed source.

an update **only** **to** generated Projections remains an auditable refresh. it retains its required Journal provenance but cannot become an implementation input **to** the semantic graph that produced the generated Carrier. a mixed change participates **only** through its substantive non-generated governed source changes.
