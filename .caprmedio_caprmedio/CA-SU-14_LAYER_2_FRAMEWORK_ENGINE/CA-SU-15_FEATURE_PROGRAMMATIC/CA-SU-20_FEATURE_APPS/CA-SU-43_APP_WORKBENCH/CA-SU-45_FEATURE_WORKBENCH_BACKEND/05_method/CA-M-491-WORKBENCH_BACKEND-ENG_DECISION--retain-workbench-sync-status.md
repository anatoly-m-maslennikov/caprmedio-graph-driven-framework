---
atom_id: CA-M-491
ref_id: CA-M-491
container:
  scope_unit: CA-SU-45
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  method_for:
  - CA-R-2952
  - CA-R-2725
status: Active
version: 1
updated_at: 2026-11-05 19:04:52 +0400
carrier_destination:
  file:
    name: CA-M-491-WORKBENCH_BACKEND-ENG_DECISION--retain-a-non-blocking-workbench-source-indexing-status.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Retain a non-blocking Workbench source indexing status

## Claim

### Prose Claim

Keep a small owner-local status snapshot beside the existing Workbench indexing state. Set `syncing` before initial capture or refresh begins and clear it when that attempt finishes. Advance `last_synced_at` only after capture/materialization reconciliation succeeds and the existing committed DuckDB state is current; when the source signature is unchanged, reuse that committed state without forcing a new database write. Record the timestamp as an offset-bearing value. On failure, preserve the previous timestamp and retain the existing failure state and error boundary.

Read the snapshot without waiting on the long lifecycle, refresh or query lock, without triggering owner start, indexing, query execution or restart. This lets a status request observe `syncing: true` while a long initial or refresh operation is running. An uninitialized owner returns the same shape with `syncing: false` and `last_synced_at: null`; the existing owner lifecycle remains responsible for starting Workbench operations.

Expose the same read-only status contract through the native MCP surface and its matching HTTP adapter, using the existing discovery/catalog and parity pattern. The payload is exactly `syncing` and `last_synced_at`. Reuse the existing frontend polling interval. Do not add a watcher service, event stream, scheduler, retry loop, or automatic restart.
