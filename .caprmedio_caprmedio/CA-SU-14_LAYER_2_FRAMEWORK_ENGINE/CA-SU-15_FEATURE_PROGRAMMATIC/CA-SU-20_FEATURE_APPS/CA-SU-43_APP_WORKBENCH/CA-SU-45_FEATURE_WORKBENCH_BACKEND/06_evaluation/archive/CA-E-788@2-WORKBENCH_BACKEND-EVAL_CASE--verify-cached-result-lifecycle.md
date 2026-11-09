---
identity:
  atom_id: CA-E-788@2
  ref_id: CA-E-788@2
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-M-462
  - CA-M-463
  - CA-O-240
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-E-788@2-WORKBENCH_BACKEND-EVAL_CASE--verify-cached-result-lifecycle.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Verify cached result lifecycle

## Claim

### Prose Claim

Through the real Workbench service and its native DuckDB result tables, verify these lifecycle outcomes:

| Case | Expected result |
| --- | --- |
| Whole-query admission | Run and Check reject a multi-statement request rather than selecting one statement at a cursor. |
| Invalid structured arguments | A malformed Run/View request fails before execution and preserves the last reachable result ID and rows. |
| Valid failed rerun | After validation succeeds, a View rerun releases its old result before the new native SQL fails; fetching the old result then fails. |
| SQL editing | Updating View SQL without a valid rerun preserves the last Run result, which remains the result of the prior SQL. |
| Age-or-open retention | An open View pins its result beyond TTL; closing it retains a young result and permits disposal of an old unpinned result. |
| Runtime setting timing | Set `result_ttl_seconds = 1` in the runtime TOML, explicitly restart the Workbench, and verify the one-second lifecycle; changing the file without restart has no effect. |
| Restart | Restart clears all materialized results and process-local result IDs. |
| Result storage boundary | Native DuckDB owns result tables; the service adds no manual result/configuration staging file, setting write, second cache or restore path. |

Use actual queries, View operations, expiry time and native result-table observability. Verify first-page failure removes only an unrevealed result while a known ID survives a later page-conversion failure. Do not substitute mocked clocks, Python row lists or a frontend-only state transition for owner and DuckDB evidence.
