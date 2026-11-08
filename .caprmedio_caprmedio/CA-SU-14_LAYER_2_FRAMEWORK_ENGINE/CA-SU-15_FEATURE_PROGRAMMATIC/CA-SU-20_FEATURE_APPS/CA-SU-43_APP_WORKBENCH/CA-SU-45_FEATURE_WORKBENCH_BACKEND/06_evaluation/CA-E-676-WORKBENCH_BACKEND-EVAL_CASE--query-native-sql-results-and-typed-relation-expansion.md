---
identity:
  atom_id: CA-E-676
  ref_id: CA-E-676
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2728
  - CA-R-2729
  - CA-R-2724
  - CA-M-462
  - CA-M-463
  - CA-M-464
  - CA-M-465
  - CA-D-672
  - CA-D-673
state:
  status: Active
  version: 12
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-E-676-WORKBENCH_BACKEND-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Query native SQL results and typed relation expansion

## Claim scope

Native SQL and typed relation expansion over derived Projection rows.

## Claim

### Prose Claim

Native DuckDB SQL and DuckPGQ SQL/PGQ return requested columns, types, counts and complete rows through stable bounded pages. Reachability follows materialized direct and declared-derived Relations once, terminates on cycles and does not infer prose links or synthesize another inverse. Graph source tables remain atoms and scope_units.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Valid selection, join, CTE, aggregation, ordering, string and regex query | Native DuckDB returns requested declared dot-separated content.* columns with snake_case segments, relative path, filename, exact counts and all rows through stable pages. |
| Graph query and relation expansion | Native GRAPH_TABLE and MATCH queries return typed direct and derived relations. Cycles return each reachable typed reference once and do not synthesize prose links. |
| No preview parameter | query_run applies no added cap and returns the normal uncapped materialized count. |
| Preview with CTE, GRAPH_TABLE and an existing LIMIT | query_run with preview N returns at most N rows, preserves an existing SQL LIMIT, uses native relation.limit(N) without rewriting SQL or its text, and reports counts for the previewed execution. |
| Exact submitted query | Run and a successful saved Run return and, when saved, persist the exact submitted one-query SQL, including comments, Unicode and any existing LIMIT. |
| Read-only schema autocomplete | query_schema({}) returns actual table/column metadata, including quoted names and optional distinct non-null values for the actual Header Status columns exposed by query_schema. Fetching schema neither executes user SQL nor reads or writes saved items. |
| Whole-query admission | Run, Check and Run & Save accept one complete query and reject multiple SQL statements. Preserve comments, quoted strings, dollar-quoted strings and CTEs. Optional UTF-16 cursor_position is editor-caret metadata only and does not select executable SQL. |
| Successful query save | query_run with save true writes one exact query Journal entry only after its Run succeeds and returns the saved identity, URL, kind and optional name. |
| Failed Run with save requested | Invalid SQL, multiple statements or execution failure returns the ordinary error and creates no saved entry. |
| Partial save failure | If the result completes but Journal saving fails, return HTTP 200 and MCP is_error=false with the completed rows/query ID plus outcome: partial and save_error. Do not return a saved identity unless known, retry, roll back or claim aggregate success. |
| View save/load | view_save writes one complete query as a View Journal entry with kind view. query_load and query_saved_list return new View entries and legacy kind worksheet entries and q_<hex>.sql/w_<hex>.json read-only fallback items. Saved items are not renamed. |
| Run, Check and Page no-save behavior | Run without save, Check and Page return actual submitted SQL, query results/counts or query error, never append a saved-item Journal row and never require Journal writability. Page returns the same materialized query result without rerunning. |
| HTTP MCP and web parity | MCP and web Run, Check, Page, Schema, Run & Save, View Save, Load and List produce the same query behavior and saved-resource fields and request-derived URLs. |
| Saved-item Journal partitioning and source watcher | Explicit saved-item writes use the existing workbench-saved-items date-partitioned 1,000-row writer and do not trigger Atom source reindexing. |
| Page metadata and empty values | columns[].has_values is complete-result metadata and identical across pages. Empty values are NULL, empty string, empty array/object; false, zero and object-with-keys are values. Zero-row results retain all headers. |
