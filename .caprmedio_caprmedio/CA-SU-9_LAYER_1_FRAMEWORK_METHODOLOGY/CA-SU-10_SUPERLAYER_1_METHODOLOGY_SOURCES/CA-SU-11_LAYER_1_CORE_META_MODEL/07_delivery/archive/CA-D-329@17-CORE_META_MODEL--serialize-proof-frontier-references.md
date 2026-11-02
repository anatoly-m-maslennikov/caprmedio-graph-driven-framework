---
subjects:
  governs: Entity/Node/Continuant/History
  depends_on: []
version: 17
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-D-329@17
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Proof Frontier References

## Scope

proof Carrier dependency-frontier serialization.

## Claim

**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.

## Details
