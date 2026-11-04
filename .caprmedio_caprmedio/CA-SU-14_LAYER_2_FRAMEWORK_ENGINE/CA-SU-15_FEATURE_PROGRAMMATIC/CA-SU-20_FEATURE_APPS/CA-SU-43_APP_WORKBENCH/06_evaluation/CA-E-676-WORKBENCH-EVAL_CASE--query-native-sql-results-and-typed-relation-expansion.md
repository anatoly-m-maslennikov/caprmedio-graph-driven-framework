---
atom_id: CA-E-676
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 3
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-676-WORKBENCH-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
relations:
  evaluation_for: [CA-R-2728, CA-R-2724, CA-R-2729, CA-M-464, CA-D-673]
updated_at: 2026-11-04 05:16:33 +0400
---
## Summary

Query native SQL results and typed Relation expansion

## Claim scope

Native SQL and typed relation expansion over in-memory Projection rows.

## Claim

### Prose Claim

Native DuckDB SQL and DuckPGQ SQL/PGQ return the requested columns, types, counts, and complete rows. Reachability queries over the registered property graph include the unambiguous seed and each reachable typed reference once and terminate on cycles. They follow materialized direct and declared-derived Relations without inferring prose links or synthesizing a second inverse. SQL joins or subqueries retrieve objects from the returned references. Graph mappings remain in memory, and the public table surface remains `atoms` and `scope_units`.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Valid selection, join, CTE, aggregation, ordering, string, and regex query | Native DuckDB returns requested columns and all rows with exact counts. |
| `SELECT COUNT(*) FROM atoms` | Only the requested aggregate appears; no `atoms.hash` is added. |
| Native `GRAPH_TABLE` / `MATCH` combined with a CTE, join, filter, and aggregate | The shared connector executes it with native semantics and complete requested results; no custom traversal engine is used. |
| `Task IS_CONTAINED_BY Epic` and declared `CONTAINS` inverse | The Task row carries the direct outgoing fact; the Epic row carries the derived outgoing fact. Both are queryable in the graph without duplicate inverse synthesis. |
| Cycles, duplicate paths, several selected Relation Types, and an isolated seed | A reachability query returns the seed and each reachable typed reference once, terminates, and applies no hidden depth limit. |
| Atom and Scope Unit with equal reference text; Current and Draft of one Atom | Kind and lifecycle-qualified reference keep the vertices distinct. |
| Unregistered relation or prose/Formal Claim text | It is not materialized or traversed. |
| Selected Docker image and application restart | The bundled DuckDB/DuckPGQ pair loads and enables its grammar without a runtime download; native SQL/PGQ queries work against the rebuilt in-memory graph. |
