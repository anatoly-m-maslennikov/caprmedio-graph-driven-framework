---
identity:
  atom_id: CA-R-2782
  ref_id: CA-R-2782@4
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
state:
  status: Archived
  version: 4
  updated_at: 2026-11-09 19:30:15 +0400
destination:
  file:
    name: CA-R-2782@4-WORKBENCH-SOLUTION--restart-workbench-without-restarting-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-676
  - CA-D-677
---

## Summary

Workbench can restart without restarting MCP

## Claim

Allow the Operator or an AI Agent to restart the selected Project's Workbench through the native MCP `workbench_restart({})` operation or an explicit health-page button, without restarting MCP, other services or the container. Restart closes the old Workbench owner, rebuilds its index from the admitted Current/Draft Atom sources and Current Scope Unit Declarations, and clears temporary query results. It preserves source files, saved queries and Views; old query-result IDs become unknown while saved-item IDs remain loadable. Return `{service: "workbench", status: "ready"}` only after the replacement Workbench is ready. If sources or startup remain invalid, return the explicit shared `workbench_unavailable` failure and leave Workbench unavailable until another explicit restart. Do not retry automatically, roll back, or write a Business Journal event.

## Details

`workbench_restart({})` accepts no service name, shell command or container arguments. Serialize restart with that Project's Workbench operations, including after caller cancellation, so no in-flight request uses a closed owner. MCP and unrelated services stay running. The service operation is synchronous and creates no Workflow, queue, background restart job, generic service registry, shell execution or Docker control.

The health page shows a Restart Workbench button using a native HTML POST form to `/caprmedio/health/workbench-restart`. On a Project server its body is empty. On a shared host it requires exactly one `project_root` field labelled Project folder; reject unknown or repeated fields before any effect. Route the action through the same gateway operation, Project selection, blacklist and public error boundary as MCP; do not reimplement lifecycle control in the page. Show the ready or failure outcome as escaped text. Do not automatically repeat the action or restart another service.

GET health requests remain read-only and preserve existing JSON readiness and HTML snapshot behavior. Opening the health page does not restart anything. Keep the health page available when Workbench fails. The explicit action requires no separate approval form and adds no generic service picker, shell commands, container control, JavaScript dependency or Workbench query-editor button.

An invalid Scope Unit Declaration continues to stop indexing and require explicit restart. Fixing its file alone does not restart Workbench. Both MCP and health expose the same restart operation and preserve the same source and saved-item data.
