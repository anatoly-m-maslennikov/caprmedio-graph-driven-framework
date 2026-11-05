---
atom_id: CA-M-462
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 9
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
    name: CA-M-462@9-WORKBENCH_BACKEND-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archive
updated_at: 2026-11-05 17:09:51 +0400
---

## Summary

Constrain public DuckDB queries to native read-only access.

## Claim scope

Trusted public SQL and internal result materialization for one Project.

## Claim

Admit one read query from trusted Operator input through MCP or the Workbench web interface with DuckDB's native parsing and query APIs, including DuckPGQ's SQL/PGQ grammar. Use native tokenization where statement extraction does not support that grammar. Do not introduce a SQL parser, function sandbox or second query language.

Execute the accepted query once into a generated internal result table in the Project's derived DuckDB database. This trusted cache write uses a normal native transaction with COMMIT; public input remains SELECT-only and cannot submit DDL or DML. Read native ordered column metadata before materialization and retain it separately, including duplicate names. Deliver bounded pages from that stable result, not the entire result in a Python list. If query_run receives a non-negative preview, apply DuckDB's native relation.limit(N) to cap the result at most at N rows while preserving an existing SQL LIMIT; do not rewrite the submitted SQL or its text, and support GRAPH_TABLE and CTE queries. Counts and pagination describe that capped execution.

Run returns the exact selected SQL, including comments, Unicode and any existing LIMIT. When query_run requests save, append the saved query only after the successful materialization, using the exact selected SQL. A save failure does not discard the completed result: return its query ID and rows with outcome partial and save_error, without retry or rollback. A failed query never creates a saved entry. Run without save, Check and Page have no Journal effect.

Trusted startup loads the bundled DuckPGQ extension before disabling external access, extension autoinstall/autoload and public configuration changes. Permit database and spill writes only in the owned Workbench runtime directory. Source files remain unchanged.

Known invalid requests, unknown result IDs, rejected SQL, storage and result-delivery errors return their useful reason to the originating MCP or web caller and report stderr. They are not successful empty results or retried requests. An ordinary rejected query leaves a valid owner available. Invalid SQL, invalid query arguments and unknown query references are recoverable request failures: log query_error as WARNING with outcome failed, not as a blocking runtime ERROR. Workbench-unavailable and unexpected internal runtime failures remain ERROR with outcome blocked. A failed owner reports Workbench-unavailable and restart-required; unexpected internal failures use the existing generic public error boundary.

DuckPGQ internal management calls remain unsupported and may invalidate the connection. This trusted-input MVP does not promise a capability sandbox. Do not add automatic query retries, rollback, retained-state restoration or connection recovery.

When preview is omitted, Run applies no added preview cap.
