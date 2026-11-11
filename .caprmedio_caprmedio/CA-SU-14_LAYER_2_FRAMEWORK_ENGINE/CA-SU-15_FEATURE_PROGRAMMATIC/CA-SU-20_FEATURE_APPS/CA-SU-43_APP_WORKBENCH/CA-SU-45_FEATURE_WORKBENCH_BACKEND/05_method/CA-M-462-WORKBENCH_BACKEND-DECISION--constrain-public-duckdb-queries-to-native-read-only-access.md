---
identity:
  atom_id: CA-M-462
  ref_id: CA-M-462
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Query Processing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2728
  - CA-R-2953
state:
  status: Active
  version: 14
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-462-WORKBENCH_BACKEND-DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Constrain public DuckDB queries to native read-only access.

## Claim scope

Trusted public SQL and internal result materialization for one Project.

## Claim

### Prose Claim

Admit one whole trusted read query through MCP or the Workbench web interface with DuckDB native parsing/query APIs, including DuckPGQ SQL/PGQ. A Run or Check never selects a statement or fragment at a cursor; use native tokenization when extraction cannot support the grammar. Do not add a SQL parser, function sandbox or second query language.

Execute the accepted SELECT-only query once into a DuckDB-owned generated result table in a normal native transaction. Public input cannot submit DDL/DML; the trusted cache write may COMMIT. Retain ordered native column metadata, including duplicates, and deliver bounded pages from that stable result. Preview uses native `relation.limit(N)` without rewriting submitted SQL, preserves an existing SQL LIMIT, supports CTE/GRAPH_TABLE, and changes counts to the capped execution; absent preview adds no cap.

Keep exact submitted SQL (comments, Unicode and LIMIT) internal. Ordinary Run, Check and Page responses never echo it. Save appends the Bookmark only after materialization; a save failure returns the completed result ID/metadata with `outcome: partial` and `save_error`, without retry or rollback. Failed queries create no saved entry; unsaved Run, Check and Page have no Journal effect. Page transforms use only the existing result table and never rerun, parse, append to or rewrite SQL. At materialization, use one native cache with a private quoted ordinal before public columns; apply preview before snapshot numbering. Resolve public indices to physical positions, never user names or DuckDB `rowid`. Use the ordinal as the final stable page tie-breaker, never as public metadata or a filter/group value. Bind literal filter values with native DuckDB, use `NULLS LAST`, put group order before sort, and calculate window counts before offset/limit. Do not add a second cache, ALTER, UPDATE, rescan, raw SQL grid clause, endpoint or service.

The dedicated result lifecycle owns retention, View pinning, restart disposal and runtime-setting reads. Startup loads bundled DuckPGQ before disabling external access, autoinstall/autoload and public configuration changes; database/spill writes stay in the owned runtime directory and sources stay unchanged. Reject/unknown/storage/delivery errors return useful caller reasons and stderr diagnostics. Invalid requests are recoverable `query_error` WARNING failures; unavailable/unexpected owner failures are ERROR/blocked with the existing restart or generic boundary. DuckPGQ management calls may invalidate the connection; this trusted-input MVP promises no capability sandbox, retry, restoration or connection recovery.
