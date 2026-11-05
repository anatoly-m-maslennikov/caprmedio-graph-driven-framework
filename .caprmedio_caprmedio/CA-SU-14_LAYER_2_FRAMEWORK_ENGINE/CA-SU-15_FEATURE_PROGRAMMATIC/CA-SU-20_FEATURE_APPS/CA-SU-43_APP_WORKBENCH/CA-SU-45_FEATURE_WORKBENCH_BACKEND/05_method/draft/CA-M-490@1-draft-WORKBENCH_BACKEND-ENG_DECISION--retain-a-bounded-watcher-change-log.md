---
atom_id: CA-M-490
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Draft
version: 1
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2950
  - CA-R-2724
carrier_destination:
  file:
    name: CA-M-490@1-draft-WORKBENCH_BACKEND-ENG_DECISION--retain-a-bounded-watcher-change-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/draft
updated_at: 2026-11-05 18:19:27 +0400
---
## Summary

Retain a bounded watcher change log

## Claim

### Prose Claim

Use the existing server watcher and its `watchfiles` grouped events as the only input to a technical change log. Watch only the selected repository's CAPRMEDIO source folder. Build no historical backfill: the initial index establishes the baseline, and later grouped observations produce `create`, `update` and `remove` records.

Use a stable technical file identity from the existing observed file state to classify an old/new path pair as `rename` or `move`. Classify only an unambiguous path change; do not match by content or hash, and do not synthesize a rename or move when identity is unavailable. An observation outside the selected source folder is ignored.

Under the existing database-owner lock, write the same event to the owned runtime NDJSON log and the DuckDB `change_log` table. Keep only the event fields defined by the Delivery carrier. This is technical derived state, not a business Journal append and not a source or graph fact.

Before a log read or source refresh, and whenever the existing watcher loop wakes, remove events older than 48 hours from both stores. Enforce one configured retention cap: row-count mode removes the oldest rows after the cap, while megabyte mode removes the oldest rows until the UTF-8 NDJSON file is within the cap; both stores retain the same events. Prefer row-count mode because it bounds event count without encoding-dependent size behavior.

Use an existing watcher timeout or yield only when it already exists to make an idle cleanup check. Do not add a daemon, scheduler, queue, retry loop, recovery procedure, or new Workflow. A storage or write failure follows the existing server error boundary and is not converted into an event row.

