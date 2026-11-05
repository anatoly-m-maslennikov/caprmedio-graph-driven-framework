---
atom_id: CA-R-2728
ref_id: CA-R-2728
container:
  scope_unit: CA-SU-43
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Active
version: 6
updated_at: 2026-11-05 14:23:38 +0400
carrier_destination:
  file:
    name: CA-R-2728-WORKBENCH-RULE--provide-native-sql-query-capability-over-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Provide native SQL query capability over query projection

## Claim scope

Queries over the synchronized Atom query Projection.

## Claim

### Prose Claim

The query capability **must**:

- keep SQL execution read-only for Atom and Scope Unit source files and the query Projection. Only explicit `query_run` with `save: true` and `view_save` append saved-item records to the configured Project Journal.
- execute each public query synchronously and return its result or error to its originating MCP or web request. A query may contain multiple statements; Run and Check execute the statement selected by the optional cursor position, with a cursor exactly on a semicolon selecting the statement to its left, while View save preserves the whole script.
- accept native SQL according to the selected SQL engine's semantics.
- expose the parsed Header and mapped Content Properties without flattening their source distinctions.
- provide a read-only `query_schema({})` operation returning `{tables: {atoms: [{name, type, values?}], scope_units: [{name, type}]}}`; `tables.atoms` includes declared `content.*` columns. For `atoms.status`, optional `values` contains distinct non-null indexed status values. This metadata is read when the schema is fetched, not during `query_run`, and does not read saved-item Journal entries, execute user SQL or create a saved record. A single-quoted prefix such as `status = 'Act` may complete to a properly escaped `Active` value.
- provide `query_run({sql, cursor_position?, page_size?, preview?, save?, name?})`, `view_save({sql, name?})`, `query_load({reference})` and `query_saved_list({limit?})`. `query_run` saves the selected statement only when `save: true` and the Run succeeds; it may receive an optional name only then. `view_save` saves the whole script and may receive an optional name only at creation. Run without save, Check and Page do not save or append Journal records. `query_load` accepts an ID or URL; and `query_saved_list` returns recent query and View entries with `saved_query_id`, `saved_query_url`, `kind`, optional `name`, `preview` and `saved_at`. New entries use `kind: query` or `kind: view`, a dedicated Project Journal with canonical unprefixed UUIDv7 IDs, exact `sql`, optional `name` and `saved_at`, and 1,000-row date-partitioned `workbench-saved-items` parts through the existing writer. Existing Journal entries with historical `kind: worksheet` and existing `q_<hex>.sql` and `w_<hex>.json` files remain read-only fallback sources; do not rewrite or migrate them. Saved entries are not renamed.
- use the selected SQL engine for SQL semantics and its native tokenization for statement boundaries rather than introduce another SQL-like parser or evaluator.
- return a query error for invalid SQL; it **must not** return an empty successful result instead.
- keep source-file errors distinct from SQL errors.
