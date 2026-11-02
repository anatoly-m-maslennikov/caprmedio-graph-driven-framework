---
atom_id: CA-P-2559
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 1
updated_at: "2026-10-21T18:41:35Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2557]
  depends_on: [CA-P-2558]
  relates_to: [CA-M-396, CA-M-397, CA-M-398, CA-M-399, CA-M-400]
---
# Summary

Integrate canonical Tool and MCP error boundaries

## Objective

Reuse the shared boundary at existing canonical public execution owners, including descriptor Tools and selected MCP routes where applicable. Preserve their different governed response schemas; reject invalid requests without disabling a healthy service. Apply once and keep registration/discovery effect-free.

## Details

One Task per file. After completion, review and update dependant Tasks before their execution. Actual business Workflow lifecycle recording remains with its declared executor; this Task does not invent it in an error decorator.

### Definition of Done

Focused public execution tests show WARNING plus request errors, runtime-only ERROR, no exception-message leakage, preserved sync/async results and no implicit Journal or retry. At most 15 minutes own work.
