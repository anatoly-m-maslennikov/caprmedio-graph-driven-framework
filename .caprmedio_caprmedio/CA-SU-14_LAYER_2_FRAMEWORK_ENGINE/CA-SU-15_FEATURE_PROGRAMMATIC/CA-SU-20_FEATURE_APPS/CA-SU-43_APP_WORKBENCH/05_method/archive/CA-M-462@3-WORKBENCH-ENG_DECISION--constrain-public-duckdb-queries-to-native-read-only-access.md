---
atom_id: CA-M-462
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 3
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2728
carrier_destination:
  file:
    name: CA-M-462@3-WORKBENCH-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-04 05:16:33 +0400
---

## Summary

Constrain public DuckDB queries to native read-only access.

## Claim scope

Public SQL access to the in-memory DuckDB Projection.

## Claim

### Prose Claim

Public SQL access to the in-memory DuckDB Projection must use `connection.extract_statements(sql)` to parse the submitted SQL with DuckDB's native engine. Only exactly one Statement whose native StatementType is `SELECT` may proceed to the read-only execution boundary. After the complete boundary accepts it, execute the original exact SQL once through the same connection. Reject multiple Statements and every other StatementType, including DDL, DML, `SET`, `COPY`, and `ATTACH`.

Native Statement classification is necessary, but it does not prove that a `SELECT` has no side effects. DuckPGQ graph-management and mutable graph-cache functions must not be callable through public SQL. The selected integration must preserve the read-only boundary for both ordinary SQL and SQL/PGQ. A `SELECT` that changes graph or Projection state must be rejected.

This boundary must not use a regular-expression keyword check or `from_query`, which can execute DML.

Trusted setup loads DuckPGQ and enables its SQL/PGQ grammar before disabling external access and locking configuration. Graph creation and refresh belong to trusted setup and indexing. Public SQL may query the registered graph but must not install or load extensions, change configuration, create or drop graphs, mutate graph caches, or enable external file or network access. Any application query helper must have no mutation effect.

Trusted setup creates only the two public tables, internal in-memory graph mappings, and no Sequences. It must configure an empty temporary directory and verify, in the selected DuckDB runtime, that temporary spilling is disabled. The in-memory Projection creates no database, snapshot, schema, or log files.

Public SQL does not write Atom carriers or the Projection. Runtime acceptance must prove that embedded writes and side-effecting extension calls are rejected; passing the Statement-type check alone is insufficient.
