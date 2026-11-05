---
atom_id: CA-M-465
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 10
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2723
  - CA-R-2725
carrier_destination:
  file:
    name: CA-M-465@10-WORKBENCH_BACKEND-ENG_DECISION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archive
updated_at: 2026-11-04 17:55:47 +0400
---

## Summary

Reconcile DuckDB derived state from a stable governed inventory.

## Claim scope

Technical background indexing of the selected source inventory into the file-backed DuckDB Projection.

## Claim

### Prose Claim

Technical background indexing must reconcile Current and Draft Atom carriers, excluding Archived carriers, into the file-backed DuckDB Projection. Every Current status remains included. It does not prescribe a fingerprint algorithm or a separate event-classification process.

Use `watchfiles` in the existing server to observe source additions, edits, moves and deletions. Watch only the selected repository’s CAPRMEDIO source folder. A larger mounted parent folder does not expand this boundary; ignore everything outside the selected repository. Build the initial index once, then refresh on grouped file-change events instead of scanning on a timer. Stop the watcher when the owner closes. Do not add a separate watcher service, queue or retry loop.

Refresh the existing file-backed database and graph directly under the shared database-owner lock and finish a successful native write transaction with COMMIT. Queries do not run during refresh. If indexing or graph refresh fails, report the error to stderr and stop serving that failed state; do not return partial success, retry the batch, swap candidate databases, restore an old state, or perform application rollback.

An invalid, unreadable, or unstable source capture is excluded with its source-owned Projection rows and all Relation facts and graph mappings supported by it, including derived counterparts carried in other object rows. Refresh those affected rows and hashes, report the source to stderr, and skip it while valid sources continue. It is not treated as deletion, retained as stale data, or automatically resubmitted. A later actual source change is new input.

Ambiguous source references, Header relation keys or inverse metadata produce warnings on stderr. Do not choose a winner or repair the model. Exclude duplicate-reference source rows and omit every ambiguous relation or inverse binding from the materialized graph; retain unrelated valid rows, direct facts and unambiguous inverse bindings. Include the ambiguous names and available source paths in the warning. Keep model Relation names and directions unchanged.

A failed indexing transaction reports its error to stderr. The failed owner requires an explicit restart rather than an automatic rollback or recovery procedure.

A container memory-limit kill is a runtime failure, not proof of invalid source data. Inspect the stopped process and its resource budget, correct capacity, and restart explicitly. Do not add automatic restart, source exclusion or query truncation to hide the failure.

Release successful parsed-source caches after a committed refresh. Existing materialized query results remain stable while the source Projection is refreshed. Database and spill errors follow the same explicit failure boundary; do not hide them through retries or automatic restart.
