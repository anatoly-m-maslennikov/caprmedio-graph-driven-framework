---
atom_id: CA-M-463
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 4
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2725
  - CA-R-2729
carrier_destination:
  file:
    name: CA-M-463@4-WORKBENCH_BACKEND-ENG_DECISION--keep-duckdb-projection-ownership-in-the-existing-server.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archive
updated_at: 2026-11-04 17:55:47 +0400
---

## Summary

Keep DuckDB Projection ownership in the existing server.

## Claim scope

The derived DuckDB Projection and query results for one Project.

## Claim

### Prose Claim

Keep one serialized DuckDB owner in the existing application. Store its rebuildable database and spill data under `.caprmedio_runtime/workbench` in the selected repository. Source files remain authoritative; the database is disposable derived data.

Materialize each Run once and return a stable query ID, original column metadata, exact total counts and its first page. Read subsequent pages from that materialized result, including after source refresh. Default to 100 rows per page and allow 1 through 1,000. Reject invalid sizes, offsets and unknown IDs explicitly. No hidden row limit changes the query result.

Keep materialized Run results until the owner closes. Rebuild the Projection and clear old query results at startup; result IDs do not survive restart. Check counts without transferring all result rows to Python and discards its own materialized result.

Serialize source refresh, Run, Page and Check through the same owner. Requests remain synchronous. Do not add a database server, queue, planner, scheduler, orchestrator or background query worker. Release successful parsed-source caches after refresh; retain failed-source signatures so unchanged invalid inputs are not retried.
