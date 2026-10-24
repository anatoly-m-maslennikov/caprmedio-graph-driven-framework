---
atom_id: CA-P-2257
content_role: Plan
type: Plan
label: Task
work_sequence_number: 22
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
version: 5
updated_at: "2026-10-23 23:03:23 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2259, CA-P-2263, CA-P-2264, CA-P-2269, CA-P-2274]
---
# Summary

Implement scalar and value-based property edits

## Objective

Property edits support explicit scalar and list-value/full-set operations without index selectors.

## Details

Initial bounded implementation: up to 15 minutes. The Operator authorized continuation after accepted RMEDO/FPF prerequisites. Remaining work is decomposed below before the next bounded phase; the parent remains Active until its complete original Definition of Done is met.

Implement accepted CA-R-1934/CA-M-374 refinements, including add/remove and exact expected current values. A single list item is selected by VALUE, never position; duplicate/ambiguous values fail safely. Reject same-ID Summary or Type changes and preserve unrelated fields. Retain exact currentness, actual changed Version +1/time and no-op Version/time preservation.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Bounded continuation

The initial private mechanics are implemented or in progress; this is not accepted receiving/runtime capability. Continue through [CA-P-2298 — Preserve carrier bytes during property edits](22-CA-P-2257-TASK--implement-scalar-and-value-based-property-edits/done/01-CA-P-2298-TASK--preserve-carrier-bytes-during-property-edits.md). This child is limited to 15 minutes and must be split again before larger work. Remaining publication, receiving Workflow and independent portfolio gates are unchanged.

### Pure-transform completion checkpoint

CA-P-2298 and its CA-P-2305/2306 children are Done after [independent pure-transform acceptance](../../_projection/core-entity-review/stage2/tools-first/property-carrier-acceptance.md) at code commit `f4f4c6ce6`: 46 focused Property tests and 162 connector tests pass. This parent remains Active because receiving Workflow, lifecycle metadata/history, publication and independent portfolio/runtime gates are not completed by a pure helper. Its original Objective and Definition of Done remain unchanged.

### Shared Update metadata/history continuation

Continue the existing shared lifecycle_intents Update path through [CA-P-2361 — Fix shared current Atom Update Version and history](22-CA-P-2257-TASK--implement-scalar-and-value-based-property-edits/02-CA-P-2361-TASK--fix-shared-current-atom-update-version-and-history.md) and [CA-P-2362 — Verify shared current Atom Update Version and history](22-CA-P-2257-TASK--implement-scalar-and-value-based-property-edits/03-CA-P-2362-TASK--verify-shared-current-atom-update-version-and-history.md). Each child is bounded to 15 minutes and requires splitting before larger work. Current CA-R-1432 v11 requires Version +1 for every real same-ID update, exact predecessor preservation and unchanged no-op metadata; this continuation fixes and independently checks that shared behavior for admitted identified non-Draft current Atoms, needed by Property and Section integration. Existing authorization, classification and rollback gates remain unchanged. Draft updates/promotion/identity, legacy migration, renderer redesign, public routes and live effects are not authorized; report any Draft/legacy policy contradiction separately. The parent remains Active with its original Objective and Definition of Done, including broader receiving/publication/runtime gates.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
