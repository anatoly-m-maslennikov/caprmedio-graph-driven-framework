---
identity:
  atom_id: CA-E-684
  ref_id: CA-E-684
context:
  container:
    scope_unit: CA-SU-48
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - CAPRMEDIO_MODEL <+ Workspace
  tier: 6
relations:
  evaluation_for:
  - CA-R-2902
  - CA-R-2903
state:
  status: Active
  version: 10
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-E-684-CODEX_EXTENSION-EVAL_CASE--exercise-workbench-workspace-views-and-query-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/06_evaluation
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Exercise Workbench Workspace Views and Query Log

## Claim

### Prose Claim

Use the real native Codex plugin UI and MCP surfaces. A browser page is not the plugin UI. Verify that the host-provided native session opens its isolated Workspace with at least one View for the explicit Project. Verify a read-only Workspace/View operation through the shared backend.

Verify the native UI, standalone browser and MCP use the same Workspace/View effects. Two Codex chats must keep separate Workspaces and unsaved SQL. Verify no standalone chat, synthetic native session, magic Workflow, code runner, scheduler, or retry behavior is required.

In a disposable protocol host and disposable valid Project, verify that `workspace_open` alone exposes `ui://caprmedio/workbench.html`; the compatibility probe remains separately linked; unknown resource URIs and unexpected inputs fail. Verify the resource is self-contained `text/html;profile=mcp-app` with no external script or stylesheet references, Workbench HTTP request, browser opening, or second server.

Verify native bootstrap accepts only the `workspace_open` host tool input's non-empty `session_id` and explicit `project_root` plus its initial structured result. Exercise either input/result arrival order, require the exact supplied IDs and initial Workspace, and verify no second `workspace_open` call occurs. For absent input or result, verify a binding error is shown and no backend call, URL/localStorage identity fallback, synthetic native session, or alternative Workspace selection occurs.

Through the native MCP transport, exercise every existing Workspace/View and query-log operation. Each call retains the exact `project_root`, uses one `tools/call`, preserves `structuredContent`, rejects `isError`, and reaches the shared handler. Check transport binding and error propagation without repeating the shared operation acceptance cases. Native mode must not apply standalone URL, localStorage or draft-migration behavior.

In a real new or resumed Codex chat with the installed local plugin and a disposable valid Project/Workspace, invoke the real `workspace_open` with the hook-supplied native session ID and trusted Project root. Verify that Codex renders the Workbench in-chat; the shown Workspace ID equals the tool input session; a read-only Workspace/View operation traverses the bridge; state is visible through ordinary MCP or standalone use of the same backend; and no browser, second chat, or second MCP connection appears. Exercise fullscreen or move-to-panel only if the host offers it and report the observed placement.

A synthetic or disposable-host test proves protocol and application behavior only. It is insufficient to claim native Codex rendering, right-panel support, or complete native Workbench delivery. The read-only probe separately verifies standard MCP Apps compatibility and must not be used as Workbench activation evidence.

Call the read-only `workbench_ui_probe` through the existing MCP connection. Verify its component renders inside Codex, displays the initial host tool result, and reports a successful separate `workbench_ui_ping` bridge call. Verify resource and tools work over real MCP transport, reject unexpected arguments and unknown resource URIs, and do not start Workbench. Verify inline/fullscreen declaration, current and offered mode display, Expand only when fullscreen is available, accepted/inline-retained/rejected/unsupported results, actual returned-mode display, and no unavailable request. If the real host does not render native UI, record delivery as incomplete and do not substitute a browser page. Observe move-to-panel only if offered; otherwise record right-panel delivery as unproven.

Use a fixture whose directory basename differs from its declared Project name. Verify HTTP and MCP workspace_open/workspace_get return the declared project_name and the native Workbench header displays it. Workspace documents do not gain a persisted Project-name field. A native initial Workspace result missing project_name reports a binding error before further tool calls; no directory-basename fallback is used.
