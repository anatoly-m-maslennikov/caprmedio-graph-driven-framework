---
identity:
  atom_id: CA-D-673
  ref_id: CA-D-673@15-draft
context:
  container:
    scope_unit: CA-SU-43
  role: Delivery
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2724
  - CA-R-2728
  - CA-R-2729
state:
  status: Draft
  version: 15
  updated_at: 2026-11-08 20:10:59 +0400
destination:
  file:
    name: CA-D-673@15-draft-WORKBENCH-SOLUTION--deliver-shared-query-run-and-check-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/draft/engine-refinement-20261108
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

Use one shared synchronous native DuckDB and DuckPGQ connector. Serve MCP through /caprmedio/mcp. Public query/View tools include query_run, query_page, query_check, query_schema, view_save, query_load and query_saved_list. There is no separate query_save tool and no save-only query endpoint. The web uses the same capabilities at /caprmedio/workbench/<project_name>/run, /page, /check, /view-save, /load, /saved-list and /schema. No queue, job, planner or second executor is required.

query_run({sql, cursor_position?, page_size?, preview?, save?, name?}) admits one complete SQL query using native SQL tokenization, rejects multiple statements, executes the query once and returns its SQL exactly as received, query_id, ordered columns, positional rows, exact counts, offset, page size and has_more. preview is an optional non-negative integer cap: return at most that many rows while preserving any existing SQL LIMIT. Apply the cap through DuckDB's relation.limit(N), not text or AST rewriting, and support GRAPH_TABLE and CTE queries. Counts and pagination describe the previewed execution.

save is an optional boolean, default false. name is accepted only when save is true. When save is false or omitted, query_run has no Journal effect. When save is true, it may accept name and writes one saved query only after the Run succeeds, using the exact submitted query SQL. A successful save adds saved_query_id, saved_query_url, kind: query and optional name to the ordinary Run response. If this save fails after the query result is complete, preserve the rows and query_id and return outcome: partial with save_error; do not return a saved ID unless one is known, and do not retry or roll back. A query or validation failure creates no saved entry.

query_page accepts query_id, non-negative offset, optional page_size and an optional request-local grid specification, and returns the same result shape from stable materialized state without rerunning SQL or persisting anything. Keep subsequent pages stable while their materialized state is retained. query_check accepts sql and optional cursor_position, returns submitted SQL, validity and exact counts or its query error, without saving or appending a Journal record. Run, Check and Page have no persistent Journal effect except the explicit save requested on a successful query_run.

view_save({sql, name?}) writes the View query text as a View Journal entry and returns saved_query_id, saved_query_url, kind: view, exact sql and optional name. query_load({reference}) accepts either ID or URL and returns saved_query_id, saved_query_url, kind, exact sql and optional name without executing it. query_saved_list({limit?}) returns {items: [{saved_query_id, saved_query_url, kind, preview, name?, saved_at}]}, newest first, default 20, maximum 1,000. New saved entries use a canonical unprefixed UUIDv7 ID and Journal fields saved_query_id, kind, sql, optional name and saved_at. Existing Journal entries with kind worksheet and existing q_/w_ runtime items remain readable as historical compatibility sources; new entries never use kind worksheet. Use the existing Journal writer's 1,000-row parts with the reserved workbench-saved-items prefix and date partition, approximately under concurrent writes rather than one unbounded file. Build public URLs from the actual HTTP request base URL, declared Project name and ?query=<saved_query_id>; carry project_root when supplied. Do not rename saved items.

query_schema({}) returns only read-only {tables: {atoms: [{name, type, values?}], scope_units: [{name, type}], change_log: [{name, type}]}} metadata. It includes declared `content.*` columns and actual Header Status columns exposed by `query_schema`. It does not read saved items, execute user SQL or create a saved record.

Preserve duplicate column names positionally. Encode ordinary JSON values losslessly; encode unsafe integers and Decimal values as strings, dates/times as ISO strings and binary as base64: strings. Unsupported values produce a delivery error. Keep source-file errors on stderr with their source path. Public SQL does not edit Atom or Scope Unit sources or source-derived facts; internal result tables are disposable cache. A zero-row result keeps every returned header visible. Pagination does not change cached SQL values. For a fixed grid specification it preserves the same filtered count; the original row count remains available separately. Saved-item Journal writes do not trigger Atom or Scope Unit projection refreshes, though their observed filesystem changes may appear in the technical change log.

## Details

cursor_position is optional JavaScript UTF-16 caret metadata. Reject Boolean, negative, out-of-range or surrogate-splitting offsets before execution; it never chooses a different statement. A delimiter inside a string or comment is not a statement boundary. Always execute the complete single submitted query. The web and MCP expose the same contracts. Page, schema, load and list are reads. An optional name is a string; omitted or blank means unnamed and names do not change an existing saved entry.

When preview is omitted, Run applies no added preview cap. A completed Run with a later save failure returns the normal MCP/HTTP Run response (MCP is_error=false, HTTP 200), carrying all completed Run fields plus outcome: partial and save_error. This is not aggregate success; the UI must display the save failure while keeping the completed result.


## Grid page delivery

Page and View Fetch may apply one request-local grid specification to the existing materialized result. Column references are zero-based positions so duplicate or dotted display names remain unambiguous. The shared backend resolves cached physical columns, binds filter values, applies filters and grouping/sort order before paging, and returns positional rows. It does not rewrite or rerun the submitted SQL, create a transformed result cache or load the full result in the browser. Group metadata covers groups present on the returned page and carries each group's exact count over all matching rows. The original whole-materialized-result column visibility metadata remains unchanged.

Standalone and embedded pages use the same backend Workspace/View operations. Generic query_run and query_page remain available for direct MCP/HTTP callers. Current Views contain one query, and saved historical text remains readable without silently executing only part of it.

MCP and HTTP call the same backend operation API. HTTP must not construct and unwrap MCP protocol requests/results merely to reach that backend. Reuse the existing Project selection, configured exclusions, current installed-contract checks, resource ownership and lifecycle guards for both transports. Keep transport-envelope checks in the adapters and operation-argument validation in the shared backend. Preserve successful and partial results and their existing public error semantics.
