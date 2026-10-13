---
atom_id: CA-P-2256
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Action, Workflow, Configuration, Revision, Journal, Plan, Operator]
version: 2
updated_at: "2026-10-13 04:30:00 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2266, CA-P-2267, CA-P-2269, CA-P-2275]
---
# Summary

Implement TOML item and full-set edits

## Objective

The shared TOML connector performs accepted add, replace and remove edits with truthful results.

## Details

Initial bounded implementation: up to 15 minutes. The Operator authorized continuation after accepted RMEDO/FPF prerequisites. Remaining work is decomposed below before the next bounded phase; the parent remains Active until its complete original Definition of Done is met.

Implement one shared connector for item/value and full-set add/replace/remove, explicit target/current-state and exact no-op. Preserve unrelated TOML meanings and reject malformed or ambiguous input safely. Do not substitute this connector for Project Structure or Project Settings Workflow schema checks; those adapters remain distinct.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Bounded continuation

The initial private mechanics are implemented or in progress; this is not accepted receiving/runtime capability. Continue through [CA-P-2297 — Bind TOML modifications to receiving schemas](21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/01-CA-P-2297-TASK--bind-toml-modifications-to-receiving-schemas.md). This child is limited to 15 minutes and must be split again before larger work. Remaining publication, receiving Workflow and independent portfolio gates are unchanged.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
