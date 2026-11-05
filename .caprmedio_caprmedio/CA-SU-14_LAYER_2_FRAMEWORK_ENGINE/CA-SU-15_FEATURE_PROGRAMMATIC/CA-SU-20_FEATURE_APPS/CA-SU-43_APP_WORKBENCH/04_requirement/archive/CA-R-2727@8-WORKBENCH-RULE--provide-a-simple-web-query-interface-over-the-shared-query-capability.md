---
atom_id: CA-R-2727
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 8
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2727@8-WORKBENCH-RULE--provide-a-simple-web-query-interface-over-the-shared-query-capability.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-05 02:58:37 +0400
---
## Summary

Provide a simple web query interface over the shared query capability

## Claim scope

The UX of the local web interface for queries over the query Projection.

## Claim

### Prose Claim

The web interface **must**:

- provide a Worksheet editor with synchronous Run, Check, Save and Save Worksheet actions.
- allow multiple SQL statements in one Worksheet, using semicolons as delimiters while preserving quoted strings, comments and dollar-quoted strings. Run, Check and Save target the statement at the cursor; a cursor exactly on a semicolon selects the statement to its left; Save Worksheet saves the whole script.
- use a compact, modern, minimal technical interface with light and dark themes, including a remembered System theme choice.
- show Workbench and the selected Project name in the top header. Put `Settings` and `Saved Queries and Worksheets` at the top-right of that header, on the same level as Workbench. Keep current Worksheet tabs in the workspace below. The `Settings` panel is hidden initially; Theme and Zoom preferences apply on page load even while it is hidden.
- provide one `Hide editor` control for the active Worksheet. Keep the whole script for every open Worksheet in browser local storage every 5 seconds and restore it on the next page load.
- title the input area `Query editor`. Show `Saved: <ID>` at the right of that title, on the same header row, when a saved resource is available.
- provide one top-left `Open Saved` button, not an inline open form. `Cmd+Option+O` opens a modal with an autofocus ID/URL input; native paste with `Cmd+V` is allowed, Enter opens the saved item without executing its SQL, and Escape or Cancel closes the modal.
- ask before closing an unsaved tab or window. The standard browser `beforeunload` warning is allowed; flush the latest local draft on `pagehide` and `beforeunload` when possible.
- use text-only zoom presets `80`, `90`, `100`, `110`, `125`, `150` and `200` percent, and remember the selected preset.
- show each available hotkey inside its action button or immediately beside it.
- bind `Cmd+Enter` to Run and `Shift+Cmd+Enter` to Check. These shortcuts must invoke different operations and target the statement at the cursor. Buttons Run, Check and Save target the same active statement; Save Worksheet targets the whole script.
- show ordinary result rows in navigable pages, exact total row and column counts, and query errors.
- use a small reusable component palette for consistent controls and result presentation.
- open a searchable command palette with `Cmd+P` from anywhere in Workbench. Expose every current user action, including Settings, moving focus, switching/creating/renaming/closing Worksheets, Run, Check, Save, Save Worksheet, Open Saved, Hide/Show editor, result paging, Theme and Zoom. Show available shortcuts. Use Arrow Up or `Ctrl+P` for the previous item, Arrow Down or `Ctrl+N` for the next item, Enter to choose and Escape to close. Invoke the same handlers and availability rules as the visible controls, without requiring a mouse or memorized action shortcuts.
- persist current Theme, Zoom and workspace preferences in browser local storage and restore them on load.
- provide SQL autocomplete from read-only `query_schema` metadata for `atoms`, `scope_units` and declared `content.*` columns, including quoted column names. Schema completion must not query saved SQL files.
- include optional non-null distinct `atoms.status` values in schema metadata for completion. When a qualified or unqualified condition has a single-quoted prefix such as `status = 'Act`, completion may insert the matching escaped value such as `'Active'`; completion never executes SQL or creates a saved record.
- load a saved query or Worksheet from `?query=<saved_query_id>` without executing it, while preserving the existing `project_root` URL parameter. Open Saved accepts an ID or URL and opens it in the current Workbench browser context. Show a recent combined query/Worksheet list from `query_saved_list` in one `Saved Queries and Worksheets` tab.
- keep presentation, formatting, page navigation and UI state in the frontend; SQL filtering, sorting and aggregation remain in the database.
- use the same query capability as MCP.
- save queries only through explicit Save and Save Worksheet actions. Run, Check, Page and their errors do not create saved entries or return a new saved identity. Run and Check still return the selected SQL and their results or errors. Explicit save answers include the saved ID, kind and full URL, constructed from the actual request context.
- allow the Operator to rename a current Worksheet and keep its optional name in browser autosave. `Save Worksheet` may persist an optional name; explicit Save may take an optional query name. Run and Check do not save queries. Do not rename saved Queries or saved Worksheets after creation; their IDs and URLs do not change.
- identify the selected Project by its declared name in the Workbench URL.
- reject a Project name that does not match the selected Project.
- remain within the existing local application boundary.
- avoid custom TABLE, DOC, or TREE result modes.
- do not auto-execute a query from a URL, add sharing or authentication, or add a queue, retry, repair, rollback or expiry mechanism.

Light (Day), Dark (Night) and System are selectable theme modes; remember the selected mode.
