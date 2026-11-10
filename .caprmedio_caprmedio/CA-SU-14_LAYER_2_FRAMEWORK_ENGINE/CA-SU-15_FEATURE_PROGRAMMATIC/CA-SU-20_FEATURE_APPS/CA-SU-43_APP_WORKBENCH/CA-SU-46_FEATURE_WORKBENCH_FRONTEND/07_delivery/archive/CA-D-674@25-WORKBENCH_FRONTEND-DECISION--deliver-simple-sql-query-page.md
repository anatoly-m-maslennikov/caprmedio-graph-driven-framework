---
identity:
  atom_id: CA-D-674
  ref_id: CA-D-674@25
context:
  container:
    scope_unit: CA-SU-46
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Delivery <+ Packaging
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2727
  - CA-R-2952
state:
  status: Archived
  version: 25
  updated_at: 2026-11-10 00:46:37 +0400
destination:
  file:
    name: CA-D-674@25-WORKBENCH_FRONTEND-DECISION--deliver-simple-sql-query-page.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/07_delivery/archive
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Deliver a simple SQL query page through the shared connector

## Claim scope

The Workbench frontend and its same-listener HTTP delivery.

## Claim

### Prose Claim

Deliver the Workbench frontend as the built Svelte, TypeScript and Vite static artifact through the existing Python application at /caprmedio/workbench/<project_name>. Node is a build dependency, not a second runtime server. Keep the query API and MCP available when the frontend build is missing; return HTTP 503 with an explicit build-required error and do not build assets or start a frontend server automatically.

For the current Project, use /caprmedio/workbench/caprmedio and keep shared static assets under /caprmedio/workbench/assets. Require the URL Project name to match the selected declared Project; a mismatched name returns HTTP 404. Send browser Run, Page and Check requests under the current Project page path. Preserve project_root, explicit chat-bound or foreign Workspace parameters, and all ID formats. For an ordinary standalone URL, keep the generated Workspace ID in browser local storage and remove a legacy workspace parameter only when it equals that browser's persisted standalone ID; preserve query, project_root, other parameters and the fragment. The plugin opener alone appends embedded=1; an ordinary standalone URL does not gain the marker.

Bind the delivered controls to the existing Workbench Workspace/View and MCP contracts for Run, Page, Check, View save, Load, Saved List and Schema. Browser calls carry the active View context and do not use an unbound query_run route. Do not add a /save endpoint, a legacy Worksheet-save endpoint, a second query evaluator, a second web service, or a new backend or MCP capability. Keep a View as one query and let the existing contract own whole-query execution, saving, loading, saved-resource listing and query_schema metadata. Keep result formatting, page navigation and UI state in the frontend; SQL filtering, sorting and aggregation remain database operations.

Preserve the existing delivery error boundary. Run, Check, pagination and query errors create no saved entry. If a save fails after the result is complete, keep the visible rows and query ID, show outcome partial and save_error, preserve the previous saved identity and dirty state, and do not retry or roll back. Successful Run & Save answers expose saved_query_id, saved_query_url, kind and optional name only when saving succeeds. Result-cache retention follows the backend Workbench contract rather than a frontend expiry rule; do not add sharing, authentication, saved-Journal deduplication, retry, repair, rollback or deletion workflows in this delivery source.

Render the read-only source-to-DuckDB sync status through the existing frontend polling interval: show Syncing during initial or refresh indexing, Not synced yet before the first successful reconciliation, and the last successful last_synced_at in browser local time afterward. Preserve the existing failure state. This status is not query or browser-autosave status and does not add a service, event stream, queue or scheduler. Its backend HTTP/MCP parity remains governed by the shared sync-status contract and the shared Workbench Evaluation CA-E-781.

Mount the existing View tabs, query editor, saved library, result surface, command palette, settings and status through the canonical methods and requirements named below. Preserve loading and error states, accessible labels, bounded result scrolling, visible headers, separately scrollable long values, positional values, duplicate column names, exact row and column counts, and all SQL values. Do not define a second grid, a custom DOC or TREE result mode, or a frontend-only replacement for a shared contract. Detailed editor, visual-design, result-display, grid, rename and duplicate behavior is exercised by the destination sources rather than restated in this delivery decision.

Use `/caprmedio/workbench/<project_name>` for Run, Page, Check, view-save, load, saved-list and schema. POST `/view-save`, `/load` and `/saved-list` use the same MCP contracts; POST `/schema` accepts `{}` and returns the same table/column metadata. No preview UI control is required. Keep generic MCP `query_run` available for MCP callers, but do not route browser UI through it.

Label permanent saved queries as Bookmarks and distinguish them from saved Views in the saved library. Keep existing IDs, URLs and wire-field names. Request `result_delivery: inline` through the shared result-fetch contract for the interactive grid. An execution or page response need not echo editor SQL; explicit Load and View-query reads still return it.
