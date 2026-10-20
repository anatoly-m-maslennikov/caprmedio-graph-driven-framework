---
subjects:
  governs: "Entity/Node/Continuant/History"
  depends_on: []
version: 16
updated_at: "2026-10-19 15:55:29 +0400"
relations: {}
atom_id: "CA-D-329"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-329-CORE_META_MODEL--serialize-proof-frontier-references.md
  source_atom_id: CA-D-329
  source_atom_revision: 16
  source_sha256: c5ea03a4913955bd85bb49b866202ab27c199e1817ab080396ddf99a7e9ac4be
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Proof Frontier References

## Scope

proof Carrier dependency-frontier serialization.

## Claim

**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.

## Details
