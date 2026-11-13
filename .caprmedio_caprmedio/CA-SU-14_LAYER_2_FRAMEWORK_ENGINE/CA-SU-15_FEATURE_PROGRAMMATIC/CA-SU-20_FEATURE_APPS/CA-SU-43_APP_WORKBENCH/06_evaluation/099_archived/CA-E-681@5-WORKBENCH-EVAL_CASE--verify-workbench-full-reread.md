---
identity:
  atom_id: CA-E-681
  ref_id: CA-E-681@5
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
  version: 5
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-681@5-WORKBENCH-EVAL_CASE--verify-workbench-full-reread.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/099_archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Verify Workbench full reread

## Claim

### Prose Claim

Verify full reread recreates derived state from governed sources through the same MCP/health operation, preserving sources/saved items/Journal and failing explicitly without retry for invalid required source/startup. A declared-property change rebuilds database/WAL/temp/schema and rereads source; rebuilt rows/relations/graph/results lack stale state and old result IDs. Saved query/View remain. `workbench_reread` is Service discovery without generic registry. Invalid Declaration leaves not-ready with no fallback; invalid ordinary source uses reader behavior rather than stale state; MCP remains usable.
