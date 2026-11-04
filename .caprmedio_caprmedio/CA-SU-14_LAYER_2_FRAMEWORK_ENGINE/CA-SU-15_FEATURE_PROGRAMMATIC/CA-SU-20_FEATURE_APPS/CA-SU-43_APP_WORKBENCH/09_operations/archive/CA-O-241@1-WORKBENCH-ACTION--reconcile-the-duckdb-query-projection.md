---
atom_id: CA-O-241
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
author: Anatoly Maslennikov
role: Operations
form: Action
tier: 6
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  depends_on:
  - CA-R-2723
  - CA-R-2725
  - CA-R-2726
  - CA-M-463
  - CA-M-465
  - CA-M-464
  - CA-D-672
  - CA-D-675
carrier_destination:
  file:
    name: CA-O-241@1-WORKBENCH-ACTION--reconcile-the-duckdb-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/09_operations/archive
updated_at: 2026-11-03 23:17:14 +0400
---

## Summary

Reconcile the DuckDB query Projection

## Claim scope

One complete governed Atom-source inventory and its one Project-local derived DuckDB query Projection.

## Claim

Reconcile the DuckDB query Projection **means** the direct technical background-index process that brings one derived query Projection to the latest valid state of its governed sources without changing those sources. It is not a planner, scheduler, orchestrator, query job, ticket, or background query processor.

## Details

1. Use the existing server's one Project owner. Serialize each index update with direct query requests, wait for any read-only query to finish, close every read-only handle, and only then open the trusted read-write handle. On server replacement, the prior owner is closed before its replacement uses the database.
2. On startup and restart, scan the complete governed source inventory before the Projection is available as current. Continue indexing later observed source states by comparing source locators and content fingerprints. Capture changed sources stably; for an invalid, unreadable, or changed-during-capture source, exclude its owned derived rows rather than publishing a mixed or stale read.
3. For every valid canonical carrier, parse its admitted Header and mapped Markdown Content without interpreting prose or Formal Claims. In one database transaction, apply its one `atoms` record, including nested Content Properties and direct Relation facts, and apply a `scope_units` record only when its Current Scope Unit Declaration establishes one; otherwise remove any `scope_units` record that source previously established. These are the only two public tables. For a confirmed missing source, remove those same derived records together; a rename or move updates its locator without inventing a source Version.
4. For an unreadable, invalid, or changed-during-capture source, skip that source, write its path, error, and available location to stderr, and atomically remove any derived records owned by that source. Do not retain stale rows, treat the error as deletion, repair the source, add a diagnostic row to query results, or retry the failed input. Continue with unrelated valid sources. An actual later file edit, move, or new observed source state is a new input.
5. Commit only complete per-source updates. On a synchronization failure, leave the transaction uncommitted, report the technical failure to stderr, and do not expose a partial state or successful result. Write actual indexed, removed, and excluded-source counts to technical stdout; do not write a Journal record. Close the read-write handle before the owner admits another direct public query.
