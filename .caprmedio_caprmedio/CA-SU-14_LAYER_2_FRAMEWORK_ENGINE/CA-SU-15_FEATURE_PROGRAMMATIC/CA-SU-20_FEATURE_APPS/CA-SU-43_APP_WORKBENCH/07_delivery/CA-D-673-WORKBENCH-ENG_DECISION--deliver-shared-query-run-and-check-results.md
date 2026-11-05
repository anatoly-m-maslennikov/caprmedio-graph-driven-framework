---
atom_id: CA-D-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 12
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
updated_at: 2026-11-05 14:23:38 +0400
---

## Summary

Deliver shared query Run and Check results

## Claim scope

The synchronous SQL, MCP and web Run, Page, Check, Save, Load and Schema interfaces.

## Claim

### Prose Claim

Use one shared synchronous native DuckDB and DuckPGQ connector. Serve MCP through /caprmedio/mcp. Public query/View tools include query_run, query_page, query_check, query_schema, view_save, query_load and query_saved_list. There is no separate query_save tool and no save-only query endpoint. The web uses the same capabilities at /caprmedio/workbench/<project_name>/run, /page, /check, /view-save, /load, /saved-list and /schema. No queue, job, planner or second executor is required.

query_run({sql, cursor_position?, page_size?, preview?, save?, name?}) selects one statement at the optional UTF-16 cursor position using native SQL tokenization, executes it once and returns the selected SQL exactly as received, query_id, ordered columns, positional rows, exact counts, offset, page size and has_more. preview is an optional non-negative integer cap: return at most that many rows while preserving any existing SQL LIMIT. Apply the cap through DuckDB's relation.limit(N), not text or AST rewriting, and support GRAPH_TABLE and CTE queries. Counts and pagination describe the previewed execution.

save is an optional boolean, default false. name is accepted only when save is true. When save is false or omitted, query_run has no Journal effect. When save is true, it may accept name and writes one saved query only after the Run succeeds, using the exact selected SQL. A successful save adds saved_query_id, saved_query_url, kind: query and optional name to the ordinary Run response. If this save fails after the query result is complete, preserve the rows and query_id and return outcome: partial with save_error; do not return a saved ID unless one is known, and do not retry or roll back. A query or selection failure creates no saved entry.

query_page accepts query_id, non-negative offset and optional page_size, and returns the same result shape from stable materialized state without rerunning SQL or persisting anything. Keep subsequent pages stable while their materialized state is retained. query_check accepts sql and optional cursor_position, returns selected SQL, validity and exact counts or its query error, without saving or appending a Journal record. Run, Check and Page have no persistent Journal effect except the explicit save requested on a successful query_run.

view_save({sql, name?}) writes the full script as a View Journal entry and returns saved_query_id, saved_query_url, kind: view, exact sql and optional name. query_load({reference}) accepts either ID or URL and returns saved_query_id, saved_query_url, kind, exact sql and optional name without executing it. query_saved_list({limit?}) returns {items: [{saved_query_id, saved_query_url, kind, preview, name?, saved_at}]}, newest first, default 20, maximum 1,000. New saved entries use a canonical unprefixed UUIDv7 ID and Journal fields saved_query_id, kind, sql, optional name and saved_at. Existing Journal entries with kind worksheet and existing q_/w_ runtime items remain readable as historical compatibility sources; new entries never use kind worksheet. Use the existing Journal writer's 1,000-row parts with the reserved workbench-saved-items prefix and date partition, approximately under concurrent writes rather than one unbounded file. Build public URLs from the actual HTTP request base URL, declared Project name and ?query=<saved_query_id>; carry project_root when supplied. Do not rename saved items.

query_schema({}) returns only read-only {tables: {atoms: [{name, type, values?}], scope_units: [{name, type}]}} metadata. It includes declared content.* columns and optional distinct non-null indexed atoms.status values for completion. It does not read saved items, execute user SQL or create a saved record.

Preserve duplicate column names positionally. Encode ordinary JSON values losslessly; encode unsafe integers and Decimal values as strings, dates/times as ISO strings and binary as base64: strings. Unsupported values produce a delivery error. Keep source-file errors on stderr with their source path. Public SQL does not edit Atom or Scope Unit sources or source-derived facts; internal result tables are disposable cache. A zero-row result keeps every returned header visible. Pagination does not change SQL values or counts. Saved-item Journal writes are excluded from source watching.

## Details

cursor_position is a JavaScript UTF-16 code-unit offset. Reject Boolean, negative, out-of-range or surrogate-splitting offsets before selecting/executing. Convert the valid prefix to UTF-8 byte length for native token boundaries. A delimiter inside a string or comment is not a boundary. With no cursor, use the submitted SQL unchanged. The web and MCP expose the same contracts. Page, schema, load and list are reads. An optional name is a string; omitted or blank means unnamed and names do not change an existing saved entry.

When preview is omitted, Run applies no added preview cap. A completed Run with a later save failure returns the normal MCP/HTTP Run response (MCP is_error=false, HTTP 200), carrying all completed Run fields plus outcome: partial and save_error. This is not aggregate success; the UI must display the save failure while keeping the completed result.
