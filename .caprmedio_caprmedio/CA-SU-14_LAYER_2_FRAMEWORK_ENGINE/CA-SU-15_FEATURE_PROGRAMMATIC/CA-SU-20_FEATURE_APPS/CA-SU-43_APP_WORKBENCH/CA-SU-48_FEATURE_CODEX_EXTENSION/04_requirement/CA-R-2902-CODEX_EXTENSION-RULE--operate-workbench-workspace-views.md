---
atom_id: CA-R-2902
ref_id: CA-R-2902
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
status: Active
version: 2
updated_at: 2026-11-05 20:32:45 +0400
carrier_destination:
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

The embedded Workbench **must** use the existing native Codex chat. It **must not** create a standalone chat. Each embedded native Codex chat has one isolated Workspace with at least one View.

The embedded browser URL **must** bind the Workbench state with `?workspace=<session_id>`. Existing browser drafts without that binding **must** remain separate and **must not** be silently migrated into an embedded native Workspace.

Embedded MCP **must** provide only the minimum operations needed to list known Workspaces for an explicit Project, get a Workspace by ID and open a Workspace by an explicit native Codex `session_id`. `workspace_open` **must** initialize the embedded Workspace for that supplied native chat when it does not exist. Except for that explicit initialization, an unknown Workspace or View ID **must** return an error; the operation **must not** silently select another chat or Project.

View operations **must** be caller-ordered and **must** support `view_create(workspace_id, position = first|last)`, `view_list(workspace_id)`, `view_update(workspace_id, view_id, sql)`, `view_run(workspace_id, view_id, preview?)`, `view_check(workspace_id, view_id, cursor_position?)`, `view_fetch(workspace_id, view_id, offset, page_size, preview?)`, `view_focus(workspace_id, view_id)`, `view_rename(workspace_id, view_id, name)`, `view_remove(workspace_id, view_id)` and `view_save(workspace_id, view_id)`. Removing the last View **must** be rejected.

Each View **must** have a stable string ID. Create and list operations **must** return View IDs, and every operation on one View **must** take its explicit View ID. Embedded browser autosave and restore **must** be keyed by Project and native session/Workspace ID. Existing unbound browser drafts **must** remain separate and **must not** be silently imported into an embedded native Workspace.

A Run **must** return status, counts, a result ID when one exists and errors, without result rows by default. The caller **may** fetch rows later through the existing pagination capability; an Operator or Agent **must not** be forced to read the full result. Existing native SQL execution, pagination, successful-run saving, saved Journal records, saved IDs and browser autosave **must** be reused. Saving a View remains separate from the temporary query execution log.

View Save **must** reuse the existing `view_save` capability with the selected Workspace and View identity. It **must not** add a second save operation. View Run **must** return execution metadata without serializing the first result page; row data remains available through the separate paginated fetch operation. Existing standalone query-run compatibility remains outside this extension.

The browser and MCP **must** expose the same Workspace and View capabilities. No magic multi-operation Workflow, separate chat controls, code runner, scheduler or retry behavior is introduced by this requirement.

## Shared standalone and embedded boundary

The standalone browser and embedded Workbench **must** use one existing Workbench backend per explicit Project and the same Workspace/View model. The standalone browser has no chat. Its existing localStorage **must** retain one unique standalone Session ID; that ID opens the standalone browser's own backend Workspace and **must not** be invented as a native Codex `session_id`. The embedded native Codex session identity remains unchanged. Neither UI may merge its Workspace with another chat or another Project.

An explicit `?workspace=<workspace_id>` URL **must** select the same Workspace in either UI. For embedded use, the existing native session binding remains the native Workspace identity; for standalone use, the mode-local Session ID is the standalone identity. The `embedded=1` URL marker is only a density-default marker and **must not** affect backend identity or Workspace selection. Assigning a standalone Workspace **must** preserve existing URL parameters, including the saved-query/open-saved `queryURL`.

The existing MCP/HTTP `workspace_open` boundary accepts the supplied native session for embedded mode or the persisted standalone Session ID for standalone mode. It **must not** manufacture a native session for standalone mode or silently choose a different Workspace.

The existing browser View operations are the backend operations for both UIs. Add no UI-specific create, update, run, fetch, focus, rename, remove or save path. A View is one SQL query: editing may temporarily be invalid, but Run and Check **must** reject multiple statements and **must not** silently choose the statement at the cursor. Existing saved multi-script queries remain intact and **must not** be executed partially through a View.

An unbound browser draft **must** survive binding. On the first explicit standalone Workspace binding, perform at most one migration into that standalone Workspace without executing SQL; retain the local copy until the backend confirms the copy. Do not merge shared Project Workspaces or automatically import drafts from another chat, and do not import an unbound browser draft into an embedded native Workspace.
