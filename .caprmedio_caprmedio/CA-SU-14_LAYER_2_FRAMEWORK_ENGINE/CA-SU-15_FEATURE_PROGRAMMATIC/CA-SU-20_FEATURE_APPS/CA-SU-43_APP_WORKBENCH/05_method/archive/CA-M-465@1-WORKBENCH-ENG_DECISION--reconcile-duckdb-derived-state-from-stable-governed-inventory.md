---
atom_id: CA-M-465
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
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
    name: CA-M-465@1-WORKBENCH-ENG_DECISION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-03 23:17:14 +0400
---

## Summary

Reconcile DuckDB derived state from a stable governed inventory.

## Claim scope

Synchronization of the DuckDB Projection with governed Atom carriers.

## Claim

### Prose Claim

The DuckDB Projection must reconcile its derived state from the complete governed source inventory on startup and periodically while the server runs. Correctness must not depend on filesystem notifications.

Reconciliation must compare source locators and content fingerprints, and it must use stable captured reads. An invalid, unreadable, or changed-during-capture source is excluded with its owned derived rows, reported to stderr, and skipped while valid sources continue. A capture set must not publish mixed source reads or automatically resubmit the same failed input. A later actual file edit, move, or new observed source state is a new input.

For each source, one database transaction must apply or remove its delivered Projection records and nested values together. Queries therefore observe one committed Projection state.

The derived state must reconcile creates, edits, renames, moves, and confirmed deletions. A move changes the source locator; it does not itself create a source Version. A source-file error does not prove deletion.

A failed database transaction must remain uncommitted, report failure through stderr and to its caller, and expose neither a partial state nor a successful result. It does not automatically start another transaction.
