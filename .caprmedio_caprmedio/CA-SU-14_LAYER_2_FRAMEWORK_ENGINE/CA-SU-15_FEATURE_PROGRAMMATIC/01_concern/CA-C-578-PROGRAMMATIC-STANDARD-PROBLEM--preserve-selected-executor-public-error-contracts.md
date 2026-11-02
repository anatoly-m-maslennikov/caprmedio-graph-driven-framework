---
atom_id: CA-C-578
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2590, CA-P-2595]
version: 1
updated_at: "2026-10-22T12:01:02Z"
---
# Summary

Preserve selected executor public error contracts

## Concern

Source review of the unaccepted <=200-line SelectedExecution facade found that extraction no longer re-exported LifecycleAdmissionError. The real MCP selected_route_request.preflight_lifecycle consumer still raises and catches selected_execution.LifecycleAdmissionError when the source-derived preview admission is absent or stale. Removing that public error binding can turn a structured blocked result into an AttributeError. Strict typing alone did not expose the dynamic-module consumer.

This is an introduced local refactor finding, not a deployed incident. Restoring a public binding to the single canonical error class is compatibility, not a second behavioral owner or an imported-method facade.

## Resolution

The integration restored the canonical LifecycleAdmissionError import and explicit public export. The public executor remains exactly 200 formatted physical lines without a source-size exception.

The retained MCP test test_selected_executor_exports.py calls the real preflight_lifecycle consumer with a bounded adapter stub and patched source observation. It verifies that missing preview admission returns blocked disposition/outcome, empty effect references and lifecycle_error.code=status-preview-admission-missing. The new regression passed, and all 21 existing selected-route MCP checks passed. The new test also passed strict Mypy and pinned Ruff format/lint/C901.

## Evidence boundary

Only the identified compatibility finding is Resolved. Complete public executor/Subject-batch integration and refactor acceptance remain under CA-P-2590 and CA-P-2595. No live Atoms, Docker, ports, production state, release or deployment were used by the consumer regression. The separate current-session continuation gap CA-C-576 remains Active.
