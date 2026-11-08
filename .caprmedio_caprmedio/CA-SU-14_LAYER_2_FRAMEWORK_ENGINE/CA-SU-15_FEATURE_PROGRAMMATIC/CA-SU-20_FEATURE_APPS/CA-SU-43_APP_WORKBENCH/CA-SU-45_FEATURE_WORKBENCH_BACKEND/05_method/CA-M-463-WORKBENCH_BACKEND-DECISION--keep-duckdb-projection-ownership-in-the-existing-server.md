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
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2725
  - CA-R-2729
state:
  status: Active
  version: 7
  updated_at: 2026-11-09 00:09:26 +0400
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

Keep one serialized DuckDB owner in the existing application. Store its rebuildable database and spill data under `.caprmedio_runtime/workbench` in the selected repository. Source files remain authoritative; the database is disposable derived data.

Materialize each Run once. Direct query_run returns a stable query ID, original column metadata, exact total counts and its first page; View Run returns only execution metadata and a query ID, and its rows are fetched separately. Read subsequent pages from that materialized result, including after source refresh. Default to 100 rows per page and allow 1 through 1,000. Reject invalid sizes, offsets and unknown IDs explicitly. No hidden row limit changes the query result.

Keep a materialized Run result while its age is less than the positive `result_ttl_seconds` setting, or while its owner View is open. Read `[workbench].result_ttl_seconds` from `.caprmedio_runtime/caprmedio_runtime_settings.toml` only when the Workbench starts; its default is `3600`, it must be a positive integer, and an edit takes effect only through explicit Workbench restart. Do not hot-reload or edit this setting through MCP. Closing a View only unpins its result, so a young closed-View result remains reachable. Editing a View's SQL preserves its last Run result until a valid rerun begins. Validate structured Run/View arguments before releasing an existing result. Once valid rerun execution begins, release the old View result before native execution, even when the new SQL then fails. Rebuild the Projection and clear all old query results at startup; result IDs do not survive restart.

Query result tables are DuckDB-owned disposable runtime data. Do not add a manual result-file or configuration staging layer, write settings, create a second cache, or restore discarded result state. If first-page conversion fails before the caller receives a query ID, remove that result registration and cache table before returning the error. A later page-conversion error keeps the caller's known result ID available for other pages. Check counts without transferring all result rows to Python and discards its own materialized result.

Serialize source refresh, Run, Page and Check through the same owner. Requests remain synchronous. Do not add a database server, queue, planner, scheduler, orchestrator or background query worker. Retain successful parsed-source rows and their filesystem signatures in the existing owner for incremental refresh. Remove their cached parsed state when a source is deleted, leaves the inventory or becomes invalid. Skip unchanged invalid inputs; a later actual source change is new input.
