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
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2950-WORKBENCH-SOLUTION--record-observed-workbench-source-changes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
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

Expose observed changes only inside selected repository `control_root` as repository-relative `create`, `update`, `rename`, `move`, `remove`. Create/update have new path; remove old; rename/move both. Same-parent basename change is rename; parent change is move even with basename change; entering root is create and leaving is remove. Keep the same retained event set in UTF-8 NDJSON `.caprmedio_runtime/workbench/watcher-change-log.ndjson` and read-only DuckDB `change_log`, under 48-hour TTL and 100,000-row cap with oldest/expired rows removed together.

Both stores are technical derived state, not business Journal, Atom/Scope Unit/Relation source or graph fact. `query_schema` exposes only `observed_at`, `operation`, `old_path`, `new_path`; omit identity/error/content/source/Journal/graph fields. Retain equal duplicate events. Record directory create/move/remove and refresh the index, ignore directory-modification noise and outside paths, and never infer move from add/delete. Persist events before refresh; reread the retained log at owner start/full reread. Failures are not event rows.
