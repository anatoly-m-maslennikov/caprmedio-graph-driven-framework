---
atom_id: CA-E-780
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Draft
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 5
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  evaluation_for:
  - CA-R-2950
  - CA-R-2724
  - CA-M-490
  - CA-D-695
carrier_destination:
  file:
    name: CA-E-780@1-draft-WORKBENCH_BACKEND-EVAL_CASE--verify-watcher-change-log.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/draft
updated_at: 2026-11-05 18:19:27 +0400
---
## Summary

Verify the Workbench watcher change log

## Claim

### Prose Claim

With the existing server watcher observing only a selected repository source folder, verify that the file and DuckDB table retain the same technical event rows:

| Case | Expected result |
| --- | --- |
| A selected source file is added, modified or deleted | One corresponding `create`, `update` or `remove` record with the appropriate new or old repository-relative path. |
| The same stable technical file identity is observed under a new name in the same parent | One `rename` record with both paths and the identity. |
| The same stable technical file identity is observed under a different parent with the same name | One `move` record with both paths and the identity. |
| A path changes in a way that is not unambiguous, or only matching content/hash is available | Do not infer `rename` or `move`; retain only the underlying observed add/remove events. |
| A change occurs outside the selected repository source folder | No change-log row. |
| A grouped watcher batch contains several observations | Preserve each observed operation; do not invent a Workflow or business Journal record. |
| An event reaches 48 hours of age before a cleanup boundary | Remove it from both the NDJSON file and `change_log`; no stale copy remains queryable after cleanup. |
| The configured row or megabyte cap is exceeded | Remove the oldest events from both stores until the selected cap is satisfied, preserving the same retained set. |
| The watcher is idle | Use only an existing wake, timeout/yield, log read or source refresh for cleanup; do not start a new daemon, scheduler, retry or recovery path. |
| A source or log write fails | Keep the existing error boundary; do not create an `error` event row or Journal entry. |

Verify that `change_log` is not used as an `atoms`/`scope_units` source, graph vertex or Relation fact, and that the delivered columns are limited to `observed_at`, `operation`, `old_path`, `new_path` and optional `technical_file_identity`.

