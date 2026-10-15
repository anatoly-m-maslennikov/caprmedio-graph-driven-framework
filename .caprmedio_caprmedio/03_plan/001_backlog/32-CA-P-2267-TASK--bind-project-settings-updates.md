---
atom_id: CA-P-2267
content_role: Plan
type: Plan
label: Task
work_sequence_number: 32
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
version: 2
updated_at: "2026-10-13 02:48:47 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2269, CA-P-2275]
---
# Summary

Bind Project Settings updates

## Objective

The Project Settings Workflow uses the shared TOML connector with its distinct schema.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Split concrete work larger than this bound into actual bounded children before execution. This Backlog Task is current pending work, not a future-Version Scope or authorization to execute now.

After CA-P-2280, bind CA-O-206/220/210 to the actual Project Settings schema, exact selected items/full sets and expected state. The Read Step calls CA-O-218; the patch Step calls CA-O-204. Use the complete observed Read result and source state for proposal validation and Modify preconditions. A failed, incomplete or stale Read prevents patch dispatch. Preserve unrelated settings and truthful schema/postcondition/no-op behavior. Do not reuse Project Structure validation as Settings acceptance or add transport, database or retry configuration.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
