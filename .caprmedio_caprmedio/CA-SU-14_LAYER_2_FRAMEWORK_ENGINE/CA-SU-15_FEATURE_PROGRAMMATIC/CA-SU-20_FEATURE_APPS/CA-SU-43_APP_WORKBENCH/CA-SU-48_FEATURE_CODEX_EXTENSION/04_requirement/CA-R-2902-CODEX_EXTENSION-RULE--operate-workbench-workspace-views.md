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
  version: 5
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-R-2902-CODEX_EXTENSION-RULE--operate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/04_requirement
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Operate Workbench Workspace Views

## Claim

The Workbench **must** be exposed as a native plugin UI in the existing Codex chat. A page opened by `open_in_codex(type=browser)` is not an integrated plugin UI and does not satisfy this requirement. The native UI **must not** create a standalone chat, host-specific side-panel API, browser iframe fallback, second MCP service, or separate Workspace identity.

The existing `workspace_open(session_id)` **must** open the native Workbench UI for the supplied chat. The host supplies the exact native `session_id` and trusted Project context; the initial response supplies that Workspace’s state. The UI **must** bind only after both required input values and that result are available. Missing context is a binding error: it **must not** issue backend calls, infer identity from a URL or localStorage, invent a native session ID, select another Workspace, or open a Workspace again.

Each native Codex chat has one isolated Workspace with at least one View. `workspace_open` initializes or resumes only the Workspace for its supplied native session. Except for this explicit initialization, unknown Workspace or View IDs **must** return an error and **must not** silently select another chat or Project. Existing standalone browser drafts and their localStorage Session ID remain standalone-only and **must not** be silently migrated into a native Workspace.

MCP **must** provide only the minimum operations needed to list known Workspaces for an explicit Project, get a Workspace by ID and open a Workspace by an explicit native Codex `session_id`. Each View **must** have a stable string ID. Create and list operations **must** return View IDs, and every operation on one View **must** take its explicit View ID. Native UI state and standalone browser autosave and restore **must** be keyed by Project and native session/Workspace ID.

The native UI and standalone browser **must** expose the same Workspace, View and query-log capabilities through the same Workbench backend. Every operation **must** retain the explicitly selected Project and chat Workspace. No UI-specific create, update, run, fetch, focus, rename, remove, save, query, or backend path is introduced.

View operations remain caller-ordered and support `view_create`, `view_list`, `view_update`, `view_run`, `view_check`, `view_fetch`, `view_focus`, `view_rename`, `view_remove`, and `view_save` with their existing explicit Workspace and View IDs. Removing the last View is rejected. Run returns status, counts, a result ID when one exists and errors without rows by default; paginated fetch returns rows later. Existing native SQL execution, pagination, successful-run saving, saved Journal records, saved IDs and browser autosave are reused. Saving remains separate from the temporary query log.

View Save **must** reuse the existing `view_save` capability with the selected Workspace and View identity and **must not** add a second save operation. View Run **must** return execution metadata without serializing the first result page; row data remains available through the separate paginated fetch operation. Existing standalone query-run compatibility remains outside this extension.

The native UI, standalone browser and MCP **must** expose the same Workspace and View effects. Each View is one SQL query: Run and Check validate the whole View, reject multiple statements, and never select by cursor. Existing saved multi-script queries remain intact and are never partially executed through a View. No magic Workflow, separate chat controls, code runner, scheduler, retry behavior, or standalone-chat bridge is introduced.

In the standalone browser, an explicit `?workspace=<workspace_id>` URL **must** select that Workspace. `embedded=1` is only a density-default marker and **must not** affect backend identity or Workspace selection. Assigning a standalone Workspace **must** preserve existing URL parameters, including the saved-query/open-saved `query`. On first explicit standalone Workspace binding, migrate an unbound browser draft at most once without executing SQL; retain the local copy until the backend confirms the copy. Do not repeat a confirmed migration, merge shared Project Workspaces, import another chat's draft, or import an unbound browser draft into a native Workspace.
