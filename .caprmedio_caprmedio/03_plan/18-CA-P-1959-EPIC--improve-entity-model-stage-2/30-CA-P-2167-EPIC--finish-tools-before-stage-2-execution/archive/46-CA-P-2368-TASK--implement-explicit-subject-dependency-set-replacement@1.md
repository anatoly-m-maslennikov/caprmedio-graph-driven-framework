---
atom_id: CA-P-2368
content_role: Plan
type: Plan
label: Task
work_sequence_number: 46
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 1
updated_at: "2026-10-14 05:52:57 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Implement explicit Subject dependency set replacement

## Objective

Implement the existing depends_on replace_set shape in the shared pure Subject planner and affected Describe/test surfaces. Compare the exact current collection, accept only explicit unique valid new Subjects, preserve unrelated bytes and comments or refuse unsupported forms, and keep governs scalar and generic duplicate refusal. Reuse the existing rendering and intent/materialization/staging paths; no implicit merging or live application.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns integration, Plans and Git. Workers use disjoint assigned files and preserve unrelated edits. This is necessary Subjects-only migration tooling; Core migration, ordinary content edits, legacy C/A repair, catalogs and unrelated connector work remain outside this Task.

### Definition of Done

Focused tests prove complete-set replacement, no-op, stale/duplicate/invalid-input refusal, LF/CRLF and unrelated-byte preservation, and consistent preview/intent/staging results. Independent code/tests verify the actual implementation. Existing selected apply integration is a separate gate, not waived.

