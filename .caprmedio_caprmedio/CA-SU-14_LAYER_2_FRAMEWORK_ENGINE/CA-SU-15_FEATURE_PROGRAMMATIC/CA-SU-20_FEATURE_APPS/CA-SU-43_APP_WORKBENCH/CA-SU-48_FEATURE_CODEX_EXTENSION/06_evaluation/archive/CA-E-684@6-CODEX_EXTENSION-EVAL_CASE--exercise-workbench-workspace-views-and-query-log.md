---
atom_id: CA-E-684
ref_id: CA-E-684@6
container:
  scope_unit: CA-SU-48
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workspace
tier: 5
relations:
  evaluation_for:
  - CA-R-2902
  - CA-R-2903
  - CA-M-476
  - CA-D-681
status: Archived
version: 6
updated_at: 2026-11-06 21:54:04 +0400
carrier_destination:
  file:
    name: CA-E-684@6-CODEX_EXTENSION-EVAL_CASE--exercise-workbench-workspace-views-and-query-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/06_evaluation/archive
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Exercise Workbench Workspace Views and Query Log

## Claim

Use the real native Codex plugin UI and MCP surfaces. Do not count a page opened by `open_in_codex(type=browser)` as the plugin UI. Verify that one current Codex chat opens one isolated Workspace with at least one View using the host-provided native session identity and explicit Project. Verify Workspace list/open, unknown-ID errors, first/last View creation, stable View IDs returned by create/list and accepted by every single-View operation, View listing, SQL update, focus, rename, save, paginated fetch with optional preview, and rejection of removing the last View. Verify Run returns status, counts, result ID and errors without rows by default, and fetch is optional.

Verify the native UI, standalone browser and MCP use the same Workspace/View effects. Two Codex chats must keep separate Workspaces and unsaved SQL. Verify no standalone chat, synthetic native session, magic Workflow, code runner, scheduler, or retry behavior is required.

Verify a successful Run and a failed Run each add the exact query-log fields while Check adds none. Verify original whole-View SQL is preserved, preview does not rewrite it, row and column counts are reported, query-log list/fetch works through MCP and the UI, and the parent backend retains entries for two days in hourly batches without a duplicate extension expiry path. Verify no result rows or extra schema data are stored, saved Views remain available without query-log retention, existing saved IDs and Journal records remain usable, and result-cache TTL remains separate with the shared default of 3600 seconds unless configured otherwise.

Use one real standalone browser context with no chat and one real native Codex UI context against the same explicit Project. Verify the persisted standalone localStorage Session ID survives reload and opens its own Workspace without creating or claiming a native `session_id`; in the plugin context, verify supplied native identity is unchanged. Verify explicit `?workspace` selection, density-only `embedded=1`, and preservation of `query`, all URL parameters, and fragment while assigning a Workspace. Seed an unbound browser draft and verify one copy into its own Workspace without SQL execution, retained local copy until confirmation, no repeated copy after confirmed retry, exact content preservation, and no shared-Project merge or import into plugin context.

Edit a View to a temporarily invalid state and verify Run and Check reject multiple statements without selecting at the cursor. Verify an existing saved multi-script query remains unchanged and is never partially executed through a View. Verify these results in standalone, native UI, and corresponding MCP calls. Open the default standalone page and verify it stays free of a workspace parameter while resuming its Workspace; open its legacy URL and verify only a redundant own ID is removed while preserving query, project_root, other parameters and fragment. Foreign or chat-bound links retain their target.

In a disposable protocol host and disposable valid Project, verify that `workspace_open` alone exposes `ui://caprmedio/workbench.html`; the compatibility probe remains separately linked; unknown resource URIs and unexpected inputs fail. Verify the resource is self-contained `text/html;profile=mcp-app` with no external script or stylesheet references, Workbench HTTP request, browser opening, or second server.

Verify native bootstrap accepts only the `workspace_open` host tool input's non-empty `session_id` and explicit `project_root` plus its initial structured result. Exercise either input/result arrival order, require the exact supplied IDs and initial Workspace, and verify no second `workspace_open` call occurs. For absent input or result, verify a binding error is shown and no backend call, URL/localStorage identity fallback, synthetic native session, or alternative Workspace selection occurs.

Mount the same Svelte App through its HTTP and MCP transports. For MCP, verify every existing operation makes one `tools/call`, retains `project_root`, returns `structuredContent` unchanged, and rejects `isError`. Exercise open state, list/get, create/update/run/fetch/focus/rename/remove/save, conflict preservation, and query log through both transports; verify they reach the same existing handlers and effects. Verify the native mode does not apply standalone URL, localStorage, or draft-migration behavior.

In a real new or resumed Codex chat with the installed local plugin and a disposable valid Project/Workspace, invoke the real `workspace_open` with the hook-supplied native session ID and trusted Project root. Verify that Codex renders the Workbench in-chat; the shown Workspace ID equals the tool input session; a read-only Workspace/View operation traverses the bridge; state is visible through ordinary MCP or standalone use of the same backend; and no browser, second chat, or second MCP connection appears. Exercise fullscreen or move-to-panel only if the host offers it and report the observed placement.

A synthetic or disposable-host test proves protocol and application behavior only. It is insufficient to claim native Codex rendering, right-panel support, or complete native Workbench delivery. The read-only probe separately verifies standard MCP Apps compatibility and must not be used as Workbench activation evidence.

Call the read-only `workbench_ui_probe` through the existing MCP connection. Verify its component renders inside Codex, displays the initial host tool result, and reports a successful separate `workbench_ui_ping` bridge call. Verify resource and tools work over real MCP transport, reject unexpected arguments and unknown resource URIs, and do not start Workbench. Verify inline/fullscreen declaration, current and offered mode display, Expand only when fullscreen is available, accepted/inline-retained/rejected/unsupported results, actual returned-mode display, and no unavailable request. If the real host does not render native UI, record delivery as incomplete and do not substitute a browser page. Observe move-to-panel only if offered; otherwise record right-panel delivery as unproven.

Verify `view_duplicate` through the public MCP and shared HTTP interface. It returns a new View ID and current Workspace state, keeps source SQL/cursor unchanged, copies them exactly into the new View, and preserves the created name and order on reload. Exercise unnamed sources, suffix collisions and numbering gaps. Reject unknown IDs and malformed or extra arguments without effects. A duplicate has revision zero, no result or saved-item identity, and no SQL execution or saved Journal effect. Running or closing either View leaves the other's independent result behavior unchanged.
