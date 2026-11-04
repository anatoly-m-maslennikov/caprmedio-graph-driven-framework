---
atom_id: CA-M-462
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 2
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
    name: CA-M-462@2-WORKBENCH-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-04 00:38:14 +0400
---

## Summary

Constrain public DuckDB queries to native read-only access.

## Claim scope

Public SQL access to the in-memory DuckDB Projection.

## Claim

### Prose Claim

Public SQL access to the in-memory DuckDB Projection must use `connection.extract_statements(sql)` to parse the submitted SQL with DuckDB's native engine. It accepts exactly one Statement whose native StatementType is `SELECT`, then executes the original exact SQL once through that same connection. It rejects multiple Statements and every other StatementType, including DDL, DML, `SET`, `COPY`, and `ATTACH`.

This boundary must not use a regular-expression keyword check or `from_query`, which can execute DML.

Before public SQL is accepted, trusted setup must disable external access, lock configuration, and register only pure query helpers with no mutation effect. Public SQL must not be able to enable external file or network access.

Trusted setup creates only the two public tables and no Sequences. It must configure an empty temporary directory and verify, in the selected DuckDB runtime, that temporary spilling is disabled. The in-memory Projection creates no database, snapshot, schema, or log files.

Public SQL does not write Atom carriers or the Projection. Runtime acceptance must prove that an embedded write attempt is rejected.
