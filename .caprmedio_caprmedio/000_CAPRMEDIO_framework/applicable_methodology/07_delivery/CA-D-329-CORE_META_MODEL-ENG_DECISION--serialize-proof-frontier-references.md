---
atom_id: CA-D-329
ref_id: CA-D-329
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
tier: 3
status: Active
version: 27
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-D-329-CORE_META_MODEL-DECISION--serialize-proof-frontier-references.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-329-CORE_META_MODEL-ENG_DECISION--serialize-proof-frontier-references.md
  source_atom_id: CA-D-329
  source_atom_revision: 27
  source_sha256: 32c00987c1cf538ce973d647b2d455409685afd5ef32d98b5bec0fbc160ef6f7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Proof Frontier References

## Claim

### Prose Claim


proof Carrier dependency-frontier serialization.


**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.
