---
atom_id: CA-R-2728
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2728@4-WORKBENCH-RULE--provide-native-sql-query-capability-over-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-05 01:40:28 +0400
---
## Summary

Provide native SQL query capability over the query Projection

## Claim scope

Queries over the synchronized Atom query Projection.

## Claim

### Prose Claim

The query capability **must**:

- keep SQL execution read-only for Atom and Scope Unit source files and the query Projection. Explicit saves and the automatic saves before Run and Check append saved-item records separately to the configured Project Journal.
- execute each public query synchronously and return its result or error to its originating MCP or web request. A query may contain multiple statements; Run and Check execute the statement selected by the optional cursor position, with a cursor exactly on a semicolon selecting the statement to its left, while Worksheet save preserves the whole script.
- accept native SQL according to the selected SQL engine's semantics.
- expose the parsed Header and mapped Content Properties without flattening their source distinctions.
- provide a read-only `query_schema({})` operation returning `{tables: {atoms: [{name, type, values?}], scope_units: [{name, type}]}}`; `tables.atoms` includes declared `content.*` columns so the editor can autocomplete actual tables and quoted column names. For `atoms.status`, optional `values` contains distinct non-null indexed status values. This metadata is read when the schema is fetched, not during `query_run`, and does not read saved-item Journal entries, execute user SQL or create a saved record. A single-quoted prefix such as `status = 'Act` may complete to a properly escaped `Active` value.
- provide `query_save({sql, cursor_position?, name?})`, `worksheet_save({sql, name?})`, `query_load({reference})` and `query_saved_list({limit?})`. `query_save` saves the selected statement and may receive an optional name only at creation; `worksheet_save` saves the whole script and may receive an optional name only at creation; Run and Check save unnamed. `query_load` accepts an ID or URL; and `query_saved_list` returns recent query and Worksheet entries with `saved_query_id`, `saved_query_url`, `kind`, optional `name`, `preview` and `saved_at`. The default list limit is 20 and the maximum is 1,000. New entries use a dedicated Project Journal with canonical unprefixed UUIDv7 IDs, `kind`, exact `sql`, optional `name` and `saved_at`; use 1,000-row date-partitioned `workbench-saved-items` parts through the existing writer. Existing `q_<hex>.sql` and `w_<hex>.json` files remain read-only fallback sources; do not rewrite or migrate them. Saved entries are not renamed.
- use the selected SQL engine for SQL semantics and its native tokenization for statement boundaries rather than introduce another SQL-like parser or evaluator.
- return a query error for invalid SQL; it **must not** return an empty successful result instead.
- keep source-file errors distinct from SQL errors.
