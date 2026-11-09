---
identity:
  atom_id: CA-M-476@6
  ref_id: CA-M-476@6
context:
  container:
    scope_unit: CA-SU-48
  role: Method
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Workspace
  tier: 4
relations:
  method_for:
  - CA-R-2902
  - CA-R-2903
state:
  status: Archived
  version: 6
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-M-476@6-CODEX_EXTENSION-SOLUTION--coordinate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/05_method/archive
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Coordinate Workbench Workspace Views

## Claim

Use the existing Codex chat as the native Workspace boundary and the existing `workspace_open` MCP operation as the native UI activation. Its host tool input is the sole native identity source: accept only non-empty `session_id` and explicit trusted `project_root`, and accept its initial structured result as the opened Workspace. Do not read URL parameters or localStorage in native mode, manufacture a native session, bind another Workspace, or call `workspace_open` a second time. Missing input or result is a visible binding error and makes no backend call.

Use one shared Svelte Workbench UI for standalone and native mode. Keep the existing typed Workspace/View facade, but substitute transport only: the standalone bootstrap keeps its existing HTTP and URL/localStorage rules; native bootstrap uses MCP Apps initialization and the bridge `tools/call`. The native transport injects the same explicit `project_root` into every existing operation call, preserves `structuredContent`, and rejects `isError`. It adds no domain logic, response adapter, MCP service, chat, or UI-specific handler.

For each explicit Project, route both modes to the existing Workspace/View backend. Native mode uses the supplied session ID unchanged. Standalone mode retains its existing browser-owned Session ID, explicit `?workspace` behavior, `embedded=1` density marker, and one-time unbound-draft migration; none applies in native mode. Do not merge Workspaces across chats or Projects and do not import an unbound standalone draft into a native Workspace.

Keep View operations as small adapters over the existing query executor, pagination, successful-run saving, saved Journal, browser autosave, and query log. Keep caller order; return Run metadata first and rows only through fetch. A View is one SQL query: Run and Check validate the whole View and reject multiple statements rather than selecting at the cursor. The parent Workbench backend owns two-day query-log retention and result-cache configuration. Add no scheduler, retry, cleanup lifecycle, lease, heartbeat, new shared service, or Domain entity.

Keep the query log separate from saved Views. Record only the approved SQL, outcome, error and counts; do not store rows or duplicate schema data. The parent Workbench backend retains entries for two days in hourly batches; this Method adds no query-log TTL, expiry, or cleanup path. Both UIs call the same existing create, update, run, fetch, focus, rename, remove and save operations.

In standalone mode, resolve an explicit `?workspace=<workspace_id>` before restoring View state and preserve every existing URL parameter while assigning a Workspace, including the saved-query/open-saved `query`; `embedded=1` remains a density marker only. On first explicit standalone binding, migrate an unbound draft at most once without SQL execution, retain the local copy until backend confirmation, and do not repeat after confirmation. Keep result-cache TTL separate from query-log retention and use the shared Workbench runtime configuration's default of 3600 seconds unless an existing configured value applies.

The initial native Workspace result carries the selected Project's canonical project_name. Reuse the existing ProjectSelection settings/name reader at the public adapter boundary. Keep this derived name out of persisted Workspace documents and do not infer it from a directory basename or add a query, parser, fallback name, or tool. The native frontend uses that supplied name for its Project header.
