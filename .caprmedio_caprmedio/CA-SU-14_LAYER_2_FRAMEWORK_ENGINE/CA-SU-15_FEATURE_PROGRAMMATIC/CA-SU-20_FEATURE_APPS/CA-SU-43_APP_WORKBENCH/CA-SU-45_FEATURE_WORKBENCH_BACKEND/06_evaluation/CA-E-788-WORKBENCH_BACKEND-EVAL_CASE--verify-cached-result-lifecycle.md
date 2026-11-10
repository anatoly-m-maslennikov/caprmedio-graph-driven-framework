---
identity:
  atom_id: CA-E-788
  ref_id: CA-E-788
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Storage <+ Temporary State
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 7
relations:
  evaluation_for:
  - CA-M-462
  - CA-M-463
  - CA-O-240
  - CA-C-701
  - CA-R-2729
  IS_REPLACEMENT_FOR:
  - CA-E-751
state:
  status: Active
  version: 5
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-788-WORKBENCH_BACKEND-EVAL_CASE--verify-cached-result-lifecycle.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify cached result lifecycle

## Claim

### Prose Claim

Use the real Workbench and native DuckDB result tables to verify whole-query admission rejects multi-statements; invalid structured Run/View preserves the last reachable result; valid failed View rerun releases the old result; and SQL editing alone preserves it. An open View pins beyond TTL, closed young results remain reachable, and old unpinned results may expire. `result_ttl_seconds = 1` takes effect only after explicit Workbench restart.

First-page `NaN`/infinity conversion failure creates no ID/registration/table; later-page failure after a known ID preserves it for other fetches. Restart clears all result tables/IDs. Query-result files are delivery artifacts, not cache/restore/pin state; no setting write/staging/restore path is added. Use actual queries, views, expiry and table observability, not mocks/row lists/frontend state. Export failure returns known ID plus delivery error without a successful path; valid later fetch remains possible and partial files never count complete.
