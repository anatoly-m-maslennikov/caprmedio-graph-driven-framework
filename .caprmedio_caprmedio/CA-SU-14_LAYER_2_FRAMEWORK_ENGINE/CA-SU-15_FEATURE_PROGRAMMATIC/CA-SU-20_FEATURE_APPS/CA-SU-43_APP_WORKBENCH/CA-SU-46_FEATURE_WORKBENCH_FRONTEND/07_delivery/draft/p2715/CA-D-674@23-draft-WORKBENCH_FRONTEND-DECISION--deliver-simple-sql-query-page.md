---
identity:
  atom_id: CA-D-674
  ref_id: CA-D-674@23-draft
context:
  container:
    scope_unit: CA-SU-46
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2727
  - CA-R-2952
state:
  status: Draft
  version: 23
  updated_at: 2026-11-08 20:06:18 +0400
destination:
  file:
    name: CA-D-674@23-draft-WORKBENCH_FRONTEND-DECISION--deliver-simple-sql-query-page.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/07_delivery/draft/p2715
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---


## Summary

Deliver a simple SQL query page through the shared connector

## Claim scope

The Workbench frontend and its same-listener HTTP delivery.

## Claim

With no saved explicit browser preference, use Theme = System, Interface text zoom = 100%, Content text zoom = 100% and Interface zoom = 100%.

### Prose Claim

Compact density uses smaller buttons, padding and gaps. Settings text may be larger for readability; both text zooms remain independent.

Build the Workbench frontend with Svelte, TypeScript and Vite. Serve its static production assets through the existing Python application at /caprmedio/workbench/<project_name>; Node is a build dependency, not a second runtime server.

Provide a compact, modern, minimal technical UI with selectable Light (Day), Dark (Night) and System modes, remembering the selected mode. Name each editor window a View. Show Workbench and the selected Project name in the top header. Put Settings and Saved Queries and Views at the top of that header, on the right at the same level as Workbench. Keep current View tabs in the workspace below. Use the available window width instead of a centered fixed-width workspace. Compact the full control area from the Workbench title through the result statistics and Cell content controls; at 100% scale, target half the height of the previous layout shown at 80%. Reduce header height, logo and button padding, and inter-control gaps while preserving readable text, accessible controls and text-only zoom; do not add a breakpoint framework. Show each available hotkey inside its action button or immediately beside it. Keep the Settings panel hidden initially; apply Theme, Interface text zoom, Content text zoom, Interface zoom and density preferences on page load even while it is hidden. Provide Compact and Comfortable density settings; Compact is the default only when the URL carries the explicit `embedded=1` marker and Comfortable is the default for an ordinary standalone URL. Saved explicit browser preferences win. The Operator selects the setting; do not detect physical screen size or infer embedding from Workspace presence. Keep Text zoom independent from Density and Interface zoom. Provide Interface zoom using the existing fixed text-zoom preset values for whole-interface scaling, remember it in browser local storage, and keep it independent from text-only zoom and Density. Use the full Query editor header panel as the single collapse control, with pale Hide editor or Show editor text on the right. Keep it keyboard-accessible and remove the separate toolbar toggle. Keep the current query text and tab state in browser local storage every 5 seconds and restore them on load, and ask before closing an unsaved tab or window. The standard browser beforeunload warning is allowed; flush the latest local draft on pagehide and beforeunload when possible. Provide independent Interface text zoom and Content text zoom, each with presets 80, 90, 100, 110, 125, 150 and 200 percent. Interface text zoom scales titles, tabs, menus, buttons, labels, Settings and column headers/types. Content text zoom scales query text, result cells and full-value text. Remember both settings locally. Neither changes layout or icon scale; whole-Interface zoom remains separate. Preserve the old saved text-zoom value as the initial value of both settings when upgrading existing browser preferences.

Show a small read-only source-to-DuckDB sync status text at the top right. Poll the existing frontend interval; show `Syncing` during initial or refresh indexing, `Not synced yet` before the first successful source reconciliation, and the last successful `last_synced_at` in browser local time afterward. This is not query or browser-autosave status. Preserve the existing failure state and do not add a second status service or event stream.

Title the input area Query editor. Put Saved: <ID> at the right of that title on the same header row when a saved resource is available. Provide a CodeMirror SQL editor with a collapsible editor toggle that preserves the query text and cursor when reopened, Run, Check, Run & Save and Save View controls, exact counts, query errors and ordinary result rows with Previous and Next page controls. A View is one query: keep its current query text/draft in the View and do not split it into separate statements. Browser query actions use the existing backend Workspace/View operations (`view_run` and the `save=true` form for Run & Save), not an unbound `query_run` routing path. Run and Check operate on the current View query, while Run & Save runs it and saves only after success; Save View persists the whole current query/draft text. Use shared components from a small component palette. Bind Cmd+Enter to Run and Shift+Cmd+Enter to Check; these shortcuts invoke different operations on the current View, not on a substatement. There is no save-only query action and no /save endpoint. Keep generic MCP `query_run` available for MCP callers, but do not route browser UI through it. Keep display formatting, page navigation and UI state in the frontend; the database executes SQL filtering, sorting and aggregation. No preview UI control is required.


