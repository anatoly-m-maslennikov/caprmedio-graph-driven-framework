---
identity:
  atom_id: CA-R-2952
  ref_id: CA-R-2952
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Active
  version: 3
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-R-2952-WORKBENCH-SOLUTION--show-workbench-source-sync-status.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-696
  - CA-M-491
---

## Summary

Show Workbench source indexing sync status

## Claim

### Prose Claim

The Workbench must expose whether source-to-DuckDB indexing is running and when it last completed successfully.

- During initial indexing or a source refresh, report `syncing: true`. The status describes source capture and DuckDB materialization, not query execution, browser autosave or another UI operation.
- Set `last_synced_at` only after a successful capture/materialization reconciliation has committed, or has confirmed the existing committed DuckDB state is current. Return it as a UTC or offset-bearing timestamp. A failed run keeps the previous timestamp and the existing source/indexing failure state.
- Before the first successful commit, return `last_synced_at: null`; the frontend displays `Not synced yet`.
- Provide the small read-only status payload over the existing HTTP and MCP parity surface. Its fields are `syncing` and `last_synced_at`. Do not restart a failed Workbench automatically.
- Poll this status through the existing frontend polling mechanism. Show a small status text at the top right and render a non-null timestamp in the browser's local time. Do not add a new service, event stream, queue or scheduler.

## Details

### Status interface

Deliver native MCP `workbench_status({})` and the matching read-only `POST /caprmedio/workbench/<project_name>/status` connector with `{}` (plus the trusted `project_root` envelope in shared mode). Register it through the grouped Service catalog and keep the normal blacklist and selected-root validation. Return exactly `syncing` (boolean) and `last_synced_at` (ISO-8601 UTC or offset-bearing timestamp, or `null` before the first successful reconciliation). Do not add an error field; the existing error boundary remains. The status is source capture-to-DuckDB indexing state, not query execution or browser autosave.

The response remains available while a capture or materialization operation is running and must not wait for the long lifecycle or query lock, start an uninitialized owner, execute SQL, or restart a failed owner. A successful capture/materialization reconciliation turns `syncing` off and advances `last_synced_at`; it may reuse unchanged committed DuckDB state without a new database write. A failed run keeps the previous timestamp and existing failure state. The frontend may poll it through its existing interval. Do not deliver a new service, event stream, scheduler, retry or restart workflow.

### Status snapshot

Keep a small owner-local status snapshot beside the existing Workbench indexing state. Set `syncing` before initial capture or refresh begins and clear it when that attempt finishes. Advance `last_synced_at` only after capture/materialization reconciliation succeeds and the existing committed DuckDB state is current; when the source signature is unchanged, reuse that committed state without forcing a new database write. Record the timestamp as an offset-bearing value. On failure, preserve the previous timestamp and retain the existing failure state and error boundary.

Read the snapshot without waiting on the long lifecycle, refresh or query lock, without triggering owner start, indexing, query execution or restart. This lets a status request observe `syncing: true` while a long initial or refresh operation is running. An uninitialized owner returns the same shape with `syncing: false` and `last_synced_at: null`; the existing owner lifecycle remains responsible for starting Workbench operations.

Expose the same read-only status contract through the native MCP surface and its matching HTTP adapter, using the existing discovery/catalog and parity pattern. The payload is exactly `syncing` and `last_synced_at`. Reuse the existing frontend polling interval. Do not add a watcher service, event stream, scheduler, retry loop, or automatic restart.
