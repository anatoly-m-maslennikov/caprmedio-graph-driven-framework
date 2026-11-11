---
identity:
  atom_id: CA-R-2727
  ref_id: CA-R-2727@21-draft
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Draft
  version: 21
  updated_at: 2026-11-11 01:59:26 +0400
destination:
  file:
    name: CA-R-2727@21-draft-WORKBENCH-SOLUTION--provide-a-simple-web-query-interface-over-the-shared-query-capability.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/draft
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Provide a simple web query interface over the shared query capability

## Claim scope

The UX of the local web interface for queries over the query Projection.

## Claim

### Prose Claim

Compact density uses smaller buttons, padding and gaps. Settings text may be larger for readability; text zoom remains independent.

The web interface **must**:

- provide a Tab editor with synchronous Run, Check, Run & Save and Save actions. Run & Save uses the shared Tab Run operation with save true; there is no save-only query action.
- keep one SQL script in each Tab, with multiple semicolon-separated statements. Run the whole script or explicitly selected statements in order; Check validates without applying changes. Follow CA-R-2728@9-draft for execution, source updates and change preview. Preserve quoted strings, comments and CTEs; Save saves the whole script without execution.
- use a compact, modern, minimal technical interface with light, dark and remembered System themes. Adapt its width to the available window. Reduce the vertical space from the Workbench title through the result statistics and Cell content controls; at 100% scale, target half the height of the previous layout shown at 80%, while preserving readable controls.
- show Workbench and the selected Project name in the top header. Put Settings and Bookmarks and Saved Tabs at the top of the window, on the right at the same level as Workbench. Keep current Tab tabs in the workspace below.
- offer Compact and Comfortable density settings. Compact is the default only when the URL carries the explicit `embedded=1` marker; an ordinary standalone URL defaults to Comfortable. Saved explicit browser preferences win. The Operator selects the setting; do not detect physical screen size or infer embedding from Workspace presence. Persist the setting with existing browser settings.
- keep the Settings panel hidden initially and lay its controls out vertically as Theme, Interface text zoom, Content text zoom, Interface zoom and Density; apply preferences on page load even while it is hidden.
- provide independent Interface text zoom and Content text zoom, each with presets 80, 90, 100, 110, 125, 150 and 200 percent. Interface text zoom scales titles, buttons, tabs, labels, Settings and table headers; Content text zoom scales query and result text. Remember both values. Both are text-only and remain independent from density and whole-Interface zoom.
- provide Interface zoom using the same fixed presets for whole-interface scaling, remember it in browser local storage, and keep it independent from text-only zoom and density. Do not auto-detect screen size or add a separate setting registry.
- use the Query editor header panel as the single collapse control for the active Tab. Put pale `Hide editor` text at the right when expanded and `Show editor` when collapsed; do not add a separate Hide editor toolbar button. Keep keyboard activation available. Keep the query text for every open Tab in browser local storage every 5 seconds and restore it on the next page load.
- title the input area Query editor. Show Saved: <ID> at the right of that title, on the same header row, when a saved resource is available.
- offer Open Saved only in the command palette, without a separate toolbar button or dedicated shortcut. The command opens a modal with an autofocus ID/URL input; native paste with Cmd+V is allowed, Enter opens the saved item without executing its SQL, and Escape or Cancel closes the modal.
- ask before closing an unsaved tab or window. The standard browser beforeunload warning is allowed; flush the latest local draft on pagehide and beforeunload when possible.
- show each available hotkey inside its action button or immediately beside it.
- bind Cmd+Enter to Run and Shift+Cmd+Enter to Check. These shortcuts invoke different operations on the whole script or explicit selection; Save saves the full script without execution.
- show ordinary result rows in navigable pages, exact row and column counts and query errors. Show column names separately from their SQL types, with types in smaller, pale text.
- use a small reusable component palette for consistent controls and result presentation.
- open a searchable command palette with Cmd+P from anywhere in Workbench. Expose every current user action, including Settings, moving focus, switching/creating/renaming/closing Tabs, Run, Check, Run & Save, Save Tab, Open Saved, Hide/Show editor, result paging, Theme, Interface text zoom, Content text zoom, Interface zoom and Density. Show available shortcuts. Use Arrow Up or Ctrl+P for the previous item, Arrow Down or Ctrl+N for the next item, Enter to choose and Escape to close. Invoke the same handlers and availability rules as the visible controls, without requiring a mouse or memorized action shortcuts.
- persist current Theme, Interface text zoom, Content text zoom, Interface zoom, Density and workspace preferences in browser local storage and restore them on load.
- provide SQL autocomplete from actual read-only query_schema metadata for all exposed tables and columns, including issue tables and declared content.* columns, with quoted column names where needed. Schema completion must not query saved SQL files.
- include optional non-null distinct values for the actual Header Status column returned by query_schema in schema metadata for completion. When a qualified or unqualified condition has a single-quoted prefix such as `"header.state.status" = 'Act`, completion may insert the matching escaped value such as 'Active'; completion never executes SQL or creates a saved record.
- load a Bookmark or Tab from ?query=<saved_query_id> without executing it, while preserving the existing project_root URL parameter. Open Saved accepts an ID or URL and opens it in the current Workbench browser context. Show a recent combined query/Tab list from query_saved_list in one Bookmarks and Saved Tabs tab.
- keep presentation, formatting, page navigation and UI state in the frontend; SQL filtering, sorting and aggregation remain in the database.
- use the same query capability as MCP.
- save a query only through a successful Run & Save. Run, Check, Page and their errors do not create permanent saved entries or return a new saved identity. Query runs have a separate two-day log; saved Tabs have no TTL. A save failure keeps the completed rows and error state, preserves the previous saved identity and dirty state, and shows the save error. Save Tab saves the whole Tab query text. Successful save answers include the saved ID, kind and full URL.
- allow the Operator to rename a current Tab and keep its optional name in browser autosave. Save Tab may persist an optional name; Run & Save may take an optional query name. Do not rename Bookmarks or saved Tabs after creation; their IDs and URLs do not change.
- identify the selected Project by its declared name in the Workbench URL and reject a Project name that does not match the selected Project.
- remain within the existing local application boundary and avoid custom TABLE, DOC or TREE result modes. Do not auto-execute a query from a URL, add sharing or authentication, or add a queue, retry, repair or rollback mechanism. Bookmarks and Tabs do not expire. Query logs and transient result tables follow their separate retention rules.

