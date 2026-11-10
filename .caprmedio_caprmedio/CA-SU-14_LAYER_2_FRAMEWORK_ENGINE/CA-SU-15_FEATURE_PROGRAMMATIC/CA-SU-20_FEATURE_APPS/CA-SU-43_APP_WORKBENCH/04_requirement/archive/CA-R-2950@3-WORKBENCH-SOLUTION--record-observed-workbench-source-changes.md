---
identity:
  atom_id: CA-R-2950
  ref_id: CA-R-2950@3
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-R-2950@3-WORKBENCH-SOLUTION--record-observed-workbench-source-changes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-695
  - CA-M-490
---

## Summary

Record observed Workbench source changes in a bounded technical change log

## Claim

### Prose Claim

The Workbench change log must expose observed changes from only the selected repository's `control_root`.

- Expose `create`, `update`, `rename`, `move` and `remove` operations with repository-relative paths. A `create` or `update` has a `new_path`, a `remove` has an `old_path`, and a `rename` or `move` has both paths.
- A same-parent basename change is `rename`. A parent change is `move`, even when the basename also changes. Preserve the old and new paths reported by the watcher.
- A move into the watched `control_root` is `create`; a move out of it is `remove`; a move with both paths inside it is `rename` or `move` by the path rule above.
- Represent the same retained event set in the technical watcher log file and the read-only DuckDB `change_log` table.
- Apply a 48-hour time-to-live and a fixed 100,000-row cap to both stores. Remove expired or oldest rows from both stores together before returning the log.

## Details

### Change log storage

Deliver one UTF-8 NDJSON file at `.caprmedio_runtime/workbench/watcher-change-log.ndjson` and one read-only DuckDB `change_log` table. Both are technical derived state owned by the Workbench runtime and contain the same retained event set; neither is a business Journal or a source of Atom, Scope Unit or Relation facts. `query_schema` exposes `change_log` as a read-only table; graph mappings continue to use only `atoms` and `scope_units`.

The file and table expose only these event fields:

| Field | DuckDB type | Nullability | Meaning |
| --- | --- | --- | --- |
| `observed_at` | `TIMESTAMPTZ` | NOT NULL | Time at which the watcher observed the event. |
| `operation` | `VARCHAR` | NOT NULL | One of `create`, `update`, `rename`, `move` or `remove`. |
| `old_path` | `VARCHAR` | NULL | Repository-relative selected-source path before the event, when one exists. |
| `new_path` | `VARCHAR` | NULL | Repository-relative selected-source path after the event, when one exists. |

For `create` and `update`, `new_path` is present; for `remove`, `old_path` is present; for `rename` and `move`, both paths are present. A same-parent basename change is `rename`; a parent change is `move`, even when the basename also changes. Do not deliver identity, error, source-kind, content-hash, event-id, raw-source, Journal or graph-mapping columns.

The Workbench settings are:

- `ttl_hours`: fixed at `48` for both the file and table.
- `max_rows`: fixed at `100000` for both the file and table.
- cleanup: the existing owner's event-consumption loop short wait timeout, including while idle on the same owner thread, plus reread at owner start and on a full reread.

When the cap or TTL removes data, remove the oldest events from the file and table together. Do not report watcher-log failures as source-change events.


For a normal event batch without retention removal, append only additions to NDJSON and INSERT only those additions into DuckDB. Preserve duplicate observations. Retained-row replacement is limited to owner-start/full-reread reconciliation and actual TTL/cap cleanup. Keep the four-column public shape unchanged.

### Watcher event capture

Use a `watchdog` `Observer` in the existing server and watch only the selected repository's `control_root`. Group its native callbacks through the existing owner before refresh. `on_created`, `on_modified` and `on_deleted` report their observed operation directly; `on_moved(src_path, dest_path)` reports the old and new paths directly. A same-parent basename change is `rename`; a parent change is `move`, even when the basename also changes. A move into the watched tree is `create`, and a move out is `remove`. Record an observed directory create, move or remove and refresh the index; do not log directory modification noise. Do not pair add/delete events by inode, hash or content. An observation outside the selected repository is ignored.

Under the existing database-owner lock, append new events to the owned runtime NDJSON log and INSERT only those additions into the DuckDB `change_log` table before refreshing source state. Do not rewrite retained rows for a normal batch or deduplicate equal observations. Watcher-log persistence remains synchronous. Reread the retained log at owner start and on a full reread so restart does not discard still-live events. This is technical derived state, not a business Journal append and not a source or graph fact.

Use the existing owner's event-consumption loop short wait timeout to remove events older than 48 hours even when idle on the same owner thread, and retain at most 100,000 rows in both stores by removing the oldest events together. Do not add a separate watcher service, Workflow scheduler, retry loop or recovery procedure. A storage or write failure follows the existing server error boundary and is not converted into an event row.


Compact or replace retained history only for owner-start/full-reread reconciliation or actual TTL/cap removal. Preserve each observation, including equal-field duplicates. Keep the existing per-record 48-hour boundary and 100,000-row cap.
