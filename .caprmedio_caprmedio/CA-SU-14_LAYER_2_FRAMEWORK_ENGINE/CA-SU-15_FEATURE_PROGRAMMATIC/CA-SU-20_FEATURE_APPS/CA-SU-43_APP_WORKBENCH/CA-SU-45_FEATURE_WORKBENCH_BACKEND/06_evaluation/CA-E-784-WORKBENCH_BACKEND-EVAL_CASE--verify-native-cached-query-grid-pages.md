---
identity:
  atom_id: CA-E-784
  ref_id: CA-E-784
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Query Processing
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 8
relations:
  evaluation_for:
  - CA-M-462
  - CA-R-2953
  - CA-O-240
state:
  status: Active
  version: 4
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-E-784-WORKBENCH_BACKEND-EVAL_CASE--verify-native-cached-query-grid-pages.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Verify native cached query grid pages

## Claim

### Prose Claim

Against a real DuckDB materialized result and the MCP page boundary, verify the following cases for both `query_page` and a View's `view_fetch` where applicable:

| Case | Expected result |
| --- | --- |
| Duplicate and dotted aliases | Zero-based grid indices select and order the intended original output positions even when aliases duplicate or contain dots. |
| `rowid` output name | A result whose public output includes `rowid` has stable page order from the hidden snapshot ordinal, not DuckDB `rowid`. |
| Native CTE, DuckPGQ and preview | CTE and DuckPGQ queries, including a previewed result, execute their original submitted SQL once through the same ordinal CTAS; pages address the limited snapshot and Run/save responses preserve the original submitted SQL unchanged. |
| Multiple sorts | Ordered sort entries apply natively, use `NULLS LAST`, and stable ties retain the same row sequence across adjacent offsets. |
| Literal contains | Case-insensitive `contains` finds literal text; a `%` or `_` filter value is not interpreted as a wildcard, and quote-like input cannot change the query. |
| AND filtering | Several filters reduce the same cache by conjunction; `row_count` is the filtered count while `source_row_count` remains the complete cache count. |
| Original column metadata | `columns`, including duplicate names and `has_values`, remains the original whole-cache metadata on filtered and paged responses. |
| One group column | Ascending and descending single-column grouping uses native `NULLS LAST`. Each page emits only its represented `{value, count}` group records, and a group split across pages keeps its global filtered count. |
| Rejected grid input | Unknown keys, invalid shapes, operators, directions, column indices and value types return an input error; a subsequent ordinary page of the same result still returns its original rows and identity. |
| No query replay | Grid page/fetch requests use the retained native table only: they neither rerun submitted SQL nor create a second materialized result table. |

Exercise the query page through the MCP interface as well as the native backend call. Use separate pages to demonstrate a group spanning a page boundary, literal `%` matching, duplicate aliases and the public `rowid` name. Inspect the executed boundary or observable cache state to establish native cached-table paging rather than a Python whole-result transform. Do not treat a frontend-only sorted array, a mock database or a successful first page alone as evidence.
