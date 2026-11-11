---
identity:
  atom_id: CA-D-673
  ref_id: CA-D-673
context:
  container:
    scope_unit: CA-SU-43
  role: Delivery
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2724
  - CA-R-2728
  - CA-R-2729
  - CA-R-2953
  - CA-R-2727
  - CA-R-2776
  - CA-R-2902
state:
  status: Active
  version: 18
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-D-673-WORKBENCH-SOLUTION--deliver-shared-query-run-and-check-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Deliver shared query Run and Check results

## Claim scope

The synchronous SQL, MCP and web Run, Page, Check, Save, Load and Schema interfaces.

## Claim

### Prose Claim

MCP is `/caprmedio/mcp`; the web interface is `/caprmedio/workbench/<project_name>`. Requests execute synchronously; no query queue, planner, scheduler or second executor is added.

`query_run({sql, cursor_position?, page_size?, preview?, save?, name?, result_delivery?, result_format?})` validates one whole query and materializes it once. Preserve its exact submitted SQL internally. `save` defaults to false; `name` is valid only with save true. `preview` is a non-negative integer cap applied with native relation.limit(N), preserving an existing LIMIT and supporting CTE and GRAPH_TABLE without rewriting SQL.

`result_delivery` is `file` by default, or explicit `inline`. `result_format` is `json_matrix` by default, or `csv` or `toon` for file delivery. A direct file-delivery Run exports the complete accepted materialized result, including any preview cap. It returns execution metadata and the completed file descriptor, without rows or full SQL. Inline delivery returns the requested bounded first page. View Run remains metadata-only; its rows are obtained by an explicit fetch.

`query_page` and `view_fetch` accept the same delivery choices alongside their existing query/View identity, offset and page size. Page size defaults to 100 and accepts 1–1,000 rows; offset is non-negative. Reject invalid sizes, offsets and unknown result IDs explicitly. Run uses that page size only for explicit inline delivery, while direct file delivery exports the accepted result. They export or return only that requested page, retain original ordered column metadata and exact total counts, and never rerun SQL. Inline responses retain positional rows for the browser grid. All responses omit automatic SQL echoes. Existing explicit query_load, View query reads and query_log_get still return requested SQL.

A result-file descriptor is `{path, format, row_count, column_count, offset, has_more}`. `path` is relative to the selected Project root and names a complete file under `.caprmedio_tmp/workbench/query_results`. Resolve it against that same trusted Project root. Use an internally generated unique filename, not SQL or a caller-supplied path. Do not put the file contents into the MCP response. Export metadata does not replace the query ID, total execution counts or ordered column metadata. Page descriptors describe the exported page; total counts describe the materialized execution. Reuse stable cached state for exports.

JSON matrix files are UTF-8 JSON objects with exactly `columns` (ordered names) and `rows` (ordered positional arrays). Preserve duplicate names and zero-row headers. CSV uses the same column order and UTF-8, CRLF records and normal quoting. Unquoted empty represents null; quoted empty represents an empty string. SQL column types remain in response metadata for matching typed readback. TOON uses the official codec for the same `{columns, rows}` value; do not convert rows to objects keyed by aliases. Arrays/objects and other values follow the existing shared result encoder. Preserve null, zero, false, Unicode, source newlines and Formal Claim text exactly.

Shared encoding preserves ordinary JSON values. Encode unsafe integers and Decimal values as strings, dates/times as ISO strings, and binary as base64: strings. Unsupported values return a delivery error. An export failure after successful execution keeps the query ID and cached result, reports outcome partial and export_error, and returns no successful path for the failed file. A partial file must not be exposed as a complete artifact. Do not rerun SQL, retry or roll back the successful result.

A Bookmark is permanent saved SQL, distinct from a saved View and the temporary query log. `query_run(save=true)` writes its exact original SQL only after the Run succeeds. A successful save adds saved_query_id, saved_query_url, kind query and optional name, not the full SQL. A later save failure preserves the result and returns outcome partial and save_error, without a saved identity unless known. Failed validation or execution creates no Bookmark.

`view_save`, `query_load` and `query_saved_list` retain their current names, ID/URL fields and kind values. View Save snapshots one query with optional name. Load explicitly returns SQL without executing it. Saved List returns recent metadata and bounded previews; it does not automatically return full SQL. Existing kind worksheet and q_/w_ items remain read-only compatibility sources. Do not rename saved entries. New saved IDs remain canonical UUIDv7. Use the existing Project Journal's date-partitioned workbench-saved-items writer and 1,000-row parts. Saved writes finish before their IDs are returned; they do not trigger Atom reindexing.

`query_check` returns validity, ordered column metadata and exact counts when available, or its query error. It returns no SQL echo, result rows or result file. Check creates no Bookmark, saved View or query-log entry. Run logs remain metadata-only NDJSON under their existing independent contract. Page, Schema, Load and List do not append a query Run log.

