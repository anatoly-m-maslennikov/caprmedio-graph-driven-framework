---
identity:
  atom_id: CA-R-2786
  ref_id: CA-R-2786@4
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 4
state:
  status: archived
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2786@4-WORKBENCH-SOLUTION--rebuild-workbench-derived-state-from-source.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/099_archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-474
  - CA-D-679
---
## Summary

Rebuild Workbench derived state from source

## Claim

### Prose Claim

`workbench_reread` synchronously drops/recreates dedicated DuckDB database, WAL/temp files, schema, graph and query-result tables, then directly rereads governed Current/Draft sources and materializes current relations/graph before ready. It preserves source files, saved queries/Views and source Journal, but ephemeral result IDs disappear. It neither retains stale database/columns nor truncates in place; invalid Current Scope Unit Declaration/startup reports explicit failure and leaves Workbench unavailable until another explicit operation, without retry. Invalid ordinary source uses existing reader behavior.

This is one Workbench service operation: no scheduler, queue, generic registry, backup or Business Journal. Expose `workbench_reread({})` in generated Service discovery and the same health POST `/caprmedio/health/workbench-reread`; GET remains read-only. MCP/health use identical Project gateway/failure boundary; shared host uses explicit `project_root`, single-project accepts no body. It never restarts MCP/other services/container, and health remains available while Workbench is unavailable.
