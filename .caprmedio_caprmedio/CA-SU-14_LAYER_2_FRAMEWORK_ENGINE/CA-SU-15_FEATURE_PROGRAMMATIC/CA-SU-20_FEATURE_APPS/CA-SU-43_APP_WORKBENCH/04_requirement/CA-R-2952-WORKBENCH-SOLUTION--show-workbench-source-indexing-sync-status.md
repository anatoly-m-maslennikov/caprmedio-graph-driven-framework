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
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: active
  version: 5
  updated_at: '2026-11-12T17:01:18.995441+00:00'
destination:
  file:
    name: CA-R-2952-WORKBENCH-SOLUTION--show-workbench-source-indexing-sync-status.md
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

Expose source-to-DuckDB indexing status, not query execution/autosave: `syncing: true` during initial/refresh capture; `last_synced_at` only after successful reconciliation commits or confirms current committed state; failure preserves prior timestamp/error state; before first success timestamp is null. The shared MCP and HTTP status includes boolean `syncing`, null-or-offset/UTC `last_synced_at`, loaded Archive Scope Unit and Role pairs, and current audit state. Apply the selected Project binding and applicable exclusions.

Read an owner-local snapshot without long lifecycle/query lock, owner start, indexing, SQL or restart, so status remains observable during work. Set syncing before attempt and clear after; unchanged signature may confirm state without a new database write. Uninitialized owner returns false/null. Existing frontend polling renders compact top-right text and local browser time. Add no service, stream, queue, scheduler, retry or automatic restart.
