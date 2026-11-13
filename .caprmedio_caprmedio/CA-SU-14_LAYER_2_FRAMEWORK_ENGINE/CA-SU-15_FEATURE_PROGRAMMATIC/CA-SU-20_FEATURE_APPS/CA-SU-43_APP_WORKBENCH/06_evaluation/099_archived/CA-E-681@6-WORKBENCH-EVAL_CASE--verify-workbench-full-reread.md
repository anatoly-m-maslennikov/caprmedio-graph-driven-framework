---
identity:
  atom_id: CA-E-681
  ref_id: CA-E-681@6
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Indexing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 6
relations:
  evaluation_for:
  - CA-R-2786
state:
  status: archived
  version: 6
  updated_at: '2026-11-12T16:59:43.837031+00:00'
destination:
  file:
    name: CA-E-681@6-WORKBENCH-EVAL_CASE--verify-workbench-full-reread.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/099_archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Verify Workbench full reread

## Claim

### Prose Claim

Verify full reread recreates derived state from governed sources through the same MCP/health operation, preserving sources/saved items/Journal and failing explicitly without retry for invalid required source/startup. Recreate the SQL tables and derived state under the installed schema and relation registry. Rebuilt rows, relations and graph omit stale data and old result IDs. The explicitly loaded Archive Scope Unit and Role pairs remain loaded and queryable before reread reports ready. Archive sources outside those pairs remain unloaded. Saved query/View remain. `workbench_reread` is Service discovery without generic registry. Invalid Declaration leaves not-ready with no fallback; invalid ordinary source uses reader behavior rather than stale state; MCP remains usable.
