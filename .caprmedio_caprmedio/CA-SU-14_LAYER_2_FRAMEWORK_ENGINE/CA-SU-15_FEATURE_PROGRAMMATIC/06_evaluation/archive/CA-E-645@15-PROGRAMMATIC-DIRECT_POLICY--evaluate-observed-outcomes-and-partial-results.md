---
identity:
  atom_id: CA-E-645@15
  ref_id: CA-E-645@15
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
      Control/Outcome Reporting
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output
      Publication
  tier: 3
relations:
  evaluation_for:
  - CA-M-405
  - CA-M-398
state:
  status: Archived
  version: 15
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-E-645@15-PROGRAMMATIC-DIRECT_POLICY--evaluate-observed-outcomes-and-partial-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Evaluate observed outcomes and partial results

## Claim

### Prose Claim

Accept outcome reporting only when it describes observed state truthfully. Complete, no-op, partial, failed, canceled and uncertain outcomes remain distinguishable; a partial result preserves completed data with the error, and a no-op does not claim a fictional write. Do not require replay or weaken atomicity merely to obtain a result.

## Details

### Scope

PROGRAMMATIC operations that can complete, no-op, partially apply, fail, cancel or become uncertain across Tools, workflows, Apps, MCP and background work.

- Exercise success, valid no-op, invalid input, mid-operation failure, cancellation and unavailable-observation cases.
- Compare returned records with durable effects and verify completed items, errors and uncertainty are represented without invented success.
- Verify a partial result contains only completed work and remaining work is not silently replayed, retried or remapped.
- Check that an atomic operation remains atomic when its contract requires it; a truthful failure is preferable to an unsafe partial write.
- Mark an outcome unresolved when the observer cannot distinguish state.
