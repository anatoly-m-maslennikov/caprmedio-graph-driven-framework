---
atom_id: CA-R-2902
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
status: Active
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Workspace
  depends_on:
  - CAPRMEDIO_MODEL <+ View
  - CAPRMEDIO_MODEL <+ Project
relations: {}
carrier_destination:
  file:
    name: CA-R-2902-CODEX_EXTENSION-RULE--operate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/04_requirement
updated_at: 2026-11-05 16:45:35 +0400
---

## Summary

Operate Workbench Workspace Views

## Claim

The embedded Workbench **must** use the existing native Codex chat. It **must not** create a standalone chat. Each native Codex chat has one isolated Workspace with at least one View.

The browser URL **must** bind the Workbench state with `?workspace=<session_id>`. Existing browser drafts without that binding **must** remain separate and **must not** be silently migrated into a native Workspace.

MCP **must** provide only the minimum operations needed to list known Workspaces for an explicit Project, get a Workspace by ID and open a Workspace by an explicit native Codex `session_id`. `workspace_open` **must** initialize the Workspace for that supplied native chat when it does not exist. Except for that explicit initialization, an unknown Workspace or View ID **must** return an error; the operation **must not** silently select another chat or Project.

View operations **must** be caller-ordered and **must** support `view_create(workspace_id, position = first|last)`, `view_list(workspace_id)`, `view_update(workspace_id, view_id, sql)`, `view_run(workspace_id, view_id, preview?)`, `view_fetch(workspace_id, view_id, offset, page_size, preview?)`, `view_focus(workspace_id, view_id)`, `view_rename(workspace_id, view_id, name)`, `view_remove(workspace_id, view_id)` and `view_save(workspace_id, view_id)`. Removing the last View **must** be rejected.

Each View **must** have a stable string ID. Create and list operations **must** return View IDs, and every operation on one View **must** take its explicit View ID. Browser autosave and restore **must** be keyed by Project and native session/Workspace ID. Existing unbound browser drafts **must** remain separate and **must not** be silently imported into a native Workspace.

A Run **must** return status, counts, a result ID when one exists and errors, without result rows by default. The caller **may** fetch rows later through the existing pagination capability; an Operator or Agent **must not** be forced to read the full result. Existing native SQL execution, pagination, successful-run saving, saved Journal records, saved IDs and browser autosave **must** be reused. Saving a View remains separate from the temporary query execution log.

View Save **must** reuse the existing `view_save` capability with the selected Workspace and View identity. It **must not** add a second save operation. View Run **must** return execution metadata without serializing the first result page; row data remains available through the separate paginated fetch operation. Existing standalone query-run compatibility remains outside this extension.

The browser and MCP **must** expose the same Workspace and View capabilities. No magic multi-operation Workflow, separate chat controls, code runner, scheduler or retry behavior is introduced by this requirement.
