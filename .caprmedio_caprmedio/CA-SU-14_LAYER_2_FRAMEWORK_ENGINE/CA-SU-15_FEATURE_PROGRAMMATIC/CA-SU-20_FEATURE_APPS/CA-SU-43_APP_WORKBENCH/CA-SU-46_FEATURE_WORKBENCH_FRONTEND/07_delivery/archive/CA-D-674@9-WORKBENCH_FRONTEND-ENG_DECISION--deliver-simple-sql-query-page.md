---
atom_id: CA-D-674
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Archived
version: 9
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2727
carrier_destination:
  file:
    name: CA-D-674@9-WORKBENCH_FRONTEND-ENG_DECISION--deliver-simple-sql-query-page.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/07_delivery/archive
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Deliver a simple SQL query page through the shared connector

## Claim scope

The Workbench frontend and its same-listener HTTP delivery.

## Claim

### Prose Claim

Build the Workbench frontend with Svelte, TypeScript and Vite. Serve its static production assets through the existing Python application at `/caprmedio/workbench/<project_name>`; Node is a build dependency, not a second runtime server.

Provide a modern, minimal technical UI with selectable Light (Day), Dark (Night) and System modes, remembering the selected mode. Name each editor window a Worksheet. Provide tabs for multiple SQL inputs, keep the whole script and tab state in browser local storage every 5 seconds and restore them on load, and ask before closing an unsaved tab or window. The standard browser `beforeunload` warning is allowed; flush the latest local draft on `pagehide` and `beforeunload` when possible. Provide text-only font zoom presets `80`, `90`, `100`, `110`, `125`, `150` and `200` percent for all text, including editor text, headings, tabs, menus, buttons and result/status text; remember the selected preset and do not scale the whole layout or icons.

Provide a CodeMirror SQL editor with a collapsible editor toggle whose state is restored, Run, Check, Save and Save Worksheet controls, exact counts, query errors and ordinary result rows with Previous and Next page controls. A Worksheet may contain multiple SQL statements separated by semicolons; the active statement is the one at the cursor, while Save Worksheet saves the whole script. Use shared components from a small component palette. Bind `Cmd+Enter` to Run and `Shift+Cmd+Enter` to Check; these shortcuts invoke different operations on the active statement. Buttons Run, Check and Save target the active statement. Keep display formatting, page navigation and UI state in the frontend; the database executes SQL filtering, sorting and aggregation.

Use read-only `query_schema({})` metadata, returned as `{tables: {atoms: [{name, type}], scope_units: [{name, type}]}}`, for autocomplete of actual `atoms`, `scope_units` and declared `content.*` columns, including quoted names. Do not query saved SQL files to build completion suggestions. A URL `?query=<saved_query_id>` loads either a saved query or Worksheet without executing it and preserves the `project_root` parameter. Open Saved accepts an ID or URL and opens it in the current Workbench browser context. Show a recent combined query/Worksheet list from `query_saved_list`.

Run, Check and Save save the exact active statement through the shared connector before execution or completion. The answer exposes `saved_query_id`, `saved_query_url`, `kind` and the actual selected `sql` separately from a materialized result `query_id`; query errors include the saved identity and URL. Save Worksheet saves the whole editor script as a Worksheet. A save failure shows an explicit error and prevents execution and does not promise an ID. Explicit save, Worksheet save, load and list use the same shared contracts as MCP; the frontend does not add sharing, authentication, deduplication, retry, repair, rollback, expiry or deletion workflows.

The frontend receives `columns[].has_values` computed over the complete materialized result. For this metadata only, NULL, empty strings, empty arrays and empty objects are empty; false and zero are values, and a nested object with keys is non-empty even when a nested value is null. For a non-empty result, hide only fully empty columns (`has_values: false`) while preserving row and column counts and all SQL values. For a zero-row result, the connector sets `has_values: true` for every returned column so all headers remain visible. The same column metadata and visibility decision applies to every page. Content column names remain the lowercase business-language names returned by SQL, including spaces in names such as `content.claim.prose claim`.

Use `/caprmedio/workbench/<project_name>/run`, `/caprmedio/workbench/<project_name>/page`, `/caprmedio/workbench/<project_name>/check`, `/caprmedio/workbench/<project_name>/save`, `/caprmedio/workbench/<project_name>/worksheet-save`, `/caprmedio/workbench/<project_name>/load`, `/caprmedio/workbench/<project_name>/saved-list` and `/caprmedio/workbench/<project_name>/schema` for the shared connector. POST `/save`, `/worksheet-save`, `/load` and `/saved-list` use the same MCP contracts; POST `/schema` accepts `{}` and returns the same table/column metadata. Fetch only the requested result page. Preserve positional values and duplicate column names. Show loading and error states and accessible labels for controls. Do not add custom TABLE, DOC or TREE modes, a second query evaluator or a separate web service.

When the frontend build is missing, keep the query API and MCP available. The Workbench page returns HTTP 503 with an explicit build-required error; do not build assets or start a frontend server automatically.

For the current Project, the page is `/caprmedio/workbench/caprmedio`. Keep shared static assets under `/caprmedio/workbench/assets`. The frontend sends Run, Page and Check requests under its current Project page path. The URL's Project name must match the existing selected Project; a mismatched name returns HTTP 404.

Keep the result table in a bounded scrolling region, with visible column headers and separately scrollable long cell values. Preserve every row and value; scrolling changes presentation, not the query result.
