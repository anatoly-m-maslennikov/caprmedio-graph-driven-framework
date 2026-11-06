---
atom_id: CA-M-468
ref_id: CA-M-468
container:
  scope_unit: CA-SU-46
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  method_for:
  - CA-R-2727
  - CA-R-2728
  - CA-R-2776
status: Active
version: 4
updated_at: 2026-11-06 21:07:42 +0400
carrier_destination:
  file:
    name: CA-M-468-WORKBENCH_FRONTEND-ENG_DECISION--use-a-simple-sql-editor-for-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Use a simple SQL editor for Workbench

## Claim scope

Workbench SQL editing, schema completion and query actions.

## Claim

Use CodeMirror 6 with its SQL language support for a text-only SQL editor and autocomplete from read-only `query_schema` metadata for actual atoms, scope_units and declared `content.*` columns. Content column names keep dots between path levels and use snake_case within each segment, for example `content.claim.prose_claim` and `content.claim.formal_claim`; quote the resulting SQL identifiers as needed and do not expose space-based Content names.

Keep one query in each View. Preserve quoted strings, comments and CTEs, but reject multiple SQL statements instead of selecting a statement at the cursor. The editor sends the whole View query and its UTF-16 cursor position only for editing context; CodeMirror provides editing, highlighting and completion, not SQL validation or a second selector. Do not write a homegrown SQL parser. Bind `Cmd+Enter` to Run and `Shift+Cmd+Enter` to Check; both target the whole current View query. Run and Check do not save; Run & Save saves only after a successful Run, and Save View saves the whole current query text. Do not execute SQL while building autocomplete suggestions.


The read-only schema metadata may include optional distinct non-null values for the actual Header Status column. Completion recognizes a single-quoted equality prefix on that declared column, inserts the matching escaped value such as `Active` without a duplicate closing quote, and never executes user SQL or creates a saved record. Fetch metadata through `query_schema`; typing a completion prefix does not execute user SQL or save a query.

Use the DuckDB dialect of `@dlh.io/dlh-sql-formatter` for the editor's explicit Format action, with two-space indentation, leading commas, lowercase keywords and a newline before the semicolon. Apply the shared query-writing style with a small token-aware adapter using the existing CodeMirror SQL parser: uppercase SELECT keywords and keep FROM and WHERE with their following expression when no comment separates them. Do not implement another SQL parser or formatter. Preserve existing expressions, identifiers, strings and comments. Return formatting errors without replacing the editor input.

