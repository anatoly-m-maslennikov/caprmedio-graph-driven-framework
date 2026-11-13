---
identity:
  atom_id: CA-M-468
  ref_id: CA-M-468@7
context:
  container:
    scope_unit: CA-SU-46
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Authoring <+ Query Authoring <+ SQL
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2727
  - CA-R-2728
  - CA-R-2776
state:
  status: archived
  version: 7
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-468@7-WORKBENCH_FRONTEND-DECISION--use-a-simple-sql-editor-for-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method/099_archived
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---
## Summary

Use a simple SQL editor for Workbench

## Claim scope

Workbench SQL editing, schema completion and query actions.

## Claim

### Prose Claim

Use CodeMirror 6 SQL support and read-only `query_schema({})` metadata: `atoms` name/type/optional values, `scope_units` name/type, and technical `change_log` only `observed_at`, `operation`, `old_path`, `new_path`. Complete actual tables, declared dotted snake_case `content.*` columns and quoted identifiers as needed; do not read saved SQL for suggestions or expose space-based Content names.

Each Tab holds a SQL script. Preserve quotes, comments and CTEs and distinguish delimiters inside them. Send the whole script or explicitly selected statements for Run or Check under CA-R-2728. CodeMirror supplies editing, highlighting and completion. Cmd+Enter runs and Shift+Cmd+Enter checks; Run & Save follows successful Run and Save snapshots complete text. Completion never executes SQL, saves or changes results. On a single-quoted equality prefix for actual Header Status, offer metadata value with correct escaping/closing quote.

Format uses DuckDB dialect `@dlh.io/dlh-sql-formatter` 1.3.0 through a small token-aware adapter and existing CodeMirror parser: two-space indent, leading commas, uppercase SELECT, lowercase clauses, newline before semicolon, with FROM/WHERE attached to following expression absent a separating comment. Preserve expressions/identifiers/strings/comments/CTEs/nesting. Apply normal editor change path; accepted formatting is idempotent. On failure show error and preserve editor/results. Do not add a parser/formatter/backend capability; native execution verification remains future, not run.
