---
atom_id: CA-P-2564
ref_id: CA-P-2564
container:
  atom: CA-P-2562
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Runtime Failure Classification
tier: 3
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
status: Backlog
version: 4
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2564-TASK--apply-shared-errors-to-all-tool-execution-owners.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/94-CA-P-2562-TASK--cover-all-docker-image-execution-boundaries/001_backlog
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Apply shared errors to all Tool execution owners

## Objective

Wire missing canonical Tool execution boundaries used by direct and Docker/MCP calls. Preserve caller schemas, verified partials, target safety and atomicity; input/artifact failures are WARNING plus explicit output errors. Do not blindly skip an invalid explicit mutation target.

## Details

One Task per file. Each leaf has at most 15 minutes own work; decompose before extending it. Review and update dependants after each predecessor's observed result. Use only broken/related checks, configured Project Temporary State and the selected virtual environment. No production mutation or full-suite run.

### Definition of Done

Focused public Tool checks cover each affected dispatch class and representative previously uncovered adapters; no guessed prefix, silent failure, hidden retry or Journal writes.
