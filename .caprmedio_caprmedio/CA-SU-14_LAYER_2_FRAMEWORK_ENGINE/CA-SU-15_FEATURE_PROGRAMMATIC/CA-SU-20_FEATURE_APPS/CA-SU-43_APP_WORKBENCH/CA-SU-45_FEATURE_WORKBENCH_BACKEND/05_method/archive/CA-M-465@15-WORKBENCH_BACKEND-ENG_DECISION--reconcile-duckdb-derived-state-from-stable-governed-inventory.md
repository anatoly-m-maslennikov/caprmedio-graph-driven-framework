---
atom_id: CA-M-465
ref_id: CA-M-465
container:
  scope_unit: CA-SU-45
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  method_for:
  - CA-R-2723
  - CA-R-2725
status: Archived
version: 15
updated_at: 2026-11-06 14:57:56 +0400
carrier_destination:
  file:
    name: CA-M-465@15-WORKBENCH_BACKEND-ENG_DECISION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Reconcile DuckDB derived state from a stable governed inventory.

## Claim scope

Technical background indexing of the selected source inventory into the file-backed DuckDB Projection.

## Claim

### Prose Claim

Technical background indexing must reconcile Current and Draft Atom carriers, excluding Archived carriers, into the file-backed DuckDB Projection. Every Current status remains included. Role-only unnumbered Draft IDs such as CA-O-draft are markers shared by multiple Draft carriers; use the marker plus the Project-relative carrier path as their unique technical reference. Do not change their Atom ID, invent a numbered ID or weaken Current identity uniqueness. Numbered Draft and Current references remain canonical. It does not prescribe a fingerprint algorithm or a separate event-classification process.

Use a `watchdog` `Observer` in the existing server's selected-repository watcher owner, watching only that repository's `control_root`. Preserve the existing callback grouping, selected-repository boundary, initial-index build, retained-log reread at owner start and on a full reread, event-consumption loop short wait timeout for 48-hour cleanup even when idle on the same owner thread, and Observer shutdown with the owner. A larger mounted parent folder does not expand this boundary; ignore everything outside the selected repository. Do not add a separate watcher service, Workflow scheduler or retry loop.

Refresh the existing file-backed database and graph directly under the shared database-owner lock and finish a successful native write transaction with COMMIT. Queries do not run during refresh. If indexing or graph refresh fails, report the error to stderr and stop serving that failed state; do not return partial success, retry the batch, swap candidate databases, restore an old state, or perform application rollback.

An invalid, unreadable, or unstable ordinary Atom source capture is excluded with its source-owned Projection rows and all Relation facts and graph mappings supported by it, including derived counterparts carried in other object rows. Refresh those affected rows and hashes, report the source to stderr, and skip it while valid sources continue. It is not treated as deletion, retained as stale data, or automatically resubmitted. A later actual source change is new input.

Ambiguous source references, Header relation keys or inverse metadata produce warnings on stderr. Do not choose a winner or repair the model. Exclude duplicate-reference source rows and omit every ambiguous relation or inverse binding from the materialized graph; retain unrelated valid rows, direct facts and unambiguous inverse bindings. Include the ambiguous names and available source paths in the warning. Keep model Relation names and directions unchanged.

A failed indexing transaction reports its error to stderr. The failed owner requires an explicit restart rather than an automatic rollback or recovery procedure.

A container memory-limit kill is a runtime failure, not proof of invalid source data. Inspect the stopped process and its resource budget, correct capacity, and restart explicitly. Do not add automatic restart, source exclusion or query truncation to hide the failure.

Retain successful parsed-source rows and their filesystem signatures in the existing owner for incremental refresh; reparse an ordinary Atom only when its source changes. Remove cached state when its carrier leaves the selected source inventory or becomes invalid. A native ordinary file event batch inserts, updates or removes only changed public rows and graph facts, including affected inverse-relation neighbors and row hashes, in one committed transaction. Do not drop and reinsert every Atom or Scope Unit for an ordinary edit. Reuse the existing relation materializer; comparing its in-memory output is allowed without rebuilding unchanged SQL rows. Initial indexing, explicit full reread, and actual structural or relation-registry changes may rebuild the affected projection/schema. Do not use full rebuild as a generic recovery path for an incremental failure. Existing materialized query results remain stable while the source Projection is refreshed. Database and spill errors follow the same explicit failure boundary; do not hide them through retries or automatic restart.

An invalid Current Scope Unit Declaration stops indexing and makes the owner unavailable. Report the error to stderr and require an explicit Workbench restart after correction. Do not skip the Declaration, serve partial or stale structure, or resume merely because its file changes. An explicit restart closes the old owner and constructs a fresh owner in the existing server; it does not restart MCP or the container.


Write successful source-index database mutation metrics to stdout at INFO: operation, table, affected row count, reference when applicable, and elapsed milliseconds measured with a monotonic timer. Log successful total refresh time at INFO too. Emit these normal-success records without enabling DEBUG. A bulk SQL write reports its measured batch timing. Log writes only after their transaction commits. With DEBUG enabled, add source-capture, materialization and database-write phase durations. These metrics do not change stderr source warnings or blocking runtime errors and do not create business Journal events.
