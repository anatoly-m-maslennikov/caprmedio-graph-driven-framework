---
atom_id: CA-P-2330@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Method
  - Delivery
  - Plan
version: 3
updated_at: 2026-10-24 06:04:18 +0400
relations:
  is_decomposition_of:
  - CA-P-2307
tier: 3
---
# Summary

Remove redundant TOML rule Types

## Objective

Remove only the unsupported Type fields from CA-M-383 and CA-D-632, as explicitly approved by the Operator.

## Details

Estimated own work: up to 15 minutes. Their Content Roles remain Method and Delivery. Preserve exact predecessor archives, increment Version once and record actual Updated At. Preserve Summary, Subjects, relations and body. Refresh only affected current pins after independent comparison; keep historical receipts unchanged.

Independently review the exact two-header correction and rerun the same explicit PRMEDO finite diagnostic. C/A remains deferred. No validator exception, new Type, legacy fallback, configuration write, dependency implementation or whole-Project admission follows from this Task.

### Definition of Done

The Plan is not Done if the permitted diff or exact archives fail independent review, affected current pins are stale, scoped checks are not rerun, or remaining failures are hidden.

### Completed bounded outcome — 2026-10-13

The exact two Type-field removals and predecessor archives passed current independent comparison. Subsequent typed-relation changes have separate acceptance; no current production pin consumer requires another refresh.

Evidence: [bounded cleanup Task closure](../../../../../../_projection/core-entity-review/stage2/tools-first/bounded-cleanup-task-closure.md). Receiving integration, full-Project/runtime admission and deferred C/A migration remain separate.
