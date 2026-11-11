---
atom_id: CA-P-2558
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 2
updated_at: "2026-10-21T18:43:51Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2557]
  relates_to: [CA-M-396, CA-M-397, CA-M-398, CA-M-399, CA-M-400]
---
# Summary

Implement shared failure classifier and decorator

## Objective

Build one transport-neutral sync/async boundary with explicit failure classification, caller-owned response adapters, and existing diagnostic logging. Python RuntimeError alone must not mean blocking runtime failure. Preserve cancellation, metadata and caller result/effect ownership.

## Details

One Task per file. After completion, review and update dependant Tasks before their execution. Actual business Workflow lifecycle recording remains with its declared executor; this Task does not invent it in an error decorator.

### Definition of Done

Focused semantic/function tests cover ordinary success, request failures, explicit blocking runtime failures, logging failure and cancellation. At most 15 minutes own work; split further if required.
