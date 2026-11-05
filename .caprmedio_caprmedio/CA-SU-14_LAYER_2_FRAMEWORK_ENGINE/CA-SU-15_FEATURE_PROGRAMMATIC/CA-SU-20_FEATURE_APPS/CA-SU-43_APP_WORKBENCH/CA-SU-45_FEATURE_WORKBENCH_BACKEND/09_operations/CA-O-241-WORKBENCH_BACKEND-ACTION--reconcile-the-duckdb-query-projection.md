---
atom_id: CA-O-241
ref_id: CA-O-241
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 6
author: Anatoly Maslennikov
role: Operations
form: Action
tier: 6
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
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
    name: CA-O-241-WORKBENCH_BACKEND-ACTION--reconcile-the-duckdb-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/09_operations
updated_at: 2026-11-04 17:55:47 +0400
container:
  scope_unit: CA-SU-45
---

## Summary

Reconcile the DuckDB query Projection

## Claim scope

Current and Draft Atom carriers excluding Archived carriers, and their Project-local file-backed DuckDB query Projection.

## Claim

Reconcile the DuckDB query Projection **means** the technical background indexing Action that reads Current and Draft Atom carriers, excluding Archived carriers, into the derived database and updates its Projection without changing source Atoms. Every Current status remains included. It is not a planner, scheduler, orchestrator, query job, ticket, or background query processor.

The Action must:

- parse YAML properties and real Markdown heading paths directly, without a Declaration-to-schema compiler, generic CFEL evaluator, prose interpreter, intermediate JSON file, or third public table;
- derive the current Scope Unit inventory from Current Scope Unit Declarations only; a Draft Declaration remains queryable but does not establish a current Scope Unit;
- store each indexed object's outgoing direct and declared-derived Relations in its own row; source files keep direct Relations only;
- rebuild affected source and counterpart rows, their hashes, and DuckPGQ vertex and edge mappings when a source or relevant Declaration changes;
- refresh the registered property graph before making the new indexed state available to queries;
- refresh the existing file-backed tables and graph under the database-owner lock and finish the successful native write transaction with COMMIT;
- exclude an invalid, unreadable, or unstable source capture with its owned rows and all supported direct and derived graph facts, refresh affected counterpart rows and hashes, write its path, error, and available location to stderr, and continue with unrelated valid sources; and
- emit actual indexed, removed, and excluded-source counts to technical stderr or stdout; reserve stdio MCP stdout for its protocol.

The Action does not retain stale rows for an excluded source, treat a source-file error as deletion, repair a source, return diagnostics as query rows, or automatically resubmit a failed input. A later actual source or relevant Declaration change is new input. A failed index or graph operation writes stderr, returns no partial success, and leaves the owner unavailable until an explicit restart. It does not retry, restore retained rows, swap databases, or perform application rollback. The Action writes no business Journal record.

After a successful refresh, release successful parsed-source caches. Keep existing materialized query results unchanged until the owner closes.
