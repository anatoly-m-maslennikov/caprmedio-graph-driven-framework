---
atom_id: CA-M-468
ref_id: CA-M-468
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Active
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
version: 2
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2727
  - CA-R-2728
  - CA-R-2776
carrier_destination:
  file:
    name: CA-M-468-WORKBENCH_FRONTEND-ENG_DECISION--use-a-simple-sql-editor-for-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
updated_at: 2026-11-05 01:40:28 +0400
container:
  scope_unit: CA-SU-46
---

## Summary

Use a simple SQL editor for Workbench

## Claim scope

Workbench SQL editing, schema completion and query actions.

## Claim

Use CodeMirror 6 with its SQL language support for a text-only SQL editor and autocomplete from read-only `query_schema` metadata for actual atoms, scope_units and declared `content.*` columns. Quote names with spaces. Allow multiple statements separated by semicolons while preserving quoted strings, comments and dollar-quoted strings. The editor sends the full Worksheet and its UTF-16 cursor position. Only the backend selects statement boundaries using native DuckDB tokenization; CodeMirror provides editing, highlighting and completion, not SQL validation or a second selector; a cursor exactly on a semicolon selects the statement to its left; do not write a homegrown SQL parser. Bind `Cmd+Enter` to Run and `Shift+Cmd+Enter` to Check; these are different operations and target the statement at the cursor. Buttons Run, Check and Save target the same active statement; Save Worksheet targets the whole script. Do not execute SQL while building autocomplete suggestions.

The schema metadata may include optional `values` for `atoms.status`, populated from distinct non-null indexed status values. Completion recognizes a single-quoted `status = 'Act` prefix, inserts the matching escaped quoted value such as `Active`, and does not execute SQL or create a saved record while completing.

Use the existing read-only schema metadata for value hints. For atoms.status, the metadata may include distinct non-null indexed status values. Offer local completion for a single-quoted equality prefix such as `status = 'Act`, inserting the escaped quoted value and avoiding a duplicate closing quote. Fetch metadata through query_schema; typing a completion prefix does not execute user SQL or save a query.
