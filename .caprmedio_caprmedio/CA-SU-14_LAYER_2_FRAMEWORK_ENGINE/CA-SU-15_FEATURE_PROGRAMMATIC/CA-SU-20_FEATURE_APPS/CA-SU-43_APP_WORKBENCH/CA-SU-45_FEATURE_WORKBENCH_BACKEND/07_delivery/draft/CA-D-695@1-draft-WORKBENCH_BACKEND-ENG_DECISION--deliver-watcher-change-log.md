---
atom_id: CA-D-695
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Draft
version: 1
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2950
  - CA-R-2724
  - CA-M-490
  - CA-E-780
carrier_destination:
  file:
    name: CA-D-695@1-draft-WORKBENCH_BACKEND-ENG_DECISION--deliver-watcher-change-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery/draft
updated_at: 2026-11-05 18:19:27 +0400
---
## Summary

Deliver the Workbench watcher change log

## Claim

### Prose Claim

Deliver one UTF-8 NDJSON file at `.caprmedio_runtime/workbench/watcher-change-log.ndjson` and one read-only DuckDB `change_log` table. Both are technical derived state owned by the Workbench runtime and contain the same retained event set; neither is a business Journal or a source of Atom, Scope Unit or Relation facts. The table is a separate technical table; Relation expansion continues to use only `atoms` and `scope_units`.

The file and table expose only these event fields:

| Field | DuckDB type | Nullability | Meaning |
| --- | --- | --- | --- |
| `observed_at` | `TIMESTAMPTZ` | NOT NULL | Time at which the watcher observed the event. |
| `operation` | `VARCHAR` | NOT NULL | One of `create`, `update`, `rename`, `move` or `remove`. |
| `old_path` | `VARCHAR` | NULL | Repository-relative selected-source path before the event, when one exists. |
| `new_path` | `VARCHAR` | NULL | Repository-relative selected-source path after the event, when one exists. |
| `technical_file_identity` | `VARCHAR` | NULL | Stable technical file identity used for a `rename` or `move`, when observed. |

For `create` and `update`, `new_path` is present; for `remove`, `old_path` is present; for `rename` and `move`, both paths and the stable identity are present. Do not deliver `error`, source-kind, content-hash, event-id, raw-source, Journal or graph-mapping columns.

The Workbench settings are:

- `ttl_hours`: fixed at `48` for both the file and table.
- `limit_mode`: exactly one of `rows` or `mb`.
- `limit_value`: a positive configured row count or megabyte value for the selected mode; the carrier does not silently choose an unlimited value.
- cleanup: before log reads and source refreshes, plus an existing watcher wake or timeout/yield when available.

When a cap or TTL removes data, remove the oldest events from the file and table together. Do not add a daemon, scheduler, retry or recovery path. Do not report watcher-log failures as source-change events.

