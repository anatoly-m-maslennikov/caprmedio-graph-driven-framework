---
identity:
  atom_id: CA-D-681@13
  ref_id: CA-D-681@13
context:
  container:
    scope_unit: CA-SU-48
  role: Delivery
  form: Solution
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - CAPRMEDIO_MODEL <+ Workspace
  tier: 5
relations:
  delivery_for:
  - CA-R-2902
  - CA-R-2903
  - CA-M-476
state:
  status: Archived
  version: 13
  updated_at: 2026-11-09 17:00:18 +0400
destination:
  file:
    name: CA-D-681@13-CODEX_EXTENSION-SOLUTION--deliver-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/07_delivery/archive
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Deliver Workbench Workspace Views

## Claim

### Prose Claim

Deliver Workbench Workspace and View effects through the existing MCP connection and one shared Svelte Workbench UI. The native Codex UI exposes the shared Workbench capability through the existing MCP connection and shared Svelte Workbench UI. Do not add a second MCP service, standalone chat, chat controls, code runner, scheduler, magic Workflow, retry system, browser iframe, or host-specific panel API.



`workspace_open` is the sole UI-bearing MCP tool. Its descriptor links `ui://caprmedio/workbench.html`, served as `text/html;profile=mcp-app`. The native host passes `session_id` and explicit trusted `project_root` as its tool input; the `workspace_open` structured result supplies the initial Workspace. The UI waits for both input and result, uses their exact values, and does not invoke another open. Missing either context displays a binding error and performs no backend call.

Build `workbench_app.html` as one self-contained MCP App resource with the existing Vite/Svelte toolchain. Its JavaScript and CSS are inline; it opens no browser, makes no Workbench HTTP request, and needs no second server. The frontend owns the one shared `App.svelte` and transport selection: standalone retains the existing HTTP bootstrap; native initializes the MCP Apps bridge and calls the existing tools through `tools/call`. The native transport injects `project_root` for every call and preserves existing structured results and errors. It does not create an API adapter or business logic.

`FEATURE_MCP` adds the Workbench resource URI only to the existing `workspace_open` descriptor and exposes the built resource from its existing registry/read handler. Existing dispatch, Project validation, and structured results remain the backend path. `FEATURE_CODEX_EXTENSION` skill instructions direct the caller to invoke `workspace_open` with the host-supplied session ID and trusted Project root; its existing hook supplies context only, starts nothing, and registers no panel. `plugin.json` adds no panel or connection declaration.

Register the existing `caprmedio-workbench` package in `.agents/plugins/marketplace.json` under `caprmedio-local`, with local source `./LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_CODEX_EXTENSION/plugin`. The desktop app discovers it after restart; the Operator installs it and explicitly trusts the bundled hook through `/hooks`. Activation requires a new or resumed native chat; building or releasing the backend does not install the plugin or retroactively run a hook. Native UI delivery completes only when the host renders the Workbench and it exercises the same MCP Workspace/View effects.

The existing `workbench_ui_probe` and `workbench_ui_ping` remain separate read-only compatibility evidence: the probe resource is not the Workbench resource and does not activate Workbench. It may establish MCP Apps protocol compatibility but cannot establish actual Workbench delivery. Fullscreen or move-to-panel is exercised only if offered by the host; neither implies a persistent right panel.

The probe and ping use the existing MCP connection, take no native arguments, return fixed messages, do not read Project data or start Workbench, and reject unexpected arguments or unknown resource URIs. The probe alone links `ui://caprmedio/workbench-compatibility-v2.html` with `text/html;profile=mcp-app`. It declares inline and fullscreen capability, shows the current and offered modes, enables Expand only when fullscreen is offered, requests it through `ui/request-display-mode`, displays the returned mode, and merges `ui/notifications/host-context-changed`. Acceptance, retained-inline, rejection and unsupported-fullscreen cases are checked. In the real host, right-panel support remains unproven unless an offered move-to-panel action preserves the same resource, initial result and bridge.

Public workspace_open and workspace_get responses include project_name alongside the existing Workspace state and request-derived workspace_url. Obtain project_name from the selected Project's validated settings through the existing public Workspace adapter, for both HTTP and MCP. The native UI requires this name in its initial Workspace result and uses it for the Project header; a missing name is a binding error, not permission to derive a directory label. Other tool inputs and Workspace persistence remain unchanged.
