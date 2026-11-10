---
identity:
  atom_id: CA-E-781
  ref_id: CA-E-781
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ State Synchronization
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2952
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-781-WORKBENCH-EVAL_CASE--verify-workbench-sync-status.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Verify the Workbench source indexing sync status

## Claim

### Prose Claim

Use built browser/real backend existing HTTP polling. Verify small top-right local-time text distinguishes indexing from query/autosave: initial/refresh poll sees `syncing: true`/Syncing; before success false/null shows Not synced yet; successful commit or confirmed committed state shows false/new offset timestamp; failure preserves prior timestamp/error and does not claim sync/restart. Status remains observable during long indexing. Query/autosave never changes it. Compare HTTP POST and MCP reads: exactly `syncing` and `last_synced_at`, same semantics, no error field/stream/service. Assert visible controls/responses, reuse polling and no automatic restart.
