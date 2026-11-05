---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
version: 27
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-D-329
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-329-CORE_META_MODEL-ENG_DECISION--serialize-proof-frontier-references.md
  source_atom_id: CA-D-329
  source_atom_revision: 27
  source_sha256: b00323af4927500e97c4d1e510a4d918fd68f7f4f6e7c480f88b1ceec5309872
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Proof Frontier References

## Claim

### Prose Claim


proof Carrier dependency-frontier serialization.


**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.
