---
atom_id: CA-P-2564@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 3
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/Runtime Failure Classification
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2562
  depends_on:
  - CA-P-2563
  relates_to:
  - CA-M-396
  - CA-M-397
  - CA-M-398
  - CA-M-399
  - CA-M-400
tier: 3
---
# Summary

Apply shared errors to all Tool execution owners

## Objective

Wire missing canonical Tool execution boundaries used by direct and Docker/MCP calls. Preserve caller schemas, verified partials, target safety and atomicity; input/artifact failures are WARNING plus explicit output errors. Do not blindly skip an invalid explicit mutation target.

## Details

One Task per file. Each leaf has at most 15 minutes own work; decompose before extending it. Review and update dependants after each predecessor's observed result. Use only broken/related checks, configured Project Temporary State and the selected virtual environment. No production mutation or full-suite run.

### Definition of Done

Focused public Tool checks cover each affected dispatch class and representative previously uncovered adapters; no guessed prefix, silent failure, hidden retry or Journal writes.
