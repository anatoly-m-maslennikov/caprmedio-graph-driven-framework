---
atom_id: CA-P-2272
content_role: Plan
type: Plan
label: Task
work_sequence_number: 37
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
version: 3
updated_at: "2026-10-13 05:09:14 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2278]
---
# Summary

Use explicit graph Delivery bindings

## Objective

Graph delivery paths derive from declared bindings rather than reconstructed folder names.

## Details

Initial bounded implementation: up to 15 minutes, authorized by the Operator's continuation after accepted source review. Any larger remaining work requires bounded decomposition before execution.

Use actual Project Structure Implementation Folder/Delivery bindings for both new FEATURE groups and unchanged legacy units. Remove the affected derivation assumption only; verify different authority/delivery naming and preserved old rows. This does not remap Subjects, generate migration outputs or infer native relations/runtime readiness.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Earlier Delivery-only checkpoint

Explicit Delivery binding and terminal-slash compatibility passed bounded independent checks (20 focused tests plus independent invalid/alias controls). At that checkpoint, live graph discovery still inferred topology from folder names and failed on the legacy 201 prefix. CA-P-2302–2304 separately repair and verify that existing R1070/M149/E295 obligation; the delivery-only receipt does not accept the broader repair.

### Bounded acceptance and remaining gate

The [bounded independent graph receipt](../../../_projection/core-entity-review/stage2/tools-first/declaration-graph-acceptance.md) accepts the topology/observation implementation and exact pins: 30 tests passed and the current read-only declaration probe returned 29 Scope Units. The shared cross-Project path guard remains incomplete, so complete invalid-declaration refusal is not yet accepted and this Task stays Active. Settings revision resolution also blocks full graph/runtime readiness. No publication is authorized by the bounded receipt.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
