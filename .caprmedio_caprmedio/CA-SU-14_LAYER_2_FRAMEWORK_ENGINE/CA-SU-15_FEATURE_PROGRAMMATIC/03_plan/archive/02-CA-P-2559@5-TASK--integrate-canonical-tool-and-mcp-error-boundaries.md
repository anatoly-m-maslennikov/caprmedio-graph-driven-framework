---
atom_id: CA-P-2559@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 5
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/Runtime Failure Classification
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2557
  depends_on:
  - CA-P-2558
  relates_to:
  - CA-M-396
  - CA-M-397
  - CA-M-398
  - CA-M-399
  - CA-M-400
tier: 3
---
# Summary

Integrate canonical Tool and MCP error boundaries

## Objective

Reuse the shared boundary at existing canonical public execution owners, including descriptor Tools and selected MCP routes where applicable. Preserve their different governed response schemas; reject invalid requests without disabling a healthy service. Apply once and keep registration/discovery effect-free.

## Details

One Task per file. After completion, review and update dependant Tasks before their execution. Actual business Workflow lifecycle recording remains with its declared executor; this Task does not invent it in an error decorator.

### Definition of Done

Focused public execution tests show WARNING plus request errors, runtime-only ERROR, no exception-message leakage, preserved sync/async results and no implicit Journal or retry. At most 15 minutes own work.

### Execution checkpoint

Integrated the shared boundary into registered Tool execution, selected MCP exception boundaries, workflow_orchestrator and the canonical Atom CLI. Existing public response schemas and provider-owned partial results are preserved. Missing logger/sink and missing implementation support remain observable; technical messages omit raw exception text/details. The MCP portfolio passed 53 cases in 22.254 seconds. The final related 32-case rerun passed and independent review approved. Missing shared implementation support remains WARNING unless its actual runtime owner explicitly classifies a blocking failure; no speculative runtime classification, retry or Journal emission was added. Source acceptance only; production is unchanged.
