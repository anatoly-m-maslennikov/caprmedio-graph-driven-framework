---
identity:
  atom_id: CA-E-785
  ref_id: CA-E-785@4
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
  status: archived
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-785@4-WORKBENCH-EVAL_CASE--verify-result-retention-and-tab-scripts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/099_archived
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

Leave unfinished edit editable; exercise whole-script and explicit selected-statement Run and Check under CA-R-2728. Verify ordered execution, first failure stops subsequent statements, and completed results and effects remain. Run two SELECT statements followed by a failing statement; fetch each earlier result by its returned query_id, and verify omission selects the last successful Tab result. Verify selected Run & Save stores exactly selected SQL while Save Tab stores the whole script. Pass only if real MCP/browser behavior agrees and settings changes alone change neither sources nor watcher log.
