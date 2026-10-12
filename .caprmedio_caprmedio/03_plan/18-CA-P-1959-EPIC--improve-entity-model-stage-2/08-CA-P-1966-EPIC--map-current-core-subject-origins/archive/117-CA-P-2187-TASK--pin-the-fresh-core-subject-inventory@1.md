---
atom_id: CA-P-2187
content_role: Plan
type: Plan
label: Task
work_sequence_number: 117
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
  is_decomposition_of: [CA-P-1966]
  blocks: [CA-P-2188, CA-P-2189]
---
# Summary

Pin the fresh Core Subject inventory

## Objective

Produce an independently checked current Core Subject frontier for fresh Candidate-3 review.

## Details

Estimated own work: 15 minutes for one AI Agent, assuming mechanical capture/pin checks on the existing bounded source tree. Reuse `.caprmedio_tmp/stage2-migration-20261012/inventory/current-subjects.inventory.json` and its preserved source-byte snapshots; the current producer reports 907 sources, 4534 occurrences and zero errors, not an accepted semantic review. Independently check source paths/owners/roles, current non-archived eligibility, identities, every governs/depends_on span, source hashes and excluded/finding coverage. All selected sources currently being Active is an observation, not an eligibility rule.

Bind the current project structure, Candidate #3 and latest decision context without importing old pins as approval. Deliver the exact inventory/hash and independent capture-verification receipt in the inventory directory. No source, history, Journal, Tool or content write. Read-only model/check preparation may proceed in parallel; semantic source Plan IDs wait for the actual disjoint partition list. Split a concrete overrun rather than claim incomplete coverage.

### Definition of Done

Not Done if current coverage/pins or independent capture verification is incomplete/stale, eligibility is silently Active-only, findings/exclusions are hidden, old semantic acceptance is inherited, authoritative bytes change or own work exceeds 15 minutes without decomposition.
