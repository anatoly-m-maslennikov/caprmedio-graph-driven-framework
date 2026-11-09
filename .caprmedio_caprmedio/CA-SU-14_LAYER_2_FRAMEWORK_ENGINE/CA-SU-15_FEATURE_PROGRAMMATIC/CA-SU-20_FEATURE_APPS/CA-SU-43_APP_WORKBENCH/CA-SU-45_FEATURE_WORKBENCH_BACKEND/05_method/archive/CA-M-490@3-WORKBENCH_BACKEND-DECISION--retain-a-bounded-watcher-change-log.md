---
identity:
  atom_id: CA-M-490@3
  ref_id: CA-M-490@3
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2950
  - CA-R-2724
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-M-490@3-WORKBENCH_BACKEND-DECISION--retain-a-bounded-watcher-change-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Retain a bounded watcher change log

## Claim

### Prose Claim

Use a `watchdog` `Observer` in the existing server and watch only the selected repository's `control_root`. Group its native callbacks through the existing owner before refresh. `on_created`, `on_modified` and `on_deleted` report their observed operation directly; `on_moved(src_path, dest_path)` reports the old and new paths directly. A same-parent basename change is `rename`; a parent change is `move`, even when the basename also changes. A move into the watched tree is `create`, and a move out is `remove`. Record an observed directory create, move or remove and refresh the index; do not log directory modification noise. Do not pair add/delete events by inode, hash or content. An observation outside the selected repository is ignored.

Under the existing database-owner lock, append new events to the owned runtime NDJSON log and INSERT only those additions into the DuckDB `change_log` table before refreshing source state. Do not rewrite retained rows for a normal batch or deduplicate equal observations. Watcher-log persistence remains synchronous. Reread the retained log at owner start and on a full reread so restart does not discard still-live events. This is technical derived state, not a business Journal append and not a source or graph fact.

Use the existing owner's event-consumption loop short wait timeout to remove events older than 48 hours even when idle on the same owner thread, and retain at most 100,000 rows in both stores by removing the oldest events together. Do not add a separate watcher service, Workflow scheduler, retry loop or recovery procedure. A storage or write failure follows the existing server error boundary and is not converted into an event row.


Compact or replace retained history only for owner-start/full-reread reconciliation or actual TTL/cap removal. Preserve each observation, including equal-field duplicates. Keep the existing per-record 48-hour boundary and 100,000-row cap.
