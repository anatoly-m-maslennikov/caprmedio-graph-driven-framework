---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History
  depends_on: []
version: 22
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
atom_id: CA-D-329
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Proof Frontier References

## Scope

proof Carrier dependency-frontier serialization.

## Claim

**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.

## Details
