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
---
## Summary

Serialize Proof Frontier References

## Claim scope

proof Carrier dependency-frontier serialization.

## Claim

**every** proof Carrier **must** serialize its machine-readable dependency frontier as a YAML `proof_frontier_refs` list of exact versioned **or** digest-bound references. prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.
