---
atom_id: CA-P-2634
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 2
updated_at: "2026-10-23T13:29:12+0400"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2613]
  depends_on: [CA-P-2633]
  relates_to: [CA-C-587, CA-M-410, CA-P-2633]
---
# Summary

Align bounded stdio startup to 120 seconds

## Objective

Align the disposable MCP test harness with its measured cold-start and
readiness budget without changing the production Gateway budget.

## Details

This is one bounded Task with at most 15 minutes of own work and depends on
the verified CA-P-2633 harness refactor. The exclusive test boundary is
102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/naked_mcp_smoke.py and
its bounded support helper. Set the test startup/discovery/read timeout to the
existing 120-second disposable-harness boundary where needed, preserving
request/result assertions and no-live-project isolation. Leave
204_MCP/hot_reload.py and its 90-second production generation-ready budget
unchanged. Keep the sanitized ValueError/source-drift hypothesis separate from
this budget repair.

## Definition of Done

Run the focused cold-start and related MCP tests after the refactor, with
Ruff and strict Mypy for changed sources. Report measured startup, discovery
and result times, failures and partial results. Do not run the full suite,
live MCP, release, deployment or image replacement.

## Execution checkpoint — 23 October 2026

The assigned worker has aligned the bounded test startup/readiness boundary to
120 seconds in the working tree, while leaving the production Gateway's
90-second budget unchanged. Focused checks are still running; independent
review must first accept CA-P-2633 and then validate this alignment before this
Task can become Done. Keep this Task Active and do not treat the working-tree
change as live admission, release or deployment evidence.