`query_schema` returns read-only table/column metadata for atoms, scope_units and change_log, including declared content columns and optional Status completion values. It neither executes user SQL nor accesses saved items.

Keep existing web routes `/run`, `/page`, `/check`, `/view-save`, `/load`, `/saved-list` and `/schema` below the Project page. Source errors go to stderr with their path. Public SQL does not edit source Atoms, Scope Units or source-derived facts. Result tables and exported files are disposable derived data, with separate lifetimes from Bookmarks and query history.

## Details

cursor_position is optional JavaScript UTF-16 caret metadata. Reject Boolean, negative, out-of-range or surrogate-splitting offsets before execution; it never chooses a different statement. A delimiter inside a string or comment is not a statement boundary. Always execute the complete single submitted query. Page, schema, load and list are reads. An optional name is a string; omitted or blank means unnamed and names do not change an existing saved entry.

When preview is omitted, Run applies no added preview cap. A completed Run with a later save failure returns the normal MCP/HTTP Run response (MCP is_error=false, HTTP 200), carrying the completed result metadata plus outcome: partial and save_error. This is not aggregate success; the UI must display the save failure while keeping the completed result.


## Grid page delivery

Page and View Fetch map the accepted grid request to the shared backend and deliver its ordered column metadata, positional rows or exported page, whole-result visibility metadata and exact group counts in the existing response envelope. Preserve the grid result contract without rerunning SQL in either adapter.

Generic query_run and query_page remain available for direct callers. HTTP must not construct and unwrap MCP protocol requests/results merely to reach the operation API. Reuse the existing Project selection, configured exclusions, current installed-contract checks, resource ownership and lifecycle guards. Keep transport-envelope checks in adapters and operation-argument validation in the shared backend. Preserve successful and partial results and their existing public error semantics.

### Workspace and View operation contracts

| Operation | Inputs | Result |
|---|---|---|
| `workspace_open` | `session_id` | Initialize or resume this Workspace with one initial View; return its state, canonical project_name and request-derived URL. |
| `workspace_list` | none | Known Workspace IDs for the explicit Project; no result rows. |
| `workspace_get` | `workspace_id` | Current Views, SQL, names, revisions, active View ID, result metadata, canonical project_name and request-derived Workspace URL; no rows. |
| `view_create` | `workspace_id`, `position` (`first` or `last`, default `last`), optional `name` | New stable View ID and state. |
| `view_duplicate` | `workspace_id`, `view_id` | New independent View copying query and cursor, next free name, active ID and Workspace state; no execution or copied results. |
| `view_list` | `workspace_id` | Ordered View IDs, names and result metadata; no SQL or rows. |
| `view_get` | `workspace_id`, `view_id` | One View's SQL, revision and result metadata; no rows. |
| `view_update` | `workspace_id`, `view_id`, `sql`, optional `cursor_position` (editor metadata only), required `expected_revision` | Updated View. A revision mismatch fails and leaves both the server SQL and the browser's unsynced draft intact; `cursor_position` never selects a statement. |
| `view_run` | `workspace_id`, `view_id`, optional `cursor_position` (editor metadata only), `preview`, `save`, `name` | Run the whole View only when it contains exactly one SQL statement; reject multiple statements and never select by cursor. Return success/fail, error, counts and query ID, with no rows. Existing successful Run-and-save behavior is available through `save=true`. |
| `view_check` | `workspace_id`, `view_id`, optional `cursor_position` (editor metadata only) | Check the whole View only when it contains exactly one SQL statement; reject multiple statements and never select by cursor; no query-log entry. |
| `view_fetch` | `workspace_id`, `view_id`, `offset` (default 0), `page_size` (default 100, 1..1000), optional `preview`, `result_delivery`, `result_format` | Fetch a page as a file by default or explicit inline rows; preview caps that page without rerunning SQL. |
| `view_focus` | `workspace_id`, `view_id` | Set the Workspace's active View. |
| `view_rename` | `workspace_id`, `view_id`, `name` | Update the current View name. |
| `view_remove` | `workspace_id`, `view_id` | Remove the View; reject the last View. |
| `view_save` | either `workspace_id` + `view_id`, or existing `sql` + optional `name` | Reuse saving of the View's one complete query and its saved ID/URL. The two input modes are exclusive. Saved View names/SQL are snapshots, not renamed in place. |
| `query_log_list` | optional `limit` (default 20, 1..1000) | Recent retained log records. |
| `query_log_get` | `log_id` | One retained log record. |

Use the existing UUID generator for new View IDs. Keep Workspace documents under `.caprmedio_runtime/workbench/workspaces`; they contain no duplicate chat history or result rows.

### Workspace Project name delivery

The public Workspace adapter obtains `project_name` from the selected Project's validated settings through the existing ProjectSelection settings/name reader, for both HTTP and MCP. Workspace persistence and other tool inputs remain unchanged.
