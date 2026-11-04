---
atom_id: CA-O-240
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 3
author: Anatoly Maslennikov
role: Operations
form: Action
tier: 6
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  depends_on:
  - CA-R-2728
  - CA-R-2729
  - CA-R-2724
  - CA-M-463
  - CA-M-462
  - CA-D-673
carrier_destination:
  file:
    name: CA-O-240@3-WORKBENCH-ACTION--execute-one-read-only-duckdb-query.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/09_operations/archive
updated_at: 2026-11-04 05:16:33 +0400
---

## Summary

Execute one read-only DuckDB query

## Claim scope

One public native-SQL Run or Check request against one committed in-memory Project query Projection.

## Claim

Execute one read-only DuckDB query **means** the direct request-time Action that performs the exact SQL supplied by an originating MCP or web Run or Check request through the Project's shared in-memory query owner.

The Action must:

- serialize the direct request with technical background indexing;
- use native DuckDB SQL and DuckPGQ SQL/PGQ semantics over the registered graph, not a keyword filter, custom SQL parser, or custom traversal engine;
- use the in-memory native SQL read-only boundary specified by CA-M-462 before public SQL is accepted, without creating temporary spill files;
- execute the exact request synchronously and return its result before the originating request completes;
- return SQL errors to the originating request as errors, never as empty successful results; and
- keep source-file failures as indexer stderr events, not query rows or query errors.

Run returns its complete rows, column names, column types, row count, and column count from that execution. Check executes the same read-only SQL to return its validity and exact row and column counts without a substituted or estimated result. The Action does not create a query job, ticket, queue, planner, scheduler, orchestrator, background query process, or business Journal record.
