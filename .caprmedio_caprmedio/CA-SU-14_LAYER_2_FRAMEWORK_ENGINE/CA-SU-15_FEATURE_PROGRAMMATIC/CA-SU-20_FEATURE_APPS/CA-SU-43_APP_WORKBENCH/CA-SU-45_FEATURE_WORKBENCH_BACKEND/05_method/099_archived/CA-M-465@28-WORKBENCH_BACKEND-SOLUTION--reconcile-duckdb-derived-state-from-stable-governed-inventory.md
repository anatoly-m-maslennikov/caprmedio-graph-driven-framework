---
identity:
  atom_id: CA-M-465
  ref_id: CA-M-465@28
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2723
  - CA-R-2725
  - CA-R-2950
  depends_on:
  - CA-M-509
  IS_REPLACEMENT_FOR:
  - CA-O-241
state:
  status: Archived
  version: 28
  updated_at: '2026-11-12T01:44:23Z'
destination:
  file:
    name: CA-M-465@28-WORKBENCH_BACKEND-SOLUTION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/099_archived
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Reconcile DuckDB derived state from a stable governed inventory.

## Claim

### Prose Claim

Index Current, Draft and Backlog carriers into the file-backed Projection at startup. Resolve explicit Archive load requests through the Scope Unit and Role placement rules. Keep a lightweight Archive filename inventory for lifecycle identity and Version reservations, and parse Archive contents only for selected folders or exact lifecycle files. Update files in the loaded Archive scope on source changes. A role-only unnumbered Draft reference is technically unique only as marker plus Project-relative carrier path. Preserve that ID and numbered Current/Draft identity.

Use the existing server's `watchdog` Observer and selected-repository watcher owner, observing only `control_root`, with grouped native callbacks. Preserve initial build, retained-log reread at owner start/full reread, idle 48-hour cleanup on the same owner thread and Observer shutdown. Under the owner lock, persist events before refresh. Normal batches append/INSERT additions only, retain equal duplicates, and never rewrite retained rows except owner-start/full-reread reconciliation or TTL/cap cleanup. Record directory create/move/remove and refresh the index; ignore directory-modification noise and outside paths, and never infer move from add/delete. A mounted parent does not enlarge the boundary; do not add a watcher service, scheduler, retry or recovery, or failure-as-event-row.

Refresh database and graph under the shared owner lock in one native COMMIT transaction. Queries do not run during refresh. Failed indexing/graph refresh reports stderr and leaves the owner unavailable pending explicit restart: no partial state, candidate swap, rollback or recovery. Unreadable or unparseable ordinary capture is excluded with its supported rows and facts. Keep parseable source rows and report current-schema violations separately. Later actual change is new input. Ambiguous references, relation keys or inverse metadata warn and omit only the affected facts. An invalid Current Scope Unit Declaration stops indexing rather than being skipped. A resource-limit kill is a runtime/capacity failure, not invalid-source evidence.

Retain parsed rows, signatures and owner-local deltas. Ordinary events update only changed public rows, affected inverse neighbours, mappings and hashes in one transaction; unchanged rows preserve object identity and values. Initial indexing, explicit full reread and actual structural/relation-registry/schema changes may rebuild the affected projection, never generic recovery. Publish state only after the database update succeeds. Preserve referenced endpoint contributions until no node or edge supports them; deletion, rename, invalidation, repair and target reappearance must not duplicate facts.

Emit post-COMMIT INFO metrics (operation, table, count/reference, monotonic elapsed and refresh phases) without changing stderr diagnostics or creating Journal events. Case-colliding native relation labels warn and omit colliding projected links while raw source facts remain. Preserve UTF-8 original Markdown and reconstruct heading text transiently; do not retain duplicate decoded bodies or second per-source Header maps.

## Details

### Claim scope

Technical background indexing of the selected source inventory into the file-backed DuckDB Projection.

### Direct indexing inputs and publication

Read YAML and actual Markdown headings directly, using generated declaration assets where admitted. Keep indexed source rows, `atoms`/`scope_units`, relation materialization, hashes and graph publication consistent with the successful transaction. Submit audit work after publishing the source data. `change_log` is technical observation data.