Use read-only query_schema({}) metadata, returned as {tables: {atoms: [{name, type, values?}], scope_units: [{name, type}], change_log: [{name, type}]}} for autocomplete of actual atoms, scope_units, declared content.* columns and the technical read-only `change_log` table. `change_log` exposes exactly `observed_at`, `operation`, `old_path` and `new_path`; preserve the existing atoms, scope_units and content.* metadata, including quoted names. Do not query saved SQL files to build completion suggestions. A URL ?query=<saved_query_id> loads either a saved query or View without executing it and preserves the project_root parameter. Open Saved accepts an ID or URL and opens it in the current Workbench browser context. Show a recent combined query/View list from query_saved_list in the single Saved Queries and Views tab.

Offer Open Saved only in the command palette, without a separate toolbar button or dedicated shortcut. The command opens a modal with an autofocus ID/URL input; native Cmd+V paste is allowed, Enter opens the saved item without executing it, and Escape or Cancel closes the modal. The schema metadata may include optional distinct non-null values for the actual Header Status column returned by query_schema. Complete a single-quoted condition prefix such as header_status = 'Act or header_state_status = 'Act with a properly escaped value such as 'Active'; do not execute SQL or create a saved record for completion.

Run and Check execute or inspect the current View query without saving it. Run & Save executes that View query first and saves only after the Run succeeds, using the Workspace/View `save=true` operation. Page and query errors also create no saved entry. Return the current View SQL with Run and Check results; pagination query_id is separate from a saved ID. Successful Run & Save answers include saved_query_id, saved_query_url, kind and optional name. If saving fails after the result is complete, keep the visible rows and query ID, show outcome partial and save_error, preserve the previous saved identity and dirty state, and do not retry or roll back. Save View persists the whole current query/draft text and returns its saved identity only when that save succeeds. Save, View save, load and list use the same shared contracts as MCP. Keep five-second browser draft autosave. Keep generic MCP query_run available, but do not route browser UI through an unbound query_run operation. Do not add sharing, authentication, saved-Journal deduplication, retry, repair, rollback or deletion workflows in this frontend lane; result-cache retention follows the backend Workbench contract rather than a frontend expiry rule.

The frontend receives columns[].has_values computed over the complete materialized result. For this metadata only, NULL, empty strings, empty arrays and empty objects are empty; false and zero are values, and a nested object with keys is non-empty even when a nested value is null. For a non-empty result, hide only fully empty columns (has_values: false) while preserving row and column counts and all SQL values. For a zero-row result, the connector sets has_values: true for every returned column so all headers remain visible. The same column metadata and visibility decision applies to every page. Content column names use dots between path levels and snake_case within each segment, such as content.claim.prose_claim; spaces are replaced with underscores.

Use the existing Workbench Workspace/View routes at /caprmedio/workbench/<project_name> for run, page, check, view-save, load, saved-list and schema. Browser calls carry the active View context; do not route them through a standalone or unbound query_run endpoint. Do not add a /save endpoint or a legacy Worksheet-save endpoint. POST /view-save, /load and /saved-list use the same MCP contracts; POST /schema accepts {} and returns the same table/column metadata. Fetch only the requested display page while backend grid operations address the full materialized View result. Preserve positional values and duplicate column names. Show loading and error states and accessible labels for controls. Do not add custom DOC or TREE result modes, a second query evaluator or a separate web service.

When the frontend build is missing, keep the query API and MCP available. The Workbench page returns HTTP 503 with an explicit build-required error; do not build assets or start a frontend server automatically.

For the current Project, the page is /caprmedio/workbench/caprmedio. Keep shared static assets under /caprmedio/workbench/assets. The frontend sends Run, Page and Check requests under its current Project page path. The URL's Project name must match the existing selected Project; a mismatched name returns HTTP 404. The plugin opener alone appends `embedded=1` when it opens a Workbench URL; ordinary browser URLs do not receive the marker. Preserve existing Project parameters and explicit chat-bound or foreign Workspace parameters. A default standalone URL must not gain a workspace parameter. Keep its generated Workspace ID in browser local storage; the same browser resumes that Workspace after reload. Remove a legacy workspace parameter only when it equals this browser's persisted standalone ID, preserving query, project_root, other parameters and the fragment. Explicit foreign or chat-bound Workspace links retain their target. Keep all ID formats unchanged.

Keep the read-only result grid in a bounded scrolling region, with visible column headers and separately scrollable long cell values. Preserve every row and value; scrolling changes presentation, not the query result.

