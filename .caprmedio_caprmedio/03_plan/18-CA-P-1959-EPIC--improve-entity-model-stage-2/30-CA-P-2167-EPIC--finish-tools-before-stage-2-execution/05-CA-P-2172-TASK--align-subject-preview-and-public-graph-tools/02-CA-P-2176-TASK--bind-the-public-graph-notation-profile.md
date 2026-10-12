---
atom_id: CA-P-2176
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Subject, Entity, Projection, Plan]
version: 1
updated_at: "2026-10-12 04:02:18 +0400"
relations:
  is_decomposition_of: [CA-P-2172]
  blocks: [CA-P-2174]
---
# Summary

Bind the public graph notation profile

## Objective

The existing public graph entry point uses an explicit approved profile under the accepted contracts.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-2169 and its actual current public graph contract packet independently accepted under CA-P-2171. Other contract packets need not be complete. Reopen public graph callers/exports/fixtures and bind the affected entry-point files. Own public profile forwarding/validation and its focused tests; reuse the internal reviewed parser and coordinate shared files with integration.

Apply the smallest change that carries and validates the selected approved profile through the existing path. Check approved compact/selector forms, `Atom`/`atom` case, unsupported/absent explicit selection, legacy/default behavior, pins and provenance. Do not add native Relations or infer meanings from candidate display paths. Deliver code/test pins and actual results to CA-P-2174. Split larger work before execution. No production graph or Core source change occurs.

### Definition of Done

The Plan is **not** Done if contract acceptance is missing/stale, a caller silently uses the wrong profile, legacy/case/source semantics regress, native admission is inferred, focused checks fail, or own work exceeds 15 minutes without decomposition.
