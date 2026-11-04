---
atom_id: CA-E-676
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 7
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-676@7-WORKBENCH_BACKEND-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/archive
relations:
  evaluation_for: [CA-R-2728, CA-R-2724, CA-R-2729, CA-M-464, CA-D-673]
updated_at: 2026-11-04 23:19:17 +0400
---
## Summary

Query native SQL results and typed Relation expansion

## Claim scope

Native SQL and typed relation expansion over derived Projection rows.

## Claim

### Prose Claim

Native DuckDB SQL and DuckPGQ SQL/PGQ return the requested columns, types, counts, and complete rows through stable bounded pages. Reachability queries over the registered property graph include the unambiguous seed and each reachable typed reference once and terminate on cycles. They follow materialized direct and declared-derived Relations without inferring prose links or synthesizing a second inverse. SQL joins or subqueries retrieve objects from the returned references. Graph mappings remain derived internal state, and the public table surface remains `atoms` and `scope_units`.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Valid selection, join, CTE, aggregation, ordering, string, and regex query | Native DuckDB returns requested business-language `content.*` columns, `relative path` and `filename`, exact counts, and all rows through stable pages. |
| Read-only schema autocomplete | `query_schema({})` returns `{tables: {atoms: [{name, type}], scope_units: [{name, type}]}}`, including declared `content.*` columns and quoted names, without reading saved SQL files or executing user SQL. |
| Multiple statements and cursor selection | A semicolon-separated script preserves quoted strings, comments and dollar-quoted strings; Run, Check and Save select the statement at the optional UTF-16 cursor position using native tokenization. |
| Explicit query and Worksheet save/load | `query_save({sql, cursor_position?})` writes exact selected SQL to immutable `q_<uuid hex>.sql`; `worksheet_save({sql})` writes `{"sql": "..."}` to immutable `w_<uuid hex>.json`; `query_load(reference)` returns saved_query_id, saved_query_url, kind and sql without executing it; `query_saved_list` returns recent entries of both kinds. |
| Run and Check saved-query identity | Run and Check save exact selected SQL before execution and return `saved_query_id`, `saved_query_url`, `kind` and `sql` separately from the materialized result `query_id`; query errors include the saved identity and URL. A save failure prevents execution and does not promise an ID. Page returns the original saved identity and URL. |
| `SELECT COUNT(*) FROM atoms` | Only the requested aggregate appears; no `atoms.hash` is added. |
| Native `GRAPH_TABLE` / `MATCH` combined with a CTE, join, filter, and aggregate | The shared connector executes it with native semantics and complete requested results; no custom traversal engine is used. |
| `Task IS_CONTAINED_BY Epic` and declared `CONTAINS` inverse | The Task row's native JSON `relations` carries the direct outgoing fact; the Epic row's `relations` carries the derived outgoing fact. Both are queryable in the same graph without duplicate inverse synthesis; rows with no outgoing facts use `{}`. |
| Cycles, duplicate paths, several selected Relation Types, and an isolated seed | A reachability query returns the seed and each reachable typed reference once, terminates, and applies no hidden depth limit. |
| Atom and Scope Unit with equal reference text; Current and Draft of one Atom | Kind and lifecycle-qualified reference keep the vertices distinct. |
| Unregistered relation or prose/Formal Claim text | It is not materialized or traversed. |
| Selected Docker image and application restart | The bundled DuckDB/DuckPGQ pair loads and enables its grammar without a runtime download; native SQL/PGQ queries work against the rebuilt graph. |
| Page metadata and empty values | `columns[].has_values` is computed across the full materialized result and remains identical across pages: NULL, empty strings, empty arrays and empty objects are empty, while false, zero and an object with keys (even null values) are values. A non-empty result may hide fully empty UI columns; a zero-row result sets `has_values: true` for every returned column and retains every header. SQL values and counts do not change. |
| UTF-16 cursor after Unicode and within strings/comments | Native UTF-8 token boundaries identify the same query for web and MCP; positions inside a surrogate pair or outside the document fail before effects. |
| No cursor and invalid/multi-statement raw SQL | Preserve the raw input in its saved file, then return the ordinary native query error with ID and full URL; Save alone does not validate SQL. |
| HTTP MCP and web saved resources | Responses contain the same saved identity fields and full request-derived URLs; no port is guessed. |

A query returning a non-null `TIMESTAMPTZ`, including `SELECT * FROM atoms` with Updated At, must preserve the instant in its ISO string result through the actual Docker dependency set.
