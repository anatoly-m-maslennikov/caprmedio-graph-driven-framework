---
atom_id: CA-P-2633
content_role: Plan
type: Plan
label: Task
work_sequence_number: 20
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 1
updated_at: "2026-10-23T13:18:33+0400"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2613]
  depends_on: [CA-C-587]
  relates_to: [CA-C-587, CA-M-410, CA-P-2634]
---
# Summary

Refactor legacy stdio test harness before budget alignment

## Objective

Refactor the canonical legacy MCP stdio test harness into bounded, cohesive
fixture and helper responsibilities before changing its startup budget.

## Details

This is one bounded Task with at most 15 minutes of own work. The exclusive
source boundary is
102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_rmed_workflow_mcp.py
(currently 304 lines). Preserve its current functional assertions, discovery
and client behavior, and the production Gateway contract. Extract only the
cohesive seams needed for the later budget alignment; do not change timeout
values, production hot_reload.py, MCP bindings, runtime images or release
behavior in this Task.

## Definition of Done

Return the refactored canonical harness with small functions/modules, focused
behavioral parity checks, Ruff and strict Mypy results, and an explicit list
of any remaining startup-budget boundary. Do not run the full suite, live MCP,
release or deployment. CA-P-2634 may start only after this refactor is
verified.
