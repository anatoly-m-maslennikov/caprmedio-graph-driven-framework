---
atom_id: CA-D-695
ref_id: CA-D-695
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 1
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2950
  - CA-R-2724
  - CA-M-490
  - CA-E-780
carrier_destination:
  file:
    name: CA-D-695-WORKBENCH_BACKEND-ENG_DECISION--deliver-the-workbench-watcher-change-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery
updated_at: 2026-11-05 18:48:47 +0400
container:
  scope_unit: CA-SU-45
---
## Summary

Deliver the Workbench watcher change log

## Claim

### Prose Claim

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

