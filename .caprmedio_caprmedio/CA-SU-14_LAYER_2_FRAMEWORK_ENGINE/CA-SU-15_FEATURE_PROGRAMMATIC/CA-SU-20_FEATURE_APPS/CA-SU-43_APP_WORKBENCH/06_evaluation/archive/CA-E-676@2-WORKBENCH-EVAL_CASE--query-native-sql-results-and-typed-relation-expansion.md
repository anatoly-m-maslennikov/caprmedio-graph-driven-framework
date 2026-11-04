---
atom_id: CA-E-676
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 2
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-676@2-WORKBENCH-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
relations:
  evaluation_for: [CA-R-2728, CA-R-2724, CA-R-2729, CA-M-464, CA-D-673]
updated_at: 2026-11-04 00:38:14 +0400
---
## Summary

Query native SQL results and typed Relation expansion

## Claim scope

Native SQL and typed relation expansion over in-memory Projection rows.

## Claim

### Prose Claim

Native DuckDB SQL returns exactly requested columns, types, counts, and complete rows. `expand` reads materialized direct and declared-derived nested relation facts, returns typed references, includes the unambiguous seed and each reachable reference once, and terminates on cycles. It neither fetches objects nor infers prose links or synthesizes a second inverse. Relation materialization stays in memory and creates no public relation table or view.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Valid selection, join, CTE, aggregation, ordering, string, and regex query | Native DuckDB returns requested columns and all rows with exact counts. |
| `SELECT COUNT(*) FROM atoms` | Only the requested aggregate appears; no `atoms.hash` is added. |
| Direct fact and declared inverse | Refreshed nested facts are materialized once each; `expand` returns no duplicate inverse traversal. |
| Cyclic selected relations | `expand` returns seed and reachable typed references once, then terminates. |
| Unregistered relation or prose/Formal Claim text | It is not materialized or traversed. |
