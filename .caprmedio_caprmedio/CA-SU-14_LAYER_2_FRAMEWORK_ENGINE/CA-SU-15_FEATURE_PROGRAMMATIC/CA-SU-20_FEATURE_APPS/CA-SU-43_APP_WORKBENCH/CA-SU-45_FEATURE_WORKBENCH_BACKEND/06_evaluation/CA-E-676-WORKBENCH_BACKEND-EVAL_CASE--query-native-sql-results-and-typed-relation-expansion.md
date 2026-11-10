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
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Query Processing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
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
  - CA-M-516
state:
  status: Active
  version: 15
  updated_at: 2026-11-10 20:47:54 +0400
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

Native DuckDB and DuckPGQ SQL/PGQ return requested columns/types/counts and complete rows through stable bounded pages. Typed reachability follows materialized direct/declared-derived Relations once, terminates cycles, and neither infers prose links nor synthesizes a second inverse; graph source tables remain `atoms` and `scope_units`.

## Details

Verify native selections, joins, CTEs, aggregation, ordering, regex and GRAPH_TABLE/MATCH with declared dotted Content columns, exact counts and stable pages. Whole-query admission retains comments, quotes, dollar quotes and CTEs; cursor metadata never selects SQL. Preview uses native `relation.limit(N)`, preserves existing LIMIT and changes execution counts; no preview adds no cap. Ordinary responses omit exact SQL, while explicit Bookmark load returns it; save follows successful execution, failed execution saves nothing, and failed post-result save returns partial metadata without retry/rollback.

Verify Run/Check/Page and MCP/web parity: Check has metadata/errors only; Page reuses the same cache; saved Views and legacy saved items retain compatibility; query schema reads no SQL/saved item. Default complete export is JSON matrix; CSV/official TOON preserve duplicate aliases, zero rows, null/empty/typed values and multiline Unicode/Formal Claims. Explicit inline pages match exports and View Run stays metadata-only until fetch. Export failure preserves a known result for later fetch and never reports a failed path or reruns SQL. Query logs retain metadata, never result rows/files.
