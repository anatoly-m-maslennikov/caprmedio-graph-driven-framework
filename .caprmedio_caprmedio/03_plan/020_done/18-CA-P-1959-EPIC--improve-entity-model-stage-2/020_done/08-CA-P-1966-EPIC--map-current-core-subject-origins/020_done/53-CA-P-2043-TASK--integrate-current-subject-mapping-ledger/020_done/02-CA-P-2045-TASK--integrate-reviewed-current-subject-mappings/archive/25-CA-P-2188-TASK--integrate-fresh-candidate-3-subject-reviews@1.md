---
atom_id: CA-P-2188
content_role: Plan
type: Plan
label: Task
work_sequence_number: 25
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject
  depends_on: [Atom, Entity, Projection, Plan, Tool, Operator]
version: 1
updated_at: "2026-10-12 14:55:39 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  blocks: [CA-P-2189]
---
# Summary

Integrate fresh Candidate-3 Subject reviews

## Objective

Persist one fresh occurrence ledger from independently accepted current per-source reviews.

## Details

Estimated own work: 15 minutes for one integration AI Agent, assuming existing deterministic ledger mechanics. Required inputs: CA-P-2187 Done and every newly assigned semantic source-batch Task Done with an independent acceptance receipt. Pin the current inventory, model/decision context and complete disjoint source ownership. Old CA-P-2050–2056 domains or matching historical bytes are not those reviews.

Root owns the single derived ledger under `.caprmedio_tmp/stage2-migration-20261012/review/`. Cover every source/occurrence once, including supported, unchanged, unresolved and excluded/finding records, with source-specific governs/dependency meaning and preserved qualifiers. Keep below-90% mappings unadopted and unstaged until the Operator answers. Preserve raw reports and source bytes. Deliver the persisted ledger/hash, coverage reconciliation and exact remaining questions to CA-P-2189; do not infer graph acceptance or live approval. Split a concrete overrun before execution.

### Definition of Done

Not Done if a fresh batch/independent receipt is missing, a pin or model binding is stale, coverage overlaps/omits an occurrence, uncertainty is silently resolved, old approval is reused, source/content bytes change or own work exceeds 15 minutes without decomposition.
