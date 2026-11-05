---
atom_id: CA-D-681
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
status: Active
version: 2
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Workspace
relations:
  delivery_for:
  - CA-R-2902
  - CA-R-2903
  - CA-M-476
  - CA-E-684
carrier_destination:
  file:
    name: CA-D-681-CODEX_EXTENSION-ENG_DECISION--deliver-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/07_delivery
updated_at: 2026-11-05 18:01:09 +0400
---

## Summary

Deliver Workbench Workspace Views

## Claim

Deliver the embedded Workbench Workspace and View operations through the supported native browser embedding and MCP surfaces. The browser and MCP **must** expose the same list, open, create, update, run, fetch, focus, rename, remove and save effects.

Reuse the existing Workbench query executor, pagination, successful-run saving, saved Journal and browser autosave. Return Run metadata without rows by default and fetch rows through the existing paged capability. Deliver the temporary seven-day query log with the same backend and MCP list/fetch behavior, without result rows or extra schema data.

Do not add an iframe SDK, standalone chat, separate chat controls, code runner, scheduler, magic Workflow or retry system.


## Interface

The extension is a local Codex plugin with `plugin.json`, `skills/workbench/SKILL.md` and a command `SessionStart` hook. The hook supplies only the native `session_id` as model context; it starts no service and makes no network request. The Skill uses the existing host-configured CAPRMEDIO MCP, carries the trusted Project root, opens its returned `workspace_url` in the native browser beside the current chat and does not bundle a second MCP connection. The Workspace ID is the supplied native session ID. The plugin does not prove or invent a native chat identity.

Workspace and View tools use explicit IDs. The HTTP interface invokes the same handlers under the selected Project's Workbench URL. A Workspace URL uses `?workspace=<workspace_id>` and preserves `project_root` when required. Unknown IDs and malformed inputs fail without selecting another Workspace.

| Operation | Inputs | Result |
|---|---|---|
| `workspace_open` | `session_id` | Initialize or resume this Workspace with one initial View; return its state and request-derived URL. |
| `workspace_list` | none | Known Workspace IDs for the explicit Project; no result rows. |
| `workspace_get` | `workspace_id` | Current Views, SQL, names, revisions, active View ID and result metadata; no rows. |
| `view_create` | `workspace_id`, `position` (`first` or `last`, default `last`), optional `name` | New stable View ID and state. |
| `view_list` | `workspace_id` | Ordered View IDs, names and result metadata; no SQL or rows. |
| `view_get` | `workspace_id`, `view_id` | One View's SQL, revision and result metadata; no rows. |
| `view_update` | `workspace_id`, `view_id`, `sql`, optional `cursor_position`, required `expected_revision` | Updated View. A revision mismatch fails and leaves both the server SQL and the browser's unsynced draft intact. |
| `view_run` | `workspace_id`, `view_id`, optional `cursor_position`, `preview`, `save`, `name` | Run the selected statement; return success/fail, error, counts and query ID, with no rows. Existing successful Run-and-save behavior is available through `save=true`. |
| `view_check` | `workspace_id`, `view_id`, optional `cursor_position` | Existing Check result; no query-log entry. |
| `view_fetch` | `workspace_id`, `view_id`, `offset` (default 0), `page_size` (default 100, 1..1000), optional `preview` | Fetch a page of the View's current result; preview caps the page without rerunning the SQL. |
| `view_focus` | `workspace_id`, `view_id` | Set the Workspace's active View. |
| `view_rename` | `workspace_id`, `view_id`, `name` | Update the current View name. |
| `view_remove` | `workspace_id`, `view_id` | Remove the View; reject the last View. |
| `view_save` | either `workspace_id` + `view_id`, or existing `sql` + optional `name` | Reuse whole-script saving and its saved ID/URL. The two input modes are exclusive. Saved View names/SQL are snapshots, not renamed in place. |
| `query_log_list` | optional `limit` (default 20, 1..1000) | Recent retained log records. |
| `query_log_get` | `log_id` | One retained log record. |

Use existing UUID generation for View IDs. Store Workspace documents under `.caprmedio_runtime/workbench/workspaces`, with no duplicate chat history or result rows. Browser draft storage keys include the explicit Project and Workspace ID; the unbound browser mode preserves its existing separate drafts. The frontend synchronizes the bound Workspace's actual state with the backend, including externally requested focus, while preserving unsynced edits on conflicts. Do not import another Workspace's browser drafts.

Each actual Run appends SQL, success/fail, error, row count and column count to the runtime query log, plus its technical ID and timestamp. Counts are null when unavailable after failure. Expire entries older than seven days on append, list or fetch; no background cleanup job. A log-write failure is reported to stderr and in the response without discarding a completed query result. Query Check is not logged. A result ID is process-local; reread or restart invalidates it. View removal or replacement of a displayed result releases that result's existing cache table. Saved Views and their Journal records have no TTL.


## Local plugin activation

Register the existing `caprmedio-workbench` package in the repository's `.agents/plugins/marketplace.json`, under marketplace `caprmedio-local` with display name CAPRMEDIO. Its local source is `./LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_CODEX_EXTENSION/plugin`, within this repository. Keep the existing MCP connection; do not bundle a second connection.

The desktop app discovers the repository entry after an app restart. The Operator installs the local plugin and explicitly trusts its bundled hook through `/hooks`. Skill and SessionStart activation require a new or resumed native chat; building or releasing the backend does not install the plugin or retroactively run a hook in an already active chat. Preserve the current chat and do not restart the desktop app as part of backend release.
