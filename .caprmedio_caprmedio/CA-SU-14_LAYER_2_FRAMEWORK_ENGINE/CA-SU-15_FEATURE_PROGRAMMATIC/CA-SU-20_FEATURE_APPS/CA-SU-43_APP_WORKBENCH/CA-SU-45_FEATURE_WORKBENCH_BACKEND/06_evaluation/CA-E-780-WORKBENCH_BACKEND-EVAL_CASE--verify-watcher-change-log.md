---
identity:
  atom_id: CA-E-780
  ref_id: CA-E-780
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Observability <+ Logging
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 6
relations:
  evaluation_for:
  - CA-R-2950
  - CA-R-2724
  - CA-C-704
state:
  status: Active
  version: 11
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-780-WORKBENCH_BACKEND-EVAL_CASE--verify-watcher-change-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify the Workbench watcher change log

## Claim

### Prose Claim

With the existing `watchdog` Observer limited to the selected repository `control_root`, verify NDJSON and DuckDB `change_log` retain the same technical rows. Native add/modify/delete produces `create`/`update`/`remove`; same-parent move is `rename`, parent-changing move is `move`, and boundary entry/exit is `create`/`remove`. Directory create/move/remove is recorded and indexed, directory-modification noise and outside-root changes are not. Add/delete without a native move callback remains two observations, never inferred rename/move.

Preserve every grouped observation without Workflow/Journal invention. The existing owner loop performs same-thread idle cleanup: rows expire after 48 hours and oldest rows are removed from both stores at 100,000 rows. Restart/full reread rehydrates live rows under the same limits. Failed source/log write follows the existing error boundary, without an error event row, Journal, watcher service, scheduler, retry or recovery.

## Details

Use a real Docker bind-mounted temporary repository and actual creation/edit/rename/move/directory/boundary operations; wait through the owner loop and verify matching callback paths/file/table rows. Prove `change_log` is not an `atoms`/`scope_units` source, graph vertex or Relation fact and exposes only `observed_at`, `operation`, `old_path`, `new_path`.

Seed a deterministic valid 5,000-Atom inventory and use it for E2E mutations and visibility timing. A result is visible only with exact ID, version, path, Header.Container and required direct/derived facts; event-log visibility/counts alone do not pass. Report structured fixture/image/operation/count/elapsed metrics from mutation to query-visible result, with 500-file throughput as 500/elapsed. Hard limits: ordinary mutation <=1.5s; 500 add/update/delete <=15s; 500 move or filename rename (including required carrier metadata) <=30s; combined rename plus Header/content update <=30s. Observation timeout is separate; no variable may raise/disable limits. Distinguish fixture/repository timing and preserve correctness deadlines.
