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
version: 4
updated_at: 2026-11-06 03:34:15 +0400
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

Use the real native Codex plugin panel and MCP surfaces. Do not count a page opened by `open_in_codex(type=browser)` as the plugin panel.

Verify that one current Codex chat opens one isolated Workspace with at least one View, using the host-provided native session identity and the explicit Project. Verify panel activation in the current chat, Workspace listing/opening, unknown-ID errors, first/last View creation, View IDs returned by create/list and accepted by every single-View operation, View listing, SQL update, focus, rename, save, paginated fetch with optional preview and rejection of removing the last View. Verify that Run returns status, counts, result ID and errors without rows by default, and fetching rows is optional.

Verify that the native plugin panel, standalone browser and MCP use the same Workspace and View effects. Two Codex chats must keep separate Workspaces and unsaved SQL. Verify that no standalone chat, synthetic native session, magic Workflow, code runner, scheduler or retry behavior is required.

Verify that a successful Run and a failed Run each add the exact query-log fields, while Check adds none. Verify the original whole-View SQL is preserved, preview does not rewrite it, row and column counts are reported, query-log list/fetch works through MCP and the panel, and the parent Workbench backend retains entries for two days in hourly batches without a duplicate extension expiry path. Verify that no result rows or extra schema data are stored, saved Views remain available without query-log retention, and existing saved IDs and Journal records remain usable. Result-cache TTL is separate and uses the shared Workbench runtime configuration's default of 3600 seconds unless an existing configured value applies.

## Native plugin panel evaluation

Use the installed local plugin in a new or resumed native Codex chat and call the Workbench UI through the host-supported native plugin surface. If the host exposes MCP Apps UI, exercise it through its standard resource/bridge. Verify that the UI renders in the chat, receives the native session and Project context, displays the current Workspace and Views, and can trigger at least one read-only Workspace/View operation. Verify no browser tab is opened by plugin activation and no second MCP connection is created. If the host exposes no native UI surface, record the panel as not delivered; do not substitute a browser page.

## Unified standalone and native plugin evaluation

Use one real standalone browser context with no chat and one real native Codex plugin UI context against the same explicit Project. Verify that both use the same backend Workspace/View model and existing create, update, run, fetch, focus, rename, remove and save effects. In the standalone context, verify that one unique localStorage Session ID survives reload and opens its own Workspace without creating or claiming a native Codex `session_id`; in the plugin context, verify that the supplied native session identity is unchanged. In the standalone browser, an explicit `?workspace=<workspace_id>` URL must select that Workspace; native plugin UI uses the supplied host session binding. Verify that `embedded=1` changes only the browser density default and cannot change Workspace identity. When a standalone Workspace is assigned, the existing saved-query/open-saved `query` parameter and all other URL parameters remain intact.

Seed an unbound browser draft, bind the standalone context once, and verify that the draft is copied into its own Workspace without any SQL execution. Verify that the local copy remains until backend confirmation, the copy is not repeated on a confirmed retry, the exact draft content is not lost, no shared Project Workspace is merged, and no draft from another chat is imported into the plugin context. Verify that MCP sees the same resulting Workspace/View state while preserving the explicit Project and Workspace IDs.

Edit one View to a temporarily invalid state and verify that both Run and Check reject multiple SQL statements without silently selecting the statement at the cursor. Verify that an existing saved multi-script query remains unchanged and is never partially executed through a View. Verify these results in the standalone browser, the native plugin UI and the corresponding MCP calls.

## Standalone URL

Open the default standalone page and verify that it stays free of a workspace parameter while using the browser-owned Workspace. Reload and verify the same Workspace and Views resume. Open its legacy URL with this browser's persisted standalone ID and verify that only that redundant parameter is removed; preserve query, project_root, other parameters and the fragment. Explicit foreign or chat-bound Workspace links keep their target, and embedded=1 keeps the supplied session ID. ID formats do not change.





## Native UI compatibility check

Call the read-only `workbench_ui_probe` through the existing MCP connection. Verify that its component renders inside Codex, displays the initial host tool result and reports a successful separate `workbench_ui_ping` call from its button. Verify the resource and both tools also work over the real MCP transport, reject unexpected arguments or unknown resource URIs, and do not start the Workbench data service. A synthetic host test verifies the component protocol only; it does not establish native Codex rendering or complete Workbench delivery.

## Presentation compatibility check

Verify that the probe declares inline and fullscreen support, displays the host mode and enables Expand only when the host offers fullscreen. Exercise acceptance, a response that keeps inline, a rejected request, and a host with no fullscreen support. Verify the actual returned mode is shown and no unavailable mode is requested. These browser cases test protocol behavior; observe Codex separately before claiming right-panel support.

In the real Codex host, observe where expansion is presented. If Codex offers a move-to-panel control, exercise it and verify the same MCP App resource, initial result and tool bridge still work in the right panel. If no such action is available or only fullscreen/inline is observed, record right-panel delivery as unproven. Do not invent a host API or substitute a browser page.
