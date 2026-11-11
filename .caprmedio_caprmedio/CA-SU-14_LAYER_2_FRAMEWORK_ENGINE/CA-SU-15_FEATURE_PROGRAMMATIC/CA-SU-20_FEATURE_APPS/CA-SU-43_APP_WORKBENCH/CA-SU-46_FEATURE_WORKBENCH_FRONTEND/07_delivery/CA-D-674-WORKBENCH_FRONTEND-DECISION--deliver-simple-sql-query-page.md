---
identity:
  atom_id: CA-D-674
  ref_id: CA-D-674
context:
  container:
    scope_unit: CA-SU-46
  role: Delivery
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery
      <+ Packaging
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2727
  - CA-R-2952
state:
  status: Active
  version: 26
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-D-674-WORKBENCH_FRONTEND-DECISION--deliver-simple-sql-query-page.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/07_delivery
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

Deliver built Svelte/TypeScript/Vite static artifact through existing Python application at `/caprmedio/workbench/<project_name>`; Node is build-only. Missing build returns explicit HTTP 503 without building assets/starting server, while API/MCP remain available. Current Project uses `/caprmedio/workbench/caprmedio` and shared assets path; mismatched declared Project name is 404. Browser Run/Page/Check stays beneath current Project page path and preserves project_root, Workspace bindings and IDs. Standalone Workspace ID stays in local storage; remove legacy workspace parameter only when it equals that stored ID, preserving other URL parts. Plugin opener alone adds `embedded=1`.

Bind all controls to existing Workspace/View/MCP contracts for Run/Page/Check/View-save/Load/Saved List/Schema, with active View context, one View-one-query and whole-query semantics. Do not use unbound browser `query_run` or add save/worksheet routes, evaluator, service or capability. Frontend owns presentation/pages/UI state; database owns SQL operations. Run/Check/page/error save nothing. Post-result save failure keeps rows/query ID/prior saved identity/dirty state, shows partial/save_error and does not retry/rollback; successful Run & Save exposes ID/URL/kind/name only on success. Result lifetime is backend-owned; no sharing/auth/dedup/retry/repair/rollback/deletion workflow.

Render existing read-only sync status as Syncing, Not synced yet, local-time last successful sync, or existing failure through polling only; it is neither query/autosave status nor new service/stream/queue/scheduler. Mount canonical tabs/editor/library/results/palette/settings/status with loading/error/accessibility, bounded scrolling, visible headers, separately scrollable long values, positional/duplicate columns and exact counts. Do not add second grid/DOC/TREE/frontend replacement. Detail belongs to editor/visual/result/grid/rename/duplicate receivers.

Use page path for Run/Page/Check/view-save/load/saved-list/schema; `POST /schema` accepts `{}` with shared metadata. No preview control is required. Browser interactive grid requests `result_delivery: inline`; generic MCP `query_run` remains for MCP callers. Label permanent saved queries Bookmarks distinct from Views; ordinary responses need not echo SQL but explicit Load/View-query reads do.
