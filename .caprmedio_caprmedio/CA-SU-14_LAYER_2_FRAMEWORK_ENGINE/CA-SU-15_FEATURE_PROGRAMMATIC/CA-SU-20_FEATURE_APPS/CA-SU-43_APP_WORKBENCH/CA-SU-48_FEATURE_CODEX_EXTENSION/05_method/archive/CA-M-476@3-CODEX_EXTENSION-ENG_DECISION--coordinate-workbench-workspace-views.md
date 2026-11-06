---
atom_id: CA-M-476
ref_id: CA-M-476@3
container:
  scope_unit: CA-SU-48
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workspace
tier: 4
relations:
  method_for:
  - CA-R-2902
  - CA-R-2903
status: Archived
version: 3
updated_at: 2026-11-06 01:46:23 +0400
carrier_destination:
  file:
    name: CA-M-476@3-CODEX_EXTENSION-ENG_DECISION--coordinate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/05_method/archive
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Coordinate Workbench Workspace Views

## Claim

For native panel mode, use the existing Codex chat as the Workspace boundary. Keep one native panel Workspace per chat and keep its Views isolated from every other chat and Project. A page opened by `open_in_codex(type=browser)` is not the panel surface. Standalone mode uses its persisted browser Session ID as its own Workspace identity, with no native chat boundary.

Implement View operations as small adapters over the existing query executor, pagination, successful-run saving, saved Journal and browser autosave. Keep the caller's order; do not add a magic Workflow or a new scheduler. Return Run metadata first and fetch result rows only when requested.

Keep the query log separate from saved Views. Record only the approved SQL, outcome, error and counts. The parent Workbench backend owns query-log retention: retain entries for two days in hourly batches; this Method adds no query-log TTL, expiry, or cleanup behavior. Do not store rows, duplicate schema data or add a cleanup daemon.

## Native plugin panel

Use the host-provided native session and trusted Project context. Reuse the existing Workspace/View backend and MCP operations; do not add a second MCP connection, synthetic session, standalone chat, scheduler or UI-specific service. Use the standard MCP Apps resource/bridge only when the host supports it, and keep the contract host-neutral.

## Shared backend identity and lifecycle

For each explicit Project, route the standalone browser and native plugin panel through the same existing backend Workspace/View model. The native panel mode uses the supplied native Codex `session_id` unchanged. The standalone mode creates or reuses one unique Session ID in the existing browser localStorage and opens its own Workspace with that mode-local identity; never manufacture a native Codex session ID for standalone mode and never merge a standalone Workspace with another chat or Project.

In the standalone browser, resolve an explicit `?workspace=<workspace_id>` URL before restoring View state. Native plugin UI uses its supplied host session binding. Preserve every existing URL parameter while assigning a standalone Workspace, including the saved-query/open-saved `query`. Treat `embedded=1` only as an embedded density-default marker; it is not a backend identity or lifecycle input.

On the first explicit standalone binding, migrate an existing unbound browser draft at most once into that standalone Workspace without executing SQL. Keep the original local copy until the backend confirms the copy. Do not merge shared Project Workspaces, import another chat's draft, or import the unbound draft into a native plugin Workspace.

Give every View one SQL query. An edit may be temporarily invalid, but Run and Check validate the whole View and reject multiple statements instead of selecting one at the cursor. Keep old saved multi-script queries intact and never execute only part of one through a View. Both UIs call the same existing create, update, run, fetch, focus, rename, remove and save operations.

Keep result-cache TTL separate from query-log retention; use the shared Workbench runtime configuration's default of 3600 seconds unless an existing configured value applies. Neither UI supplies a query-log TTL or cleanup lifecycle. Add no new function, shared-service layer, lease, heartbeat, chat or Domain entity.
