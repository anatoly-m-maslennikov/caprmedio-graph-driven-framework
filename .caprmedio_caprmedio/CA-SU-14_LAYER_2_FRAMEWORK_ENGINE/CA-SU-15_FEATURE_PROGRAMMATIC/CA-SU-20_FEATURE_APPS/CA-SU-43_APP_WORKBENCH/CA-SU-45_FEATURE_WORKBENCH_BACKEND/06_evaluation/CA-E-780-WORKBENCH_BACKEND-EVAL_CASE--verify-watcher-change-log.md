---
atom_id: CA-E-780
ref_id: CA-E-780
container:
  scope_unit: CA-SU-45
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
relations:
  evaluation_for:
  - CA-R-2950
  - CA-R-2724
  - CA-M-490
  - CA-D-695
  - CA-C-704
status: Active
version: 4
updated_at: 2026-11-06 20:37:19 +0400
carrier_destination:
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

With the existing server `watchdog` Observer observing only a selected repository `control_root`, verify that the file and DuckDB table retain the same technical event rows:

| Case | Expected result |
| --- | --- |
| A selected source file is added, modified or deleted | One corresponding `create`, `update` or `remove` record with the appropriate new or old repository-relative path. |
| A native `on_moved(src_path, dest_path)` callback changes the basename in the same parent | One `rename` record with the callback's old and new paths. |
| A native `on_moved(src_path, dest_path)` callback changes the parent | One `move` record with the callback's old and new paths, even when the basename also changes. |
| A native move enters or leaves the watched `control_root` | Entering produces `create` with `new_path`; leaving produces `remove` with `old_path`. |
| A native callback reports a selected directory create, move or remove | Record the observed directory operation and refresh the index; do not record directory modification noise. |
| An add/delete pair occurs without a native move callback | Do not promote the pair to `rename` or `move`. |
| A change occurs outside the selected repository source folder | No change-log row. |
| A grouped watcher batch contains several observations | Preserve each observed operation; do not invent a Workflow or business Journal record. |
| An event reaches 48 hours of age | The existing owner event-consumption loop's short wait timeout, including while idle on the same owner thread, removes it from both the NDJSON file and `change_log`; no stale copy remains queryable after cleanup. |
| The 100,000-row cap is exceeded | Remove the oldest events from both stores until the same retained set has at most 100,000 rows. |
| The owner restarts or performs a full reread | Reread retained log rows, preserve still-live events, and apply the same 48-hour TTL and 100,000-row cap. |
| The watcher is idle | The existing owner event-consumption loop's short wait timeout performs cleanup on the same owner thread; no separate watcher service, Workflow scheduler, retry or recovery path is started. |
| A source or log write fails | Keep the existing error boundary; do not create an `error` event row or Journal entry. |

Run a real Docker end-to-end check on a bind-mounted temporary repository and selected `control_root`. Perform actual file creation, modification, same-parent rename, parent-changing move, and selected-directory move operations while the Observer is running; verify native callback paths, observed directory create/move/remove handling, and matching file/table rows. Keep the owner idle through the event-consumption loop's short wait timeout and verify 48-hour expiry in both stores using the real runtime path. Do not fabricate paired add/delete events or call an internal callback directly.

Verify that `change_log` is not used as an `atoms`/`scope_units` source, graph vertex or Relation fact, and that the delivered columns are limited to `observed_at`, `operation`, `old_path` and `new_path`.

Seed approximately 5,000 actual Atom source files before the Docker watcher starts, assert the indexed workload size, and reuse that one fixture for the existing mutations and latency measurements. Verify a child Atom created inside a newly host-created nested folder becomes query-visible too. For each file mutation exercised by the Docker E2E test, report elapsed milliseconds from immediately before the filesystem operation until a query returns the matching Atom version and path, or confirms its absence after removal. Include the operation and number of observations. Measure create, edit, host and native rename/move, and entry/exit across the watched boundary. Event-log visibility alone is not index visibility.

Report these measurements without adding a speed pass/fail threshold. Keep the existing correctness deadlines. State that the timing includes request and polling overhead; distinguish the small fixture from measurements on the actual repository.
