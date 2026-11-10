---
identity:
  atom_id: CA-E-787
  ref_id: CA-E-787
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
  tier: 5
relations:
  evaluation_for:
  - CA-R-2903
state:
  status: Active
  version: 6
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-787-WORKBENCH_BACKEND-EVAL_CASE--verify-hourly-query-log-retention.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify hourly query-log retention

## Claim

### Prose Claim

Use the real backend to verify adjacent UTC hours append NDJSON to their respective `query-log-YYYY-MM-DD-HH.ndjson` files; every retained record has exactly `log_id`, `at`, `sql`, `outcome`, `error`, `row_count`, `column_count`. Records younger than 48 hours remain listable/gettable; those at or beyond 48 hours disappear during append/list/get retention.

Legacy `query-log.json` remains byte-identical and listable/gettable beside hourly records; no new record is appended, migrated or backfilled there. Successful/failed Run submits once to an ordered background writer after synchronous Save; Check submits none and Run returns without waiting. Writer failure reports stderr without retry/warning and preserves completed result. Expiry does not alter saved Views/Journal, watcher log or result cache. Verify backend/MCP rollover and legacy cases; orderly shutdown drains submitted history, while crash may lose unflushed history but not sources/saved items.
