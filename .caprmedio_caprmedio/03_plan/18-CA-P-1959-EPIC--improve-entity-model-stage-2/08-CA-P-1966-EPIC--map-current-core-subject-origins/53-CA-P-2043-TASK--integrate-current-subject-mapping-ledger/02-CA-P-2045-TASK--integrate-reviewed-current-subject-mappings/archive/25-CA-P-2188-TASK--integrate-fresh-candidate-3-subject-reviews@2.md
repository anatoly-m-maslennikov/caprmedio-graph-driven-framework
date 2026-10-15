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
version: 2
updated_at: "2026-10-12 16:31:39 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  blocks: [CA-P-2189]
---
# Summary

Integrate fresh Candidate-3 Subject reviews

## Objective

Persist one fresh occurrence ledger from independently accepted current per-source reviews.

## Details

Estimated own work: 15 minutes for one integration AI Agent, assuming existing deterministic ledger mechanics. Required inputs: CA-P-2187 and CA-P-2193 Done, with every current source-packet Plan and its bounded review/assembly descendants complete, independent semantic receipts for reviewed meanings and actual accepted-content/coverage checks for assembly. Pin the current inventory, Candidate #3, [base Operator decisions](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/operator-subject-decisions.md), SHA-256 `ce28c370232ae43829036714eb24957987d11453fd94a76c4794997b088ecfb5`, additive [compact scope-reference decision](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/scope-reference-decision.md), SHA-256 `df2303d0128ca9b882e2877f41ebc2f17f2c9fc2ce4a3a7ffefa394000d249c0` and [approved content-conflict exclusions](../../../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc`, with complete disjoint source ownership. Old CA-P-2050–2056 domains or matching historical bytes are not those reviews.

Root owns the single derived ledger under `.caprmedio_tmp/stage2-migration-20261012/review/`. Cover every source/occurrence once, including supported, unchanged, unresolved and excluded/finding records, with source-specific governs/dependency meaning and preserved qualifiers. Keep below-90% mappings unadopted and unstaged until the Operator answers. Preserve raw reports and source bytes. Deliver the persisted ledger/hash, coverage reconciliation and exact remaining questions to CA-P-2189; do not infer graph acceptance or live approval. Split a concrete overrun before execution.

Reconcile all 907 owners and 4534 occurrences. A confirmed content conflict records a whole-Atom staging exclusion, its ID/Version/source hash, contradictory source and candidate/Operator evidence, reason and explicit CA-P-1970 queue entry. Excluded originals remain byte-unchanged and visible as unmigrated in inventory/graph coverage; do not stage even a supported subset of that owner. Mark eligible only independently accepted, fully supported whole-owner Subject changes. Missing coverage, uncertainty or weak evidence must not be relabeled as content conflicts; their existing investigation/Operator gates remain. No partial unreviewed set completes this ledger.

### Definition of Done

Not Done if a fresh batch/independent receipt is missing, a pin or model binding is stale, coverage overlaps/omits an occurrence, uncertainty is silently resolved or mislabeled as a content conflict, an exclusion lacks exact whole-owner evidence/preservation or its CA-P-1970 queue, old approval is reused, source/content bytes change or own work exceeds 15 minutes without decomposition.
