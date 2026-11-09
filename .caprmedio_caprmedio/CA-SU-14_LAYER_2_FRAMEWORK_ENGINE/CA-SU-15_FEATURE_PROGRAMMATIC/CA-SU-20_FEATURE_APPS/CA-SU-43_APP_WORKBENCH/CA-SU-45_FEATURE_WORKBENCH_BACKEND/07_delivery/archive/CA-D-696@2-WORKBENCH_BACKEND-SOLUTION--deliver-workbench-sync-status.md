---
identity:
  atom_id: CA-D-696@2
  ref_id: CA-D-696@2
context:
  container:
    scope_unit: CA-SU-45
  role: Delivery
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2952
  - CA-M-491
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-D-696@2-WORKBENCH_BACKEND-SOLUTION--deliver-workbench-sync-status.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Deliver Workbench source indexing sync status

## Claim

### Prose Claim

Deliver native MCP `workbench_status({})` and the matching read-only `POST /caprmedio/workbench/<project_name>/status` connector with `{}` (plus the trusted `project_root` envelope in shared mode). Register it through the grouped Service catalog and keep the normal blacklist and selected-root validation. Return exactly `syncing` (boolean) and `last_synced_at` (ISO-8601 UTC or offset-bearing timestamp, or `null` before the first successful reconciliation). Do not add an error field; the existing error boundary remains. The status is source capture-to-DuckDB indexing state, not query execution or browser autosave.

The response remains available while a capture or materialization operation is running and must not wait for the long lifecycle or query lock, start an uninitialized owner, execute SQL, or restart a failed owner. A successful capture/materialization reconciliation turns `syncing` off and advances `last_synced_at`; it may reuse unchanged committed DuckDB state without a new database write. A failed run keeps the previous timestamp and existing failure state. The frontend may poll it through its existing interval. Do not deliver a new service, event stream, scheduler, retry or restart workflow.
