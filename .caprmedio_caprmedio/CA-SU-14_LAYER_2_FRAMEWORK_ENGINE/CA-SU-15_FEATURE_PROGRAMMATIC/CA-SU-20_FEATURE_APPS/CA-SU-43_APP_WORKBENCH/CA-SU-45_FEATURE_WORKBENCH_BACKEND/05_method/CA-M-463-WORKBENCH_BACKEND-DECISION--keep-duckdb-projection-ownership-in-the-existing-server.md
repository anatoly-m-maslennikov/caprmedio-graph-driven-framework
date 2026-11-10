---
identity:
  atom_id: CA-M-463
  ref_id: CA-M-463
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Storage <+ Temporary State
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2725
  - CA-R-2729
state:
  status: Active
  version: 10
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-463-WORKBENCH_BACKEND-DECISION--keep-duckdb-projection-ownership-in-the-existing-server.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Keep DuckDB Projection ownership in the existing server.

## Claim scope

The derived DuckDB Projection and query results for one Project.

## Claim

### Prose Claim

Keep one serialized DuckDB owner in the existing application. Use the delivered database and spill locations.

Materialize each Run once. Page reads use that materialized result, including after source refresh; execution and delivery retain their separate failure boundaries.

Use the delivered startup TTL to keep a result while it is young or pinned by its open owner View. Measure age with a monotonic clock. Add no heartbeat, cross-process lease or crash recovery. Closing unpins but does not evict a young result. Editing View SQL preserves its last result until valid rerun starts; then release it before native execution, even if SQL fails. Startup rebuild clears old results; IDs do not survive restart. First-page conversion failure removes an unrevealed result; later conversion/export failure preserves the known ID and reports the delivery error.

Serialize refresh, Run, Page and Check through this owner synchronously. Do not add a database server, queue, planner, scheduler or worker. Retain parsed-source rows/signatures for incremental refresh; remove cache for deleted, excluded or invalid sources and treat a later actual change as new input. No configuration staging, second cache or discarded-state restoration is added.
