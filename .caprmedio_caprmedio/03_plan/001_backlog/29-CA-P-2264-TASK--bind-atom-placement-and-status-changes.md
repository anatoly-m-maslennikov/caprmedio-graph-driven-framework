---
atom_id: CA-P-2264
content_role: Plan
type: Plan
label: Task
work_sequence_number: 29
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Backlog
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Action, Workflow, Configuration, Revision, Journal, Plan, Operator]
version: 1
updated_at: "2026-10-13 00:21:20 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2269, CA-P-2276]
---
# Summary

Bind Atom placement and Status changes

## Objective

Atom placement and allowed Status changes use their actual semantic lifecycle adapters.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Split concrete work larger than this bound into actual bounded children before execution. This Backlog Task is current pending work, not a future-Version Scope or authorization to execute now.

Adapt CA-R-867/CA-M-187 placement separately from generic carrier move. Enforce actual role-specific Status/backlog/archive rules using existing CA-O-029/066/045 where applicable, not a hidden Active-only policy. Every actual same-ID change, including Status, has Version +1 and actual time; exact no-op preserves both. No Atom deletion or Summary/Type same-ID edit is admitted.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
