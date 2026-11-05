---
atom_id: CA-E-684
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
status: Archived
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 5
subjects:
  active: CAPRMEDIO_MODEL <+ Workspace
relations:
  evaluation_for:
  - CA-R-2902
  - CA-R-2903
  - CA-M-476
  - CA-D-681
carrier_destination:
  file:
    name: CA-E-684@1-CODEX_EXTENSION-EVAL_CASE--exercise-workbench-workspace-views-and-query-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/06_evaluation/archive
updated_at: 2026-11-05 16:45:35 +0400
---

## Summary

Exercise Workbench Workspace Views and Query Log

## Claim

Using the real browser and MCP surfaces, verify that one existing native Codex chat resumes one isolated Workspace with at least one View. Verify Workspace listing and opening, unknown-ID errors, first/last View creation, View IDs returned by create/list and accepted by every single-View operation, View listing, SQL update, focus, rename, save, paginated fetch with optional preview and rejection of removing the last View. Verify that Run returns status, counts, result ID and errors without rows by default, and that fetching rows is optional.

Verify browser autosave and restore are keyed by Project and native session/Workspace ID, while unbound legacy browser drafts remain separate and are not silently imported.

Verify that a successful Run and a failed Run each add the exact query-log fields, while Check adds none. Verify the original selected SQL is preserved, preview does not rewrite it, row and column counts are reported, query-log list/fetch works through both backend and MCP, entries older than seven days expire when the log is used, and no result rows or extra schema data are stored. Verify saved Views remain available without the query-log TTL and existing saved IDs and Journal records remain usable.

Verify that browser and MCP operations have the same effects, that operations cannot read, write or focus another Workspace without its explicit correct ID, and that no standalone chat, magic Workflow, code runner, scheduler or retry behavior is required.

Verify that browser autosave and restore are keyed by the selected Project and native session/Workspace ID. Two chats must not restore or overwrite each other's unsaved SQL, and unbound legacy browser drafts remain separate.
