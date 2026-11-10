---
identity:
  atom_id: CA-E-753
  ref_id: CA-E-753
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 6
relations:
  evaluation_for:
  - CA-C-703
  - CA-R-2728
  - CA-M-462
  - CA-D-673
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-753-WORKBENCH_BACKEND-EVAL_CASE--verify-deployed-mcp-query-schema.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify the deployed MCP Workbench query schema.

## Claim

### Prose Claim

Verify the deployed MCP query schema requires `sql` and accepts optional native-typed `preview` (non-negative integer) and `save` (boolean). A native SDK request with `preview: 0` and `save: false` reaches the operation, yields the expected zero-row preview and creates no saved query; shared results/saved-resource behavior remains consistent.
