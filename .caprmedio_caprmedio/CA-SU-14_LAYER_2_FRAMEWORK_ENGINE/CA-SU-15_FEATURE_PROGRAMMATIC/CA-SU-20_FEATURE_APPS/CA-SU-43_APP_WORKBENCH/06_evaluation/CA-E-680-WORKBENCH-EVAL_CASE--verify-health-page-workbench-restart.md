---
identity:
  atom_id: CA-E-680
  ref_id: CA-E-680
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2782
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-680-WORKBENCH-EVAL_CASE--verify-health-page-workbench-restart.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Verify health-page Workbench restart

## Claim

### Prose Claim

Verify health Restart Workbench invokes the same native MCP action and shows actual ready/failure while page remains available on failure; GET HTML/JSON is read-only. Fixed Project form yields fresh queries, unknown old IDs and loadable saved items. Invalid Declaration reports failure without disabling MCP/page. Shared host requires explicit Project folder and restarts only it; missing/repeated/unknown fields reject before effect; blacklist remains enforced.
