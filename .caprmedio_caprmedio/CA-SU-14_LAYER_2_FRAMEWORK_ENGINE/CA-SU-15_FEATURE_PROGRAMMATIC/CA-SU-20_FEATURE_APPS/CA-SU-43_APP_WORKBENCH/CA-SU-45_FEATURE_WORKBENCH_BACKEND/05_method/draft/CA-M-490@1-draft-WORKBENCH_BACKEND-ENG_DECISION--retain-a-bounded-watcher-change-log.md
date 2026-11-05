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

Use a `watchdog` `Observer` in the existing server and watch only the selected repository's `control_root`. Group its native callbacks through the existing owner before refresh. `on_created`, `on_modified` and `on_deleted` report their observed operation directly; `on_moved(src_path, dest_path)` reports the old and new paths directly. A same-parent basename change is `rename`; a parent change is `move`, even when the basename also changes. Do not pair add/delete events by inode, hash or content. An observation outside the selected repository is ignored.

Under the existing database-owner lock, write the same event to the owned runtime NDJSON log and the DuckDB `change_log` table. Reread the retained log at owner start and on a full reread so restart does not discard still-live events. This is technical derived state, not a business Journal append and not a source or graph fact.

Use the existing owner timeout to remove events older than 48 hours while idle, and retain at most 100,000 rows in both stores by removing the oldest events together. Do not add a daemon, scheduler, queue, retry loop, recovery procedure or new Workflow. A storage or write failure follows the existing server error boundary and is not converted into an event row.

