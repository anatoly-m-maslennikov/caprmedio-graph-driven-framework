---
atom_id: CA-D-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 10
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2724
  - CA-R-2728
  - CA-R-2729
carrier_destination:
  file:
    name: CA-D-673-WORKBENCH-ENG_DECISION--deliver-shared-query-run-and-check-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery
---

## Summary

Deliver shared query Run and Check results

## Claim scope

The synchronous SQL, MCP and web Run, Page, Check, Save, Load and Schema interfaces.

## Claim

### Prose Claim

Use one shared synchronous native DuckDB and DuckPGQ connector. Serve MCP through `/caprmedio/mcp`. Public tools are `query_run`, `query_page`, `query_check`, `query_schema`, `query_save`, `worksheet_save`, `query_load` and `query_saved_list`; the web uses the same capabilities at `/caprmedio/workbench/<project_name>/run`, `/page`, `/check`, `/save`, `/worksheet-save`, `/load`, `/saved-list` and `/schema`. No queue, job, planner or second executor is required.

`query_save({sql, cursor_position?, name?})` selects one statement at the optional UTF-16 cursor position using native SQL tokenization, writes a new entry to a dedicated append-only Journal under the configured Project Journal root, and returns `saved_query_id`, `saved_query_url`, `kind: query`, the selected `sql` and optional `name`. `worksheet_save({sql, name?})` writes the full script as a Worksheet Journal entry and returns the same fields with `kind: worksheet`. New saved entries use a canonical unprefixed UUIDv7 ID and Journal fields `saved_query_id`, `kind`, `sql`, optional `name` and `saved_at`. Use the existing Journal writer's 1,000-row parts with the reserved `workbench-saved-items` prefix and date partition, approximately under concurrent writes rather than one unbounded file. `query_load({reference})` accepts either ID or URL and returns `saved_query_id`, `saved_query_url`, `kind`, `sql` and optional `name` without executing it. `query_saved_list({limit?})` returns `{items: [{saved_query_id, saved_query_url, kind, preview, name?, saved_at}]}`, newest first, default 20, maximum 1,000. Build public URLs from the actual HTTP request base URL, declared Project name and `?query=<saved_query_id>`; carry `project_root` when supplied. Existing `q_<hex>.sql` and `w_<hex>.json` runtime files remain read-only fallback sources for load/list; preserve their IDs and URLs, and do not rewrite or migrate them. No saved-item rename, deduplication, sharing, authentication, expiry or deletion workflow is added.

`query_schema({})` returns only read-only `{tables: {atoms: [{name, type, values?}], scope_units: [{name, type}]}}` metadata. It includes declared `content.*` columns and optional distinct non-null indexed `atoms.status` values for completion. It is not produced by `query_run`, does not read saved items, execute user SQL or create a saved record.

Run accepts `sql`, optional UTF-16 `cursor_position` and optional `page_size` (default 100, maximum 1,000). It selects one statement, materializes the complete native read-only result once and returns the selected `sql`, `query_id`, ordered columns, positional rows, exact counts, offset, page size and `has_more`; it does not save SQL, append a Journal record or return a saved identity. Query errors return through the originating caller without inventing selected SQL when selection failed. Page accepts `query_id`, non-negative `offset` and optional `page_size`, returns the same result shape from stable materialized state without rerunning SQL or persisting anything. Check accepts `sql` and optional `cursor_position`, returns selected SQL, validity and exact counts or its query error, without saving or appending a Journal record. Run, Check and Page are read-only; only explicit Save and Save Worksheet have persistent Journal effects.

Preserve duplicate column names positionally. Encode ordinary JSON values losslessly; encode unsafe integers and Decimal values as strings, dates/times as ISO strings and binary as `base64:` strings. Unsupported values produce a delivery error. Keep source-file errors on stderr with their source path. Public SQL does not edit Atom or Scope Unit sources or source-derived facts; internal result tables are disposable cache. A zero-row result keeps every returned header visible. Pagination does not change SQL values or counts.

## Details

`cursor_position` is JavaScript UTF-16 code-unit offset. Reject Boolean, negative, out-of-range or surrogate-splitting offsets before selecting/executing. Convert the valid prefix to UTF-8 byte length for native token boundaries. A delimiter inside a string/comment is not a boundary. With no cursor, use the submitted SQL unchanged. The web and MCP expose the same contracts. Saved-item Journal writes are excluded from source watching. Page, schema, load and list are reads. An optional name is a string; omitted or blank means unnamed and names do not change an existing saved entry.
