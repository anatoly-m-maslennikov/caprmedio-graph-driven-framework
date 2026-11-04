---
atom_id: CA-M-463
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
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
    name: CA-M-463@1-WORKBENCH-ENG_DECISION--keep-duckdb-projection-ownership-in-the-existing-server.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-03 23:17:14 +0400
---

## Summary

Keep DuckDB Projection ownership in the existing server.

## Claim scope

The DuckDB Projection for one Project.

## Claim

### Prose Claim

The DuckDB Projection for one Project must have one stable owner for the lifetime of the existing Project gateway/shared Project pool, outside reloadable implementation children. Those children forward query and synchronization work to that owner; they must not create an independent DuckDB owner, database server, or watcher service.

The owner must preserve these connection constraints:

- serialize database-update batches and query runs;
- use native read-write mode only for trusted setup and synchronization;
- use native read-only mode for public SQL;
- close every handle in the prior mode before opening a handle in the other mode;
- never overlap read-only and read-write handles for the same database file; and
- close an old owner before its stable Project-owner replacement starts an owner for that file.

The owner serializes native read-write synchronization and native read-only public queries. This does not introduce a microservice, Project-wide lock, or scheduler coupling. The Projection state remains separate from scheduler state and outside Atom source folders.

Query Run and Check execute synchronously in the originating MCP or web request. Call the shared connector directly; do not submit query jobs to a planner, scheduler, queue or Workflow orchestrator. Background source indexing is separate technical maintenance, not asynchronous query execution.
