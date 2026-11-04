---
atom_id: CA-M-463
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 2
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
    name: CA-M-463-WORKBENCH-ENG_DECISION--keep-duckdb-projection-ownership-in-the-existing-server.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
updated_at: 2026-11-04 00:38:14 +0400
---

## Summary

Keep DuckDB Projection ownership in the existing server.

## Claim scope

The in-memory DuckDB Projection for one Project.

## Claim

### Prose Claim

The in-memory DuckDB Projection for one Project must have one owner in the existing server. The owner holds the Projection only in memory, creates no temporary spill files, and does not create a database server, watcher service, queue, planner, scheduler, or orchestrator.

The owner serializes technical background indexing and public native-SQL access. Query Run and Check execute synchronously in the originating MCP or web request through that owner; they are not background query work.

The Projection is rebuilt when the application restarts after code changes. This MVP does not prescribe a live implementation-generation handoff.
