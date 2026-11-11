---
atom_id: CA-P-2330
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Method, Delivery, Plan]
version: 1
updated_at: "2026-10-13 19:35:59 +0400"
relations:
  is_decomposition_of: [CA-P-2307]
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
