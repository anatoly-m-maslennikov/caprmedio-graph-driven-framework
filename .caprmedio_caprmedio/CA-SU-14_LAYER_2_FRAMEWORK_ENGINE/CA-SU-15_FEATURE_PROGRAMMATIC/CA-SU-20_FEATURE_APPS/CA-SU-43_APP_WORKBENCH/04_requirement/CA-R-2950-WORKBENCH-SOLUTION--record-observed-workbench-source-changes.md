---
identity:
  atom_id: CA-R-2950
  ref_id: CA-R-2950
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Active
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-R-2950-WORKBENCH-SOLUTION--record-observed-workbench-source-changes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
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