Provide a native searchable command-palette dialog, opened by Cmd+P from anywhere in the page. Focus its search field on opening. Offer every current Workbench user action, including Settings, saved library, editor/results focus, View switching/create/rename/close, query actions, Open Saved, Hide/Show editor, page navigation, result-grid filtering, sorting, grouping and context-menu actions, Theme, Interface text zoom, Content text zoom, Interface zoom and Density choices. Show shortcut hints where available. Reuse the existing control handlers and availability conditions. Arrow Up and Ctrl+P move to the previous item; Arrow Down and Ctrl+N move to the next item; Enter invokes the selected available action; Escape closes. Current Theme, Interface text zoom, Content text zoom, Interface zoom, Density and workspace preferences persist in local storage and restore on load. The palette adds no backend capability of its own or command execution engine; View actions use the declared shared backend operations, including view_duplicate.

Double-clicking the current View name opens the existing shared rename modal with the displayed name prefilled. Confirm uses the existing Workspace rename and persistence path; Cancel and Escape leave the name unchanged. The command-palette Rename View action opens the same modal; no click-only rename button is added.

Render each result column name on its own line, with its SQL type below in smaller muted text. Do not concatenate the name and type. Keep the SQL column names and types unchanged.

Render the result grid with Tabulator 6.7.1 integrated directly into the Svelte frontend; do not add a wrapper framework. Keep the grid read-only with no cell or row editors. Use the existing backend Workbench View/grid/page contract against the full materialized cached result: filtering, multisort, one-column grouping and exact global row/group counts must not operate only on the currently loaded page, and no display action reruns the View query. Use the same backend View context in standalone and embedded Workbench modes; one View remains one query. Provide only these context-menu actions: Cell Copy value, Cell Show full value, Row Copy row, Column Sort ascending, Column Sort descending, Group by, Filter and Clear filter. Group by is limited to one column in this MVP. Do not add nested grouping, pivoting, exports, collaboration, editors or persisted grid state. The Full/Limited content preference remains presentation-only and keeps the complete cached values intact. In Dark theme, Tabulator headers, cells, borders and hover/focus/selected states remain readable; use the existing theme styling without adding grid features.

Deliver the result-display preferences as presentation-only UI. Settings presents Adaptive or Fixed row/page sizing, with Adaptive as the default. Retain a Fixed value of 100 rows, but show its numeric field only when Fixed is selected; constrain that positive integer to 1..1000 and store the selected mode and value in browser local storage. Adaptive sizing fits visible Results and recalculates when viewport size, Interface text zoom, Content text zoom, Interface zoom or Density changes. Use the smallest native ResizeObserver integration at the existing ResultsTable/Preferences boundary; do not add a scheduler or service. Page navigation reuses the existing query_id and page and does not rerun SQL.

Put the `Full`/`Limited` cell-content control inline in the ResultsTable header, persist it with the same global result-display preference, and expose the same current actions in the command palette without duplicate divergent controls. Limited is the default and shows up to N Unicode characters, with N=150 retained as the default positive integer; N is configurable as any positive integer without an arbitrary maximum, and its field is hidden when Full is selected. Preserve the complete underlying result rows and values; the full returned value remains available to the frontend and through the MCP/query capability. Use one canonical handler for Settings, ResultsTable and palette actions. No backend or MCP schema or endpoint is added for these choices.


Keep result column names prominent. Display SQL types/formats in smaller, pale text in both light and dark themes.

Display every source newline as a new line in Content cells and full-value views using pre-wrap presentation. Do not collapse single newlines into spaces or require a blank line. Preserve source text and existing escaping; Limited content still uses its configured character limit.

Deliver a Format button beside the existing Query editor actions and expose the same action in the command palette. Use `@dlh.io/dlh-sql-formatter` version 1.3.0 with the DuckDB dialect and the existing CodeMirror parser, in both standalone and native Workbench. Apply the result through the normal editor-change path so existing unsaved-state and local autosave behavior applies. Formatting does not execute SQL, create a saved item or replace existing query results. A formatter error is visible and leaves the query unchanged.

Handle an ordinary Saved-link activation inside Workbench by focusing the View that owns the link and preventing the default navigation. Keep ordinary modified-link browser actions available. Route Open Saved references through the existing loader; after resolving the saved ID, focus an already-open matching View before considering creation. Persist and restore its saved identity with the existing standalone browser draft.

Add Rename and Duplicate to a View-tab context menu and the command palette. Context-menu actions target the tab that was opened; palette actions target the current View. Reuse the current rename dialog, prefilled with the current name. Support dismissal and keyboard use of the menu. Duplicate calls `view_duplicate` after current edits are synchronized, inserts the new View after its source, focuses it, and preserves its copied query and cursor. The new unsaved View has its own ID and no result or saved-item identity. Names use the exact no-space form `<current name>(1)`, then the first unused positive suffix. Use the existing `View N` display name when the source has no explicit name.
