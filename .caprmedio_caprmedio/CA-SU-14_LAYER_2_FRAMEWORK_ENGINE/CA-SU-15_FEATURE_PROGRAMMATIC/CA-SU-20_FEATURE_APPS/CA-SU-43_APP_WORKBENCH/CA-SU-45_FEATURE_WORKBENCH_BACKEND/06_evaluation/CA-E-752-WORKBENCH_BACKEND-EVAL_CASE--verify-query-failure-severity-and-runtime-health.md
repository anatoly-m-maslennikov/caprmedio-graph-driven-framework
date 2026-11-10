---
identity:
  atom_id: CA-E-752
  ref_id: CA-E-752
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control <+ Failure Handling
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 6
relations:
  evaluation_for:
  - CA-C-702
  - CA-M-462
  - CA-M-396
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-752-WORKBENCH_BACKEND-EVAL_CASE--verify-query-failure-severity-and-runtime-health.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify query-failure severity and runtime availability.

## Claim

### Prose Claim

Invalid SQL or query arguments return useful request error, `query_error` at WARNING and `outcome: failed`, while the healthy owner remains usable. Workbench-unavailable or unexpected runtime failure remains ERROR with `outcome: blocked` and its restart/runtime boundary. Verify a valid native MCP/HTTP request succeeds after an invalid one.
