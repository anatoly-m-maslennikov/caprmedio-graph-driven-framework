---
atom_id: CA-P-2336
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Configuration, Workflow, Plan]
version: 1
updated_at: "2026-10-13 20:49:49 +0400"
relations:
  is_decomposition_of: [CA-P-2318]
---
# Summary

Preserve single Atom Status bundles

## Objective

One identified Atom Status change preserves its exact predecessor and moves its matching Directory Carrier with the current carrier without changing descendants.

## Details

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git; workers own disjoint implementation/test files and preserve other workers' edits. Inherit accepted parent RMEDO and independent review gates.

Repair the actual single-target lifecycle publisher using existing helpers and current O127/O129/O128, D461/D463/D467, R1432/R1788 and M372. Keep local nested P/O placement, canonical archive version suffix and exact predecessor bytes; changed target gets Version +1 and actual time, unchanged descendants do not. Seal/recheck source and destination carrier sets, collision refusal, observed results and bounded own-action recovery. No global batch rollback, retries or new publication-concurrency policy. Audit move/archive/update/revert callers before editing; isolate status-specific behavior when shared behavior differs. Draft identity admission and multi-Run composition remain separate. Test nested P/O, parent directory, historical bytes, no-op, collisions, stale inputs and fault cases. If this does not fit 15 minutes, return a precise remaining split before more work.

### Definition of Done

The outcome has exact current source/code/test evidence, actual positive/refusal checks and independent acceptance. Preparation, isolated helpers or source acceptance do not establish live/runtime completion. No unapproved policy, weakened guard, live Core migration or deferred capability is included.
