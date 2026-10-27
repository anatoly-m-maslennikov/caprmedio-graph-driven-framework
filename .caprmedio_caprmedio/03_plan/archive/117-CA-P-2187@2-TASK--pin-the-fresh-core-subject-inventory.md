---
atom_id: CA-P-2187@2
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
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Atom
  - Entity
  - Projection
  - Plan
  - Tool
  - Operator
version: 2
updated_at: 2026-10-12 15:42:26 +0400
relations:
  is_decomposition_of:
  - CA-P-1966
  blocks:
  - CA-P-2188
  - CA-P-2189
---
# Summary

Pin the fresh Core Subject inventory

## Objective

Produce an independently checked current Core Subject frontier for fresh Candidate-3 review.

## Details

Estimated own work: 15 minutes for one AI Agent, assuming mechanical capture/pin checks on the existing bounded source tree. Reuse `.caprmedio_tmp/stage2-migration-20261012/inventory/current-subjects.inventory.json` and its preserved source-byte snapshots; the current producer reports 907 sources, 4534 occurrences and zero errors, not an accepted semantic review. Independently check source paths/owners/roles, current non-archived eligibility, identities, every governs/depends_on span, source hashes and excluded/finding coverage. All selected sources currently being Active is an observation, not an eligibility rule.

Bind the current project structure, Candidate #3 and latest decision context without importing old pins as approval. Deliver the exact inventory/hash and independent capture-verification receipt in the inventory directory. No source, history, Journal, Tool or content write. Read-only model/check preparation may proceed in parallel; semantic source Plan IDs wait for the actual disjoint partition list. Split a concrete overrun rather than claim incomplete coverage.

### Completion receipt

[Independent inventory check](../../../../../.caprmedio_tmp/stage2-migration-20261012/inventory-independent-check.json) passed for 907 sources and 4534 occurrences against inventory SHA-256 `0b2f217e8ebf541cc84322d18be81073bfdbb54342f248cbf9928583678455c7`. All four controls rejected dropped/duplicate occurrences, wrong source hashes and wrong Subjects. Root also rechecked all 12124 canonical Core/history hashes against the captured frontier: unchanged. No source writes occurred; all selected sources being Active remains an observation, not the eligibility rule.

This closes current capture/coverage only. Candidate-3 per-source semantic review, whole-ledger independent acceptance, staged export and graph review remain pending; historical meaning approval is not inherited.

### Definition of Done

Not Done if current coverage/pins or independent capture verification is incomplete/stale, eligibility is silently Active-only, findings/exclusions are hidden, old semantic acceptance is inherited, authoritative bytes change or own work exceeds 15 minutes without decomposition.
