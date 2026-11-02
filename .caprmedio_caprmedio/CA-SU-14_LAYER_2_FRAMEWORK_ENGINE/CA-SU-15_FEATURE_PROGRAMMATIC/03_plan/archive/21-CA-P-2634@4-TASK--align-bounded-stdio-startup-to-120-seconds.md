---
atom_id: CA-P-2634@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 4
updated_at: 2026-10-24 06:04:43 +0400
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2613
  depends_on:
  - CA-P-2633
  relates_to:
  - CA-C-587
  - CA-M-410
  - CA-P-2633
tier: 3
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

The assigned worker aligned the bounded test startup/readiness boundary to
120 seconds in the working tree while leaving the production Gateway's
90-second budget unchanged. Five focused hot-reload readiness/telemetry checks
passed in 20.556 seconds; the related 12 stdio/telemetry checks passed in
117.937 seconds under CA-P-2633. Ruff, strict Mypy and the AST-diff check
passed, and the independent reviewer returned PASS after the RMED header
correction. This Task is Done for the bounded test alignment and focused
verification. The production Gateway, live binding, runtime image, release
and deployment remain unchanged; the sanitized ValueError/source-drift
hypothesis remains unproven.
