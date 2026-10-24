---
atom_id: CA-P-2270
content_role: Plan
type: Plan
label: Task
work_sequence_number: 35
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
updated_at: "2026-10-13 18:52:21 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2278]
---
# Summary

Refresh authority consumers and release admission

## Objective

Affected authority consumers and release/admission bindings use actual current rebuilt source pins.

## Details

Initial bounded implementation: up to 15 minutes, authorized by the Operator's continuation after accepted source review. Any larger remaining work requires bounded decomposition before execution.

Replace affected hardcoded authority assumptions with actual declared source ownership/delivery evidence. Refresh only approved release/admission bindings after complete independently accepted contracts and FPF review; preserve historical receipts and unrelated authority. Prove stale/old source pins fail safely and source acceptance is not runtime activation.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Current checkpoint

The registered-owner resolver passed bounded independent checks (11 focused tests and 11 independent assertions). Full Release admission remains unproven: CA-D-572 was deliberately archived without a current successor. Do not restore it or use historical/installed bytes as current authority. Source/consumer disposition remains separate from the accepted resolver change.

### Bounded continuation — 2026-10-13

[CA-P-2315 — Resolve graph authority from declared sources](35-CA-P-2270-TASK--refresh-authority-consumers-and-release-admission/01-CA-P-2315-TASK--resolve-graph-authority-from-declared-sources.md) repairs the graph-authority refresh consumer's obsolete source roots. Preserve the finite source-ID set, exact current source checks and stale-pin refusal. This does not authorize manifest-wide repinning or source migration. The Operator deferred legacy source migration again; the malformed legacy Concern and missing current CA-D-572 remain separate blockers. This parent stays Active.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
