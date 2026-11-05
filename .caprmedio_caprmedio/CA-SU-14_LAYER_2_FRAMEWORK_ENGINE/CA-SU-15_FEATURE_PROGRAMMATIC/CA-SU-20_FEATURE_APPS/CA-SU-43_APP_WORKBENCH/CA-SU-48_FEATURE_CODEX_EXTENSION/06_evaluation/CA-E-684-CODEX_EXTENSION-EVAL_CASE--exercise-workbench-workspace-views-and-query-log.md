---
atom_id: CA-E-684
ref_id: CA-E-684
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
status: Active
version: 2
updated_at: 2026-11-05 20:32:45 +0400
carrier_destination:
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

Using the real browser and MCP surfaces, verify that one existing embedded native Codex chat resumes one isolated Workspace with at least one View. Verify Workspace listing and opening, unknown-ID errors, first/last View creation, View IDs returned by create/list and accepted by every single-View operation, View listing, SQL update, focus, rename, save, paginated fetch with optional preview and rejection of removing the last View. Verify that Run returns status, counts, result ID and errors without rows by default, and that fetching rows is optional.

Verify embedded browser autosave and restore are keyed by Project and native session/Workspace ID, while unbound legacy browser drafts remain separate and are not silently imported into an embedded native Workspace.

Verify that a successful Run and a failed Run each add the exact query-log fields, while Check adds none. Verify the original whole-View SQL is preserved, preview does not rewrite it, row and column counts are reported, query-log list/fetch works through both backend and MCP, and the parent Workbench backend retains entries for two days in hourly batches without a duplicate extension expiry path. Verify that no result rows or extra schema data are stored, saved Views remain available without query-log retention, and existing saved IDs and Journal records remain usable. Result-cache TTL is separate and uses the shared Workbench runtime configuration's default of 3600 seconds unless an existing configured value applies.

Verify that browser and MCP operations have the same effects, that operations cannot read, write or focus another Workspace without its explicit correct ID, and that no standalone chat, magic Workflow, code runner, scheduler or retry behavior is required.

Verify that embedded browser autosave and restore are keyed by the selected Project and native session/Workspace ID. Two embedded native chats must not restore or overwrite each other's unsaved SQL, and unbound legacy browser drafts remain separate.

## Unified standalone and embedded evaluation

Use two real browser contexts against the same explicit Project: one standalone browser context with no chat and one embedded native Codex context. Verify that both use the same backend Workspace/View model and existing create, update, run, fetch, focus, rename, remove and save effects. In the standalone context, verify that one unique localStorage Session ID survives reload and opens its own Workspace without creating or claiming a native Codex `session_id`; in the embedded context, verify that the supplied native session identity is unchanged. An explicit `?workspace=<workspace_id>` URL must select the same Workspace from either context. Verify that `embedded=1` changes only the embedded density default and cannot change Workspace identity. When a standalone Workspace is assigned, the existing saved-query/open-saved `queryURL` and all other URL parameters remain intact.

Seed an unbound browser draft, bind the standalone context once, and verify that the draft is copied into its own Workspace without any SQL execution. Verify that the local copy remains until backend confirmation, the copy is not repeated on a confirmed retry, the exact draft content is not lost, no shared Project Workspace is merged, and no draft from another chat is imported into the embedded context. Verify that MCP sees the same resulting Workspace/View state and effects as the browser while preserving the explicit Project and Workspace IDs.

Edit one View to a temporarily invalid state and verify that both Run and Check reject multiple SQL statements without silently selecting the statement at the cursor. Verify that an existing saved multi-script query remains unchanged and is never partially executed through a View. Verify these results in both browser contexts and through the corresponding MCP calls.
