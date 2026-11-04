---
atom_id: CA-D-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 8
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
    name: CA-D-673@8-WORKBENCH-ENG_DECISION--deliver-shared-query-run-and-check-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Deliver shared query Run and Check results

## Claim scope

The synchronous SQL, MCP and web Run, Page, Check, Save, Load and Schema interfaces.

## Claim

### Prose Claim

Use one shared synchronous native DuckDB and DuckPGQ connector. Serve MCP through `/caprmedio/mcp`. Public tools are `query_run`, `query_page`, `query_check`, `query_schema`, `query_save`, `worksheet_save`, `query_load` and `query_saved_list`; the web uses the same capabilities at `/caprmedio/workbench/<project_name>/run`, `/page`, `/check`, `/save`, `/worksheet-save`, `/load`, `/saved-list` and `/schema`. No queue, job, planner or second executor is required.

`query_save({sql, cursor_position?})` selects one statement at the optional UTF-16 cursor position using native SQL tokenization, writes that exact SQL as one immutable UTF-8 `.caprmedio_runtime/workbench/saved_queries/q_<uuid hex>.sql` file, and returns `saved_query_id`, `saved_query_url`, `kind: query` and the selected `sql`. `worksheet_save({sql})` writes the full script as `{"sql": "..."}` in one immutable `.caprmedio_runtime/workbench/saved_queries/w_<uuid hex>.json` file and returns the same fields with `kind: worksheet`. `query_load({reference})` accepts either ID or URL and returns `saved_query_id`, `saved_query_url`, `kind` and `sql` without executing it. `query_saved_list({limit?})` returns `{items: [{saved_query_id, saved_query_url, kind, preview, saved_at}]}`, where `preview` is a short SQL preview and `saved_at` is the filesystem modification time. Entries cover queries and Worksheets, newest first; its default limit is 20 and maximum is 1,000. At public web and HTTP MCP boundaries, construct the full URL from the actual HTTP request base URL, the declared Project name and `?query=<saved_query_id>`. Carry `project_root` when that selection was supplied. Private transport-free helpers may return storage identities, but public responses must contain the full URL; no guessed port or new non-HTTP Workbench transport is added. No deduplication, sharing, authentication, expiry or deletion workflow is added.

`query_schema({})` returns only read-only table and column metadata as `{tables: {atoms: [{name, type}], scope_units: [{name, type}]}}`; `tables.atoms` includes declared `content.*` columns. It does not query saved SQL files or execute user SQL.

Run accepts `sql`, optional UTF-16 `cursor_position` and optional `page_size` (default 100, maximum 1,000). A cursor exactly on a semicolon selects the statement to its left. It saves the selected exact SQL before execution and returns that `sql`, `saved_query_id`, `saved_query_url` and `kind` separately from `query_id`, ordered `columns` (name, native type and `has_values`), positional `rows`, exact total `row_count` and `column_count`, `offset`, `page_size` and `has_more`. It includes the saved identity on successful and query-error answers. If saving fails, it returns an explicit error and does not execute the query or promise an ID. `has_values` is computed across the complete materialized result, so it is identical on every page. For this metadata only, NULL, empty strings, empty arrays and empty objects are empty; false and zero are values. A nested object with keys is non-empty even when a nested value is null. Page accepts `query_id`, a non-negative integer `offset` and optional `page_size`, and returns the same result shape plus the original `saved_query_id`, its full `saved_query_url` and `kind`; known Page errors preserve that saved identity and URL when available. Page reads the stable materialized result; it does not rerun SQL. Check accepts `sql` and optional `cursor_position`, performs the same save-before-execute step and returns the selected `sql`, saved identity, validity and exact counts, or its query error, without sending all rows.

Preserve duplicate column names positionally. Encode ordinary JSON values losslessly; encode integers outside JavaScript's safe range and Decimal values as strings, dates/times as ISO strings and binary values as `base64:` strings. Apply conversion recursively to lists and string-keyed mappings. Non-finite numbers, non-string mapping keys and unsupported values produce a delivery error. Counts remain integers. Do not add row hashes to arbitrary SQL results.

Keep source-file errors on stderr with their source path. Return known query and page errors to their originating caller. Source files and source-derived facts remain unchanged by public queries; internal result tables are disposable cache, not a third public source table. A zero-row result sets `has_values: true` for every returned header so the full column set remains visible; pagination does not remove columns or change SQL values and counts.

## Details

`cursor_position` is an integer offset in JavaScript UTF-16 code units. Reject a Boolean, negative/out-of-range offset or a position splitting a surrogate pair as an input error before saving or executing. Convert the valid UTF-16 prefix to its UTF-8 byte length before comparing it with native DuckDB token offsets. Slice the original UTF-8 SQL at those native boundaries and decode that exact slice. A delimiter inside a native string or comment token is not a statement boundary. A cursor on a delimiter or immediately after it selects the statement ending there. Leading whitespace before a following statement belongs to that following statement; trailing whitespace or comments after the final delimiter belong to the final statement.

With no cursor, use the submitted SQL unchanged. Saving does not validate or rewrite SQL. Run and Check still use the existing one-read-query admission after saving, so invalid or multi-statement raw submissions can return a query error with their saved identity. Save Worksheet always takes the complete script.

Saved IDs contain no filename extension: `q_` plus 32 lowercase hexadecimal UUID characters identifies a query; `w_` plus the same UUID format identifies a Worksheet. The extension is derived from the ID kind. Load parses an ID or a Workbench URL to that identity; it does not fetch remote URLs or switch Projects implicitly. Invalid, unknown or malformed saved references return an explicit operation error. Bad saved files are reported on stderr; the recent list retains valid entries rather than inventing a repair or retry.

The web and MCP expose the same backend contracts. Run, Check, Save and Save Worksheet have persistent saved-file effects; their tool annotations must reflect those effects even though public SQL remains read-only. Page, schema, load and recent-list operations are reads.
