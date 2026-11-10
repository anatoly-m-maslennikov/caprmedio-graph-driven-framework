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
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Query Processing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 8
relations:
  evaluation_for:
  - CA-M-462
  - CA-R-2953
  - CA-O-240
state:
  status: Active
  version: 6
  updated_at: 2026-11-10 20:47:54 +0400
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

Against real DuckDB materialized results and the MCP boundary, verify `query_page` and applicable `view_fetch`. Zero-based grid indices address original positions despite duplicate/dotted aliases; public `rowid` order comes from a hidden snapshot ordinal. CTE, DuckPGQ and preview execute original SQL once through the same ordinal CTAS; original SQL is retained for execution/Bookmark but omitted from ordinary Run/Page responses.

Verify native ordered sorts with `NULLS LAST` and stable ties, literal case-insensitive `contains` where `%`/`_` are not wildcards, conjunctive filters, original whole-cache column metadata, and single-column group page records with global filtered counts across page splits. Invalid grid keys/shapes/operators/directions/indices/types return input error without damaging the result identity or a later normal page. Page/fetch uses only the retained table: no replay or second cache.

Exercise MCP plus native calls, real page boundaries, cache observability and completed exports/explicit inline pages. JSON matrix/CSV/TOON decode to the selected positional values/columns with exact counts/group metadata; export never reruns SQL.
