---
atom_id: CA-R-2950
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Draft
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2950@1-draft-WORKBENCH-RULE--record-observed-workbench-source-changes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/draft
updated_at: 2026-11-05 18:19:27 +0400
---
## Summary

Record observed Workbench source changes in a bounded technical change log

## Claim

### Prose Claim

The Workbench source watcher must record observed changes from only the selected repository's CAPRMEDIO source folder.

- Consume the existing `watchfiles` grouped file events. Map observed additions, modifications and deletions to `create`, `update` and `remove` records.
- Record `rename` or `move` only when one stable technical file identity is observed at both the old and new paths. A matching hash, name or content alone must never infer a rename or move; without stable identity, retain the observed additions and deletions instead.
- Keep repository-relative `old_path` and `new_path` values. A `create` or `update` has a `new_path`, a `remove` has an `old_path`, and a `rename` or `move` has both. `technical_file_identity` is optional and is required for an inferred rename or move.
- Represent the same retained event set in the technical watcher log file and the read-only DuckDB `change_log` table. Each event has only `observed_at`, `operation`, `old_path`, `new_path` and optional `technical_file_identity` fields.
- Apply a 48-hour time-to-live to both stores. At every cleanup boundary, remove events older than `observed_at < now - 48 hours` before returning them.
- Bound retention with one configured limit mode, either a row count or UTF-8 log-file megabytes, and remove the oldest events from both stores together when the limit is reached.
- Keep this log technical and separate from business Journal history, Atom or Scope Unit source data, and Relation graph facts. Do not add error rows, automatic retries, recovery, a scheduler, or a new watcher service.