- provide a Result display preference with `Adaptive` or `Fixed` row/page sizing. Adaptive is the default. Retain a Fixed value of 100 rows in the preference, but show that numeric value only when Fixed is selected; persist explicit choices in browser storage.
- in Fixed mode, accept and persist a positive integer page size from 1 through 1000, matching the existing backend `page_size` limit. In Adaptive mode, fit the visible Results to the available space and update the display when viewport size, Interface text zoom, Content text zoom, Interface zoom or Density changes.
- keep row sizing, pagination and content presentation display-only: reuse the existing `query_id` and `page` for page requests and never rerun SQL. A `Full`/`Limited` cell-content choice shows either the complete returned value or the first N Unicode characters. Limited is the default with N=150; N is configurable as any positive integer without an arbitrary maximum, and the N field is hidden when Full is selected. The underlying values remain unchanged. Request inline result pages explicitly for the grid; MCP result files preserve those same values.
- expose these current result-display actions through the existing Settings and command-palette policy, without adding a backend or MCP capability.

Display every source newline as a new line in Content cells and full-value views. Do not collapse single newlines into spaces or require a blank line. Preserve source text and existing escaping; Limited content still uses its configured character limit.

The Query editor must provide Format for the current Tab. Formatting applies the query-writing Method to the existing SQL as an ordinary unsaved edit. It preserves query expressions, identifiers, literal values and comments, and neither runs nor saves the query. If formatting fails, retain the original input and show the error.

Opening a saved item that already has an open Tab focuses that Tab without creating a copy or replacing its current edits. Clicking a Tab's Saved link keeps that Tab open in the current Workbench. Match saved items by their saved-entry identity, not by SQL text.

Provide Rename and Duplicate in each Tab tab's context menu and in the command palette. Rename uses the existing current-Tab name dialog. Duplicate creates and focuses a new Tab with a new ID, copying only the current query and cursor position. It does not copy or execute results, create a saved Journal entry, or change the original Tab. Its name is the current display name followed immediately by the first unused positive suffix `(1)`, `(2)` and so on within the Workspace.

Every primary Workbench workflow is keyboard-operable, with visible focus, meaningful control names and roles, predictable traversal, perceivable status changes and reachable error recovery.

The frontend renders untrusted Project content as inspectable data. Text, markup, links, styles and control characters cannot escape their output context, execute or grant capabilities.
