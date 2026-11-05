---
atom_id: CA-P-1724
ref_id: CA-P-1724
role: Plan
form: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 9
updated_at: 2026-10-25 17:32:27 +0400
topics:
  main_subject: Subject/Graph Node/Engineering/Release
  dependencies:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Engineering/Methodology
  - Subject/Graph Node/Engineering/Manifest
  - Subject/Graph Node/Engineering/Release Testing/Executor Admission
relations:
  is_decomposition_of:
  - CA-P-1717
tier: 3
container:
  atom: CA-P-1717
carrier_destination:
  file:
    name: 4-CA-P-1724-TASK--implement-the-declared-release-suite-driver.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/3-CA-P-1623-TASK--implement-release-version-from-reviewed-rmed/5-CA-P-1643-TASK--integrate-release-actions-and-admission/27-CA-P-1717-TASK--isolate-the-release-suite-from-the-executing-runtime/done
---
# Summary

Implement the declared Release suite driver

## Objective

Implement the accepted complete-suite driver and maintained module-level probe rules.

## Details

Own only RELEASE_VERSION/run_release_suite.py and release_suite_bindings.json. Execute every declared testcase in fresh per-module children, attest exact sealed sources, emit one JUnit row per actual testcase, and fail closed for unavailable prerequisites. Reuse unittest and standard-library facilities. Expected bounded work: <=15 minutes; decompose if needed.

## Definition of Done

The driver satisfies the accepted RMED and deterministic E2E corpus without hidden exclusions or synthetic full-suite success.

## Results

The fixed CLI driver and maintained source-probe rules are saved in 689dd212f. Independent bounded review accepts exact per-testcase reporting, complete sealed-module discovery and truthful incomplete/non-pass states. Twelve golden cases pass; no actual complete Docker suite is claimed.
