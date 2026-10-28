---
atom_id: CA-E-645
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:38 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
relations:
  evaluation_for:
  - CA-M-405
  - CA-M-398
tier: 3
---
# Summary

Evaluate observed outcomes and partial results

## Scope

PROGRAMMATIC operations that can complete, no-op, partially apply, fail, cancel or become uncertain across Tools, workflows, Apps, MCP and background work.

## Claim

Accept outcome reporting only when it describes observed state truthfully. Complete, no-op, partial, failed, canceled and uncertain outcomes remain distinguishable; a partial result preserves completed data with the error, and a no-op does not claim a fictional write. Do not require replay or weaken atomicity merely to obtain a result.

## Details

- Exercise success, valid no-op, invalid input, mid-operation failure, cancellation and unavailable-observation cases.
- Compare returned records with durable effects and verify completed items, errors and uncertainty are represented without invented success.
- Verify a partial result contains only completed work and remaining work is not silently replayed, retried or remapped.
- Check that an atomic operation remains atomic when its contract requires it; a truthful failure is preferable to an unsafe partial write.
- Mark an outcome unresolved when the observer cannot distinguish state.
