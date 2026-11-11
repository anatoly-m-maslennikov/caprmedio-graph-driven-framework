---
atom_id: CA-P-2389
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, "Atom/Status", Journal, Workflow, Operator]
version: 1
updated_at: "2026-10-15 22:53:45 +0400"
relations:
  is_decomposition_of: [CA-P-2385]
---
# Summary

Verify Status operations without history or Journal

## Objective

The previously blocked manual-Draft case and supported Status paths pass without history/Journal admission. Journal failure is distinct from mutation success; ordinary safety cases remain correct. No fabricated history/Journal, automatic replay or weakened target validation is used.

## Details

Use focused integration/functional tests with real temporary Atom carriers and actual adapters. Cover direct non-Draft creation, supported Status values/transitions, manual Draft promotion without retained history, missing/empty/incomplete Journal, append failure after a successful mutation, no-op and existing singular/bulk behavior. Retain invalid-schema, collision, stale-source, permission and truthful partial-batch refusal cases. Prefer boundary tests over implementation-coupled unit tests.

Estimated own work: at most 15 minutes; split further before execution if needed. After completion, review/update the next dependent task. A blocked leaf is postponed with a truthful Problem/Question Concern as appropriate; independent ready work continues.

## Definition of Done

The previously blocked manual-Draft case and supported Status paths pass without history/Journal admission. Journal failure is distinct from mutation success; ordinary safety cases remain correct. No fabricated history/Journal, automatic replay or weakened target validation is used.
