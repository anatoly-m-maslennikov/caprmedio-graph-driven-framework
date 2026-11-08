---
atom_id: CA-D-681
ref_id: CA-D-681@10
container:
  scope_unit: CA-SU-48
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workspace
tier: 4
relations:
  delivery_for:
  - CA-R-2902
  - CA-R-2903
  - CA-M-476
  - CA-E-684
status: Archived
version: 10
updated_at: 2026-11-07 01:21:17 +0400
carrier_destination:
  file:
    name: CA-D-681@10-CODEX_EXTENSION-ENG_DECISION--deliver-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/07_delivery/archived
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Deliver Workbench Workspace Views

## Claim

Deliver Workbench Workspace and View effects through the existing MCP connection and one shared Svelte Workbench UI. The standalone browser and native Codex UI expose the same existing list, open, create, update, run, fetch, focus, rename, duplicate, remove, save, and query-log effects. Reuse the existing query executor, pagination, successful-run saving, saved Journal, browser autosave, query-log retention, and backend handlers. Do not add a second MCP service, standalone chat, chat controls, code runner, scheduler, magic Workflow, retry system, browser iframe, or host-specific panel API.

Workspace and View tools use explicit IDs. The HTTP interface invokes the same handlers under the selected Project's Workbench URL. A Workspace URL uses `?workspace=<workspace_id>` and preserves `project_root` when required. Unknown IDs and malformed inputs fail without selecting another Workspace.

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
| `view_fetch` | `workspace_id`, `view_id`, `offset` (default 0), `page_size` (default 100, 1..1000), optional `preview` | Fetch a page of the View's current result; preview caps the page without rerunning the SQL. |
| `view_focus` | `workspace_id`, `view_id` | Set the Workspace's active View. |
| `view_rename` | `workspace_id`, `view_id`, `name` | Update the current View name. |
| `view_remove` | `workspace_id`, `view_id` | Remove the View; reject the last View. |
| `view_save` | either `workspace_id` + `view_id`, or existing `sql` + optional `name` | Reuse whole-script saving and its saved ID/URL. The two input modes are exclusive. Saved View names/SQL are snapshots, not renamed in place. |
| `query_log_list` | optional `limit` (default 20, 1..1000) | Recent retained log records. |
| `query_log_get` | `log_id` | One retained log record. |

Use existing UUID generation for View IDs. Store Workspace documents under `.caprmedio_runtime/workbench/workspaces`, with no duplicate chat history or result rows. Browser draft storage keys include explicit Project and Workspace ID; the frontend synchronizes actual bound state, including externally requested focus, while preserving unsynced edits on conflicts. Do not import another Workspace's browser drafts.

Each actual Run appends SQL, success/fail, error, row count, column count, technical ID and timestamp to the runtime query log. Counts are null when unavailable after failure. The parent backend retains entries for two days in hourly batches; no duplicate expiry or cleanup path is added. Automatic query-log writes use the backend background writer; failures are reported to stderr only without changing a completed result; Check is not logged. A result ID is process-local; reread or restart invalidates it. View removal or replacement releases the existing cache table. Saved Views and their Journal records have no query-log retention TTL.

`workspace_open` is the sole UI-bearing MCP tool. Its descriptor links `ui://caprmedio/workbench.html`, served as `text/html;profile=mcp-app`. The native host passes `session_id` and explicit trusted `project_root` as its tool input; the `workspace_open` structured result supplies the initial Workspace. The UI waits for both input and result, uses their exact values, and does not invoke another open. Missing either context displays a binding error and performs no backend call.

Build `workbench_app.html` as one self-contained MCP App resource with the existing Vite/Svelte toolchain. Its JavaScript and CSS are inline; it opens no browser, makes no Workbench HTTP request, and needs no second server. The frontend owns the one shared `App.svelte` and transport selection: standalone retains the existing HTTP bootstrap; native initializes the MCP Apps bridge and calls the existing tools through `tools/call`. The native transport injects `project_root` for every call and preserves existing structured results and errors. It does not create an API adapter or business logic.

`FEATURE_MCP` adds the Workbench resource URI only to the existing `workspace_open` descriptor and exposes the built resource from its existing registry/read handler. Existing dispatch, Project validation, and structured results remain the backend path. `FEATURE_CODEX_EXTENSION` skill instructions direct the caller to invoke `workspace_open` with the host-supplied session ID and trusted Project root; its existing hook supplies context only, starts nothing, and registers no panel. `plugin.json` adds no panel or connection declaration.

Register the existing `caprmedio-workbench` package in `.agents/plugins/marketplace.json` under `caprmedio-local`, with local source `./LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_CODEX_EXTENSION/plugin`. The desktop app discovers it after restart; the Operator installs it and explicitly trusts the bundled hook through `/hooks`. Activation requires a new or resumed native chat; building or releasing the backend does not install the plugin or retroactively run a hook. Native UI delivery completes only when the host renders the Workbench and it exercises the same MCP Workspace/View effects.

The standalone browser uses the same selected-Project handlers and backend, but no chat. Its unique localStorage Session ID opens its own Workspace without inventing a native `session_id`. Explicit `?workspace` selects a Workspace; `embedded=1` is density only; assigning a Workspace preserves `query` and all parameters. First binding copies an unbound draft once without SQL execution and retains its local copy until confirmation. Result-cache TTL is separate from query-log retention and defaults to 3600 seconds unless already configured.

The existing `workbench_ui_probe` and `workbench_ui_ping` remain separate read-only compatibility evidence: the probe resource is not the Workbench resource and does not activate Workbench. It may establish MCP Apps protocol compatibility but cannot establish actual Workbench delivery. Fullscreen or move-to-panel is exercised only if offered by the host; neither implies a persistent right panel.

The probe and ping use the existing MCP connection, take no native arguments, return fixed messages, do not read Project data or start Workbench, and reject unexpected arguments or unknown resource URIs. The probe alone links `ui://caprmedio/workbench-compatibility-v2.html` with `text/html;profile=mcp-app`. It declares inline and fullscreen capability, shows the current and offered modes, enables Expand only when fullscreen is offered, requests it through `ui/request-display-mode`, displays the returned mode, and merges `ui/notifications/host-context-changed`. Acceptance, retained-inline, rejection and unsupported-fullscreen cases are checked. In the real host, right-panel support remains unproven unless an offered move-to-panel action preserves the same resource, initial result and bridge.

Expose `view_duplicate` through the same Workbench backend, HTTP interface and MCP registry. It accepts exactly `workspace_id` and `view_id`. Return the existing create-shaped Workspace state plus the new `view_id`. In the existing serialized Workspace action boundary, copy source SQL and cursor into a new UUID View at revision zero, insert it immediately after the source and make it active. Do not copy results or saved identity, and do not execute SQL. Generate a name by taking the source's explicit name, or its current `View N` display name, and appending the smallest unused positive `(n)` suffix among current Workspace display names.

Public workspace_open and workspace_get responses include project_name alongside the existing Workspace state and request-derived workspace_url. Obtain project_name from the selected Project's validated settings through the existing public Workspace adapter, for both HTTP and MCP. The native UI requires this name in its initial Workspace result and uses it for the Project header; a missing name is a binding error, not permission to derive a directory label. Other tool inputs and Workspace persistence remain unchanged.
