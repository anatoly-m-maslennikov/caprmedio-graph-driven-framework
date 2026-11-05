---
atom_id: CA-E-676
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 9
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 5
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
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
carrier_destination:
  file:
    name: CA-E-676@9-WORKBENCH_BACKEND-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/archive
---

## Summary

Query native SQL results and typed relation expansion

## Claim scope

Native SQL and typed relation expansion over derived Projection rows.

## Claim

### Prose Claim

Native DuckDB SQL and DuckPGQ SQL/PGQ return requested columns, types, counts and complete rows through stable bounded pages. Reachability follows materialized direct and declared-derived Relations once, terminates on cycles and does not infer prose links or synthesize another inverse. Public tables remain `atoms` and `scope_units`.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Valid selection, join, CTE, aggregation, ordering, string and regex query | Native DuckDB returns requested business-language `content.*` columns, `relative path`, `filename`, exact counts and all rows through stable pages. |
| Read-only schema autocomplete | `query_schema({})` returns actual table/column metadata, including quoted names and optional distinct non-null `atoms.status` values. Fetching schema neither executes user SQL nor reads/writes saved items. |
| Multiple statements and cursor selection | Run, Check and explicit Save select the optional UTF-16 cursor statement with native tokenization; a semicolon script preserves strings, comments and dollar-quoted strings. |
| Explicit query and Worksheet save/load | `query_save({sql, cursor_position?, name?})` and `worksheet_save({sql, name?})` append exact SQL to the Project saved-item Journal with canonical UUIDv7 ID, kind, optional creation name and saved time. Load/list return valid Journal items and legacy `q_<hex>.sql`/`w_<hex>.json` read-only fallback items. Saved items are not renamed. |
| Run and Check read-only behavior | Run and Check return actual selected SQL, query result/counts or query error, never append a saved-item Journal row, never require Journal writability and never return a new saved identity. Page returns the same materialized query result without rerunning or persisting SQL. |
| Invalid SQL or failed selection | Return the ordinary query/validation error, not an empty successful result and not invented selected SQL or saved identity. |
| HTTP MCP and web parity | MCP and web Run/Check/Page produce the same query behavior; explicit Save/Worksheet Save, Load and List produce the same saved-resource fields and request-derived URLs. |
| Saved-item Journal partitioning and source watcher | Explicit saved-item writes use the existing `workbench-saved-items` date-partitioned 1,000-row writer and do not trigger Atom source reindexing. |
| Graph queries | Native `GRAPH_TABLE`/`MATCH`, joins and CTEs execute with native semantics; cycles return each reachable typed reference once and do not synthesize prose links. |
| Page metadata and empty values | `columns[].has_values` is complete-result metadata and identical across pages. Empty values are NULL, empty string, empty array/object; false, zero and object-with-keys are values. Zero-row results retain all headers. |
