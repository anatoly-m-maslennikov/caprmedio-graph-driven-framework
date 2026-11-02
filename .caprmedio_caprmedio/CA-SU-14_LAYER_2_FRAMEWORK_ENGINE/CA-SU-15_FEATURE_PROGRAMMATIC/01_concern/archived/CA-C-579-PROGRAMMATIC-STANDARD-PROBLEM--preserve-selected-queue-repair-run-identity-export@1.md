---
atom_id: CA-C-579
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2590, CA-P-2595]
version: 1
updated_at: "2026-10-22T12:02:27Z"
---
# Summary

Preserve selected queue repair Run identity export

## Concern

Final independent source review of the unaccepted bounded SelectedExecution facade found that selected_queue_repair still imports RUN_ID from selected_execution, while extraction moved the canonical pattern into selected_execution_contracts without retaining the public binding. Queue-repair import would fail before its safety checks or execution. This is a compatibility regression in local refactoring, not a deployed incident.

## Required disposition

Preserve the existing public Run identity binding by re-exporting the one canonical pattern, without copying its value or adding a size exception. Retain the <=200 formatted physical-line bound, handler precedence, source-bound dispatch, no-replay behavior and the existing queue-repair validations. Run focused queue-repair/import checks and close the final independent compatibility review before CA-P-2590 or CA-P-2595 can complete.

## Evidence boundary

The missing symbol was found by read-only source/caller review. No production queue, Run, MCP service, release or deployment was exercised. The separate public LifecycleAdmissionError regression is resolved in CA-C-578 with a retained real-consumer test; its closure does not establish queue-repair compatibility.
