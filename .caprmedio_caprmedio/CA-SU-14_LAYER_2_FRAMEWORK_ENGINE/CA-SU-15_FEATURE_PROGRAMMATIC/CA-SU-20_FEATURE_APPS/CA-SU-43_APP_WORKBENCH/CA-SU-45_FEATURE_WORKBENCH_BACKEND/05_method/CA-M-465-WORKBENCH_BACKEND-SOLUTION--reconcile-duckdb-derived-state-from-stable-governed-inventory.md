---
identity:
  atom_id: CA-M-465
  ref_id: CA-M-465
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2723
  - CA-R-2725
  depends_on:
  - CA-M-509
state:
  status: Active
  version: 24
  updated_at: 2026-11-08 20:06:37 +0400
destination:
  file:
    name: CA-M-465-WORKBENCH_BACKEND-SOLUTION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
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

Ambiguous source references, Header relation keys or inverse metadata produce warnings on stderr. Do not choose a winner or repair the model. Exclude duplicate-reference source rows and omit every ambiguous relation or inverse binding from the materialized graph; retain unrelated valid rows, direct facts and unambiguous inverse bindings. Include the ambiguous names and available source paths in the warning. Do not edit authored Relation names, endpoints or directions. Registry-based normalization changes only the query representation of the same unambiguous fact.

A failed indexing transaction reports its error to stderr. The failed owner requires an explicit restart rather than an automatic rollback or recovery procedure.

A container memory-limit kill is a runtime failure, not proof of invalid source data. Inspect the stopped process and its resource budget, correct capacity, and restart explicitly. Do not add automatic restart, source exclusion or query truncation to hide the failure.

Retain successful parsed-source rows and their filesystem signatures in the existing owner for incremental refresh; reparse an ordinary Atom only when its source changes. Remove cached state when its carrier leaves the selected source inventory or becomes invalid. A native ordinary file event batch inserts, updates or removes only changed public rows and graph facts, including affected inverse-relation neighbors and row hashes, in one committed transaction. Do not drop and reinsert every Atom or Scope Unit for an ordinary edit. Reuse the existing relation materializer; comparing its in-memory output is allowed without rebuilding unchanged SQL rows. Initial indexing, explicit full reread, and actual structural or relation-registry changes may rebuild the affected projection/schema. Do not use full rebuild as a generic recovery path for an incremental failure. Existing materialized query results remain stable while the source Projection is refreshed. Database and spill errors follow the same explicit failure boundary; do not hide them through retries or automatic restart.

An invalid Current Scope Unit Declaration stops indexing and makes the owner unavailable. Report the error to stderr and require an explicit Workbench restart after correction. Do not skip the Declaration, serve partial or stale structure, or resume merely because its file changes. An explicit restart closes the old owner and constructs a fresh owner in the existing server; it does not restart MCP or the container.


Write successful source-index database mutation metrics to stdout at INFO: operation, table, affected row count, reference when applicable, and elapsed milliseconds measured with a monotonic timer. The successful INFO refresh event includes total elapsed time and source-capture, materialization and database-write phase durations. These records are enabled by default and need no DEBUG setting. A bulk SQL write reports its measured batch timing. Log writes only after their transaction commits. These metrics do not change stderr source warnings or blocking runtime errors and do not create business Journal events.

When native graph labels cannot distinguish registered Relation names that differ only by case, warn with all colliding names and source paths and omit every colliding type and its projected links. Preserve raw source facts; do not choose a winner, rename a model Relation or invent a graph alias.

For a full source inventory, exclude archive and projection subtrees before expensive per-file checks. Resolve admitted role roots by ancestor membership rather than comparing every file with every Scope Unit. Preserve source and symlink boundaries.


For an ordinary watcher batch, compare only affected raw source rows with their previous values. If no projection source changed, finish the sync without relation materialization, row hashing or database work. Explicit full reread, Scope Unit changes and Content-schema changes still use their existing full path. Equality must preserve value types, including the distinction between a Boolean and a number.

Keep unchanged raw rows immutable within their SourceReader owner. “Same raw row” means the same strongly retained Python object (`is`), not `id()` or value equality. Reuse a prior materialized Atom row and hash only when the same raw row and the same outgoing relation facts are unchanged. Recompute changed rows and inverse-relation neighbours. Remove reused state for deleted, invalid or duplicate-excluded sources. This state is in memory and belongs to one Workbench owner; it is not a new source or stored cache. Publish the next reused state only after the database update succeeds.

Keep the canonical Relation registry in the existing owner, using the compiler under CA-M-509. Reparse only changed registry source contributions for ordinary deltas. Regenerate the derived registry on every supported image rebuild, including local release. An actual registry, alias or inverse-binding change uses the existing full projection boundary. A full capture may compile the registry once; the service must not compile the same captured inventory twice. Preserve current source/graph hashes, inverse relations, schema rebuilding and failure handling.


Expose the affected source paths from an ordinary capture, including removals and invalid exclusions; use an explicit full-capture marker for initial, structural and schema captures. Pass that bounded delta through materialization and database application instead of discovering changes by rebuilding the complete cached graph.

For an ordinary delta, remove old direct facts of affected files and add their new direct facts. Update only changed outgoing owners and affected inverse neighbours. Reuse unrelated rows and facts. Apply only the resulting public-row, edge and reference changes to DuckDB in one transaction. Do not rebuild and compare GraphState over every cached Atom or Scope Unit to discover that delta.

Retain enough owner-local node/edge contribution information to preserve a referenced endpoint when its source node disappears, and remove a reference only when no node or edge still contributes it. Handle deletion, rename, invalidation, repair and target reappearance. Duplicate-reference membership changes may use the existing conservative full boundary. Publish new materialization, schema and graph state only after the database update succeeds; an error keeps the existing explicit unavailable/restart boundary, not a retry or full-rebuild recovery path.

Cached source records must retain the original Markdown and heading spans without storing a second complete section string for every heading. Reconstruct section text when needed. Preserve public parser output, compiled Content values and public row hashes, including legacy Claim handling and original line endings. This changes only the disposable Workbench cache; do not edit source Atoms or drop the caches needed for incremental speed.

Cached source records must also omit duplicate direct Markdown text. Derive direct text from the original body and immediate-child heading spans when a declared Content value needs it; public parser records remain unchanged. Preserve the incremental caches and all Content values/hashes.

Keep only aggregate Header schema counters between refreshes. For an incremental delta, compute contributions from its exact old and new materialized rows, subtract old contributions and add new contributions. Do not retain a second per-source Header contribution map or inspect unchanged Headers. Preserve full-inference parity, normalized-name collision checks, schema transitions and publication only after a successful transaction.

Keep cached original Markdown in UTF-8 bytes rather than widened Python strings. Decode transiently when Content extraction or model-declaration compilation needs text; keep the existing public parser and public values as strings. Preserve original line endings, Content values, relation interpretation, source hashes and public row hashes. Do not retain another complete decoded body. Adopt this representation only after unprofiled correctness, ordinary-edit, bulk and rebuild gates pass; report measured process RAM separately from encoded-byte estimates.

On a full rebuild, derive the public Atom and Scope Unit rows once and reuse those rows for SQL insertion and the retained projection snapshot. Do not repeat Content decoding, extraction or public-row hashing for the second consumer. This reuses the existing full-build result; it is not another retained cache. Publish the new snapshot only after the database transaction succeeds.
