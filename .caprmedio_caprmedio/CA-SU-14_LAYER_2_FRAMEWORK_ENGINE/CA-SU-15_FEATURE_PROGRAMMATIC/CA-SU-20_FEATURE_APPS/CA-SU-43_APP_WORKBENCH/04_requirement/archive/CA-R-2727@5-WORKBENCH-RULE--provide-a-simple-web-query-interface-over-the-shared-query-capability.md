---
atom_id: CA-R-2727
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 5
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2727@5-WORKBENCH-RULE--provide-a-simple-web-query-interface-over-the-shared-query-capability.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-04 23:19:17 +0400
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
- use a modern, minimal technical interface with light and dark themes, including a remembered System theme choice.
- provide tabs for multiple open SQL inputs. Keep the whole script for every open Worksheet in browser local storage every 5 seconds and restore it on the next page load, including the collapsed-editor state.
- ask before closing an unsaved tab or window. The standard browser `beforeunload` warning is allowed; flush the latest local draft on `pagehide` and `beforeunload` when possible.
- use text-only zoom presets `80`, `90`, `100`, `110`, `125`, `150` and `200` percent, and remember the selected preset.
- bind `Cmd+Enter` to Run and `Shift+Cmd+Enter` to Check. These shortcuts must invoke different operations and target the statement at the cursor. Buttons Run, Check and Save target the same active statement; Save Worksheet targets the whole script.
- show ordinary result rows in navigable pages, exact total row and column counts, and query errors.
- use a small reusable component palette for consistent controls and result presentation.
- provide SQL autocomplete from read-only `query_schema` metadata for `atoms`, `scope_units` and declared `content.*` columns, including quoted column names. Schema completion must not query saved SQL files.
- load a saved query or Worksheet from `?query=<saved_query_id>` without executing it, while preserving the existing `project_root` URL parameter. Open Saved accepts an ID or URL and opens it in the current Workbench browser context. Show a recent combined query/Worksheet list from `query_saved_list`.
- keep presentation, formatting, page navigation and UI state in the frontend; SQL filtering, sorting and aggregation remain in the database.
- use the same query capability as MCP.
- include `saved_query_id`, `saved_query_url`, `kind` and the actual selected SQL in Run, Check and Save answers, including query errors. Page returns the original saved identity and URL. Construct the saved URL from the actual request context; do not invent a port.
- identify the selected Project by its declared name in the Workbench URL.
- reject a Project name that does not match the selected Project.
- remain within the existing local application boundary.
- avoid custom TABLE, DOC, or TREE result modes.
- do not auto-execute a query from a URL, add sharing or authentication, or add a queue, retry, repair, rollback or expiry mechanism.

Light (Day), Dark (Night) and System are selectable theme modes; remember the selected mode.
