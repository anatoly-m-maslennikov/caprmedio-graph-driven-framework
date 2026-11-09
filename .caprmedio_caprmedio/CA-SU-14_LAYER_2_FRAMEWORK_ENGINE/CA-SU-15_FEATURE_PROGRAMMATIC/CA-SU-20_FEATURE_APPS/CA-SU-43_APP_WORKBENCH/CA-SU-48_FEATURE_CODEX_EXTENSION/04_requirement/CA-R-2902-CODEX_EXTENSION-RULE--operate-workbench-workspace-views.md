---
identity:
  atom_id: CA-R-2902
  ref_id: CA-R-2902
context:
  container:
    scope_unit: CA-SU-48
  role: Requirement
  form: Rule
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Workspace
    dependencies:
    - CAPRMEDIO_MODEL <+ View
    - CAPRMEDIO_MODEL <+ Project
  tier: 3
state:
  status: Active
  version: 6
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-R-2902-CODEX_EXTENSION-RULE--operate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/04_requirement
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-476
  - CA-D-681
---

## Summary

Operate Workbench Workspace Views

## Claim

### Prose Claim

The Workbench **must** be exposed as a native plugin UI in the existing Codex chat. A page opened by `open_in_codex(type=browser)` is not an integrated plugin UI and does not satisfy this requirement. The native UI **must not** create a standalone chat, host-specific side-panel API, browser iframe fallback, second MCP service, or separate Workspace identity.

The existing `workspace_open(session_id)` **must** open the native Workbench UI for the supplied chat. The host supplies the exact native `session_id` and trusted Project context; the initial response supplies that Workspace’s state. The UI **must** bind only after both required input values and that result are available. Missing context is a binding error: it **must not** issue backend calls, infer identity from a URL or localStorage, invent a native session ID, select another Workspace, or open a Workspace again.

Each native Codex chat has one isolated Workspace with at least one View. `workspace_open` initializes or resumes only the Workspace for its supplied native session. Except for this explicit initialization, unknown Workspace or View IDs **must** return an error and **must not** silently select another chat or Project. Existing standalone browser drafts and their localStorage Session ID remain standalone-only and **must not** be silently migrated into a native Workspace.

MCP **must** provide only the minimum operations needed to list known Workspaces for an explicit Project, get a Workspace by ID and open a Workspace by an explicit native Codex `session_id`. Each View **must** have a stable string ID. Create and list operations **must** return View IDs, and every operation on one View **must** take its explicit View ID. Native UI state and standalone browser autosave and restore **must** be keyed by Project and native session/Workspace ID.

The native UI and standalone browser **must** expose the same Workspace, View and query-log capabilities through the same Workbench backend. Every operation **must** retain the explicitly selected Project and chat Workspace. No UI-specific create, update, run, fetch, focus, rename, remove, save, query, or backend path is introduced.

View operations remain caller-ordered and support `view_create`, `view_list`, `view_update`, `view_run`, `view_check`, `view_fetch`, `view_focus`, `view_rename`, `view_remove`, and `view_save` with their existing explicit Workspace and View IDs. Removing the last View is rejected. Run returns status, counts, a result ID when one exists and errors without rows by default; paginated fetch returns rows later. Existing native SQL execution, pagination, successful-run saving, saved Journal records, saved IDs and browser autosave are reused. Saving remains separate from the temporary query log.

View Save **must** reuse the existing `view_save` capability with the selected Workspace and View identity and **must not** add a second save operation. View Run **must** return execution metadata without serializing the first result page; row data remains available through the separate paginated fetch operation. Existing standalone query-run compatibility remains outside this extension.

The native UI, standalone browser and MCP **must** expose the same Workspace and View effects. Each View is one SQL query: Run and Check validate the whole View, reject multiple statements, and never select by cursor. Existing saved multi-script queries remain intact and are never partially executed through a View. No magic Workflow, separate chat controls, code runner, scheduler, retry behavior, or standalone-chat bridge is introduced.

In the standalone browser, an explicit `?workspace=<workspace_id>` URL **must** select that Workspace. `embedded=1` is only a density-default marker and **must not** affect backend identity or Workspace selection. Assigning a standalone Workspace **must** preserve existing URL parameters, including the saved-query/open-saved `query`. On first explicit standalone Workspace binding, migrate an unbound browser draft at most once without executing SQL; retain the local copy until the backend confirms the copy. Do not repeat a confirmed migration, merge shared Project Workspaces, import another chat's draft, or import an unbound browser draft into a native Workspace.

## Details

### Native application and transport

The shared Svelte Workbench UI **must** use MCP Apps initialization and the `tools/call` bridge in native mode. It **must** inject the explicit `project_root` into every call, preserve `structuredContent`, reject `isError`, and add no domain logic, response adapter, MCP service, chat, or UI-specific handler. Standalone mode retains the existing HTTP bootstrap; native mode and standalone mode use the same `App.svelte` and Workbench backend.

`workspace_open` is the sole UI-bearing MCP tool. Its descriptor **must** link `ui://caprmedio/workbench.html`, served as `text/html;profile=mcp-app`. `workbench_app.html` **must** be one self-contained MCP App resource built with the existing Vite/Svelte toolchain: its JavaScript and CSS are inline, it opens no browser, makes no Workbench HTTP request, and needs no second server. `FEATURE_MCP` adds that resource URI only to the existing `workspace_open` descriptor and serves the built resource through its existing registry/read handler; existing dispatch, Project validation, and structured-result paths remain unchanged.

`FEATURE_CODEX_EXTENSION` instructions **must** direct the caller to invoke `workspace_open` with the host-supplied session ID and trusted Project root. Its hook supplies context only, starts nothing, and registers no panel; `plugin.json` adds no panel or connection declaration. The existing `caprmedio-workbench` package **must** be registered in `.agents/plugins/marketplace.json` under `caprmedio-local` with local source `./LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_CODEX_EXTENSION/plugin`. The desktop app discovers it after restart and the Operator installs it and explicitly trusts the bundled hook through `/hooks`. Activation requires a new or resumed native chat; building or releasing the backend neither installs the plugin nor retroactively runs a hook.

### Host boundary and evidence

Native UI delivery is complete only when the host renders the Workbench and it exercises the same MCP Workspace/View effects. The existing `workbench_ui_probe` and `workbench_ui_ping` are separate read-only compatibility evidence: the probe resource is not the Workbench resource and does not activate Workbench. They use the existing MCP connection, take no native arguments, return fixed messages, do not read Project data or start Workbench, and reject unexpected arguments and unknown resource URIs.

The probe alone links `ui://caprmedio/workbench-compatibility-v2.html` with `text/html;profile=mcp-app`. It declares inline and fullscreen capability, shows current and offered modes, enables Expand only when fullscreen is offered, requests it through `ui/request-display-mode`, displays the returned mode, and merges `ui/notifications/host-context-changed`. Acceptance, retained-inline, rejection, and unsupported-fullscreen cases remain distinct. Fullscreen or move-to-panel is exercised only if offered by the host; neither proves a persistent right panel. In a real host, right-panel support remains unproven unless an offered move-to-panel action preserves the same resource, initial result, and bridge.

### Project name boundary

Public `workspace_open` and `workspace_get` responses **must** include `project_name` alongside the existing Workspace state and request-derived `workspace_url`. The public Workspace adapter obtains `project_name` from the selected Project's validated settings through the existing ProjectSelection settings/name reader, for both HTTP and MCP. The initial native Workspace result supplies this canonical name for the Project header. A missing name is a binding error; it does not permit a directory-basename inference, query, parser, fallback name, or tool. Workspace persistence and other tool inputs remain unchanged.
