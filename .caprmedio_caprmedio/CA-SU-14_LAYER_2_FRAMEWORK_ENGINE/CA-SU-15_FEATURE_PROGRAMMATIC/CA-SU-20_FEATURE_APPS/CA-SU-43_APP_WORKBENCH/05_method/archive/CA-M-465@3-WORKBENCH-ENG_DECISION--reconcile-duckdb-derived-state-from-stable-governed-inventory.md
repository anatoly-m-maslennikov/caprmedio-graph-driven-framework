---
atom_id: CA-M-465
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 3
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
    name: CA-M-465@3-WORKBENCH-ENG_DECISION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-04 05:16:33 +0400
---

## Summary

Reconcile DuckDB derived state from a stable governed inventory.

## Claim scope

Technical background indexing of the selected source inventory into the in-memory DuckDB Projection.

## Claim

### Prose Claim

Technical background indexing must reconcile Current and Draft Atom carriers, excluding Archived carriers, into the in-memory DuckDB Projection. Every Current status remains included. It does not prescribe a fingerprint algorithm or a separate event-classification process.

Each indexing batch must publish one complete affected state of source rows, outgoing materialized Relations, row hashes, and the DuckPGQ graph, or publish none of that batch. Queries remain serialized with indexing until graph refresh finishes, so no public query observes old graph mappings with new table rows or a half-batch state. If graph refresh fails, report the failure and do not serve a mismatched graph as current.

An invalid, unreadable, or unstable source capture is excluded with its source-owned Projection rows and all Relation facts and graph mappings supported by it, including derived counterparts carried in other object rows. Refresh those affected rows and hashes, report the source to stderr, and skip it while valid sources continue. It is not treated as deletion, retained as stale data, or automatically resubmitted. A later actual source change is new input.

A failed indexing transaction remains uncommitted, reports the technical failure to stderr, and exposes neither a partial state nor a successful result.
