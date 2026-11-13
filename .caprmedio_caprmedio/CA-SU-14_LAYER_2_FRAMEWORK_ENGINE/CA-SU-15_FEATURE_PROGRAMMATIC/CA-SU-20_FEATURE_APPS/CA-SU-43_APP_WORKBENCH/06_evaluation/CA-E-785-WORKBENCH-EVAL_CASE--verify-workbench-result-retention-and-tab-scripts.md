---
identity:
  atom_id: CA-E-785
  ref_id: CA-E-785
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Storage <+ Temporary State
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2776
  - CA-M-470
  - CA-D-675
state:
  status: active
  version: 5
  updated_at: '2026-11-12T12:34:26.377451+00:00'
destination:
  file:
    name: CA-E-785-WORKBENCH-EVAL_CASE--verify-workbench-result-retention-and-tab-scripts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Verify Workbench result retention and Tab scripts

## Claim scope

The shared Workbench result cache, open-View pinning, runtime TTL setting and whole-query execution as observed through MCP and the web frontend.

## Claim

### Prose Claim

Through real MCP/browser surfaces of one shared backend, verify start-time `.caprmedio_runtime/caprmedio_runtime_settings.toml`: missing is 3,600 seconds; positive `result_ttl_seconds=1` takes effect only after explicit restart/reread; edit alone does not hot reload; invalid `0` fails stderr boundary, never defaults; settings lie outside watcher root and create no change-log event.

Run through one surface and page/inspect through the other to prove one owner/cache. Record monotonic creation: unpinned result is available before TTL and may expire after it through existing idle/Run/Page cleanup. Open View pins beyond TTL; closing unpins while young survives/old may expire—no heartbeat/lease/crash recovery/scheduler/service. Rerun drops old result before replacement; failed replacement does not restore old ID. Restart removes transient tables/IDs while rebuilding Projection and retains saved query/View Journal.

Keep unfinished text editable. Run and Check accept one complete query and reject multiple statements under CA-R-2728. Verify Run & Save stores the exact submitted SQL and Save View stores the complete SQL text. Pass only if real MCP/browser behavior agrees and settings changes alone change neither sources nor watcher log.
