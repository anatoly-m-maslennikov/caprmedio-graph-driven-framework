---
atom_id: CA-D-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 2
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2724
  - CA-R-2728
  - CA-R-2729
carrier_destination:
  file:
    name: CA-D-673@2-WORKBENCH-ENG_DECISION--deliver-shared-query-run-and-check-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 00:38:14 +0400
---

## Summary

Deliver shared query Run and Check results

## Claim scope

The synchronous native SQL connector, MCP Run and Check operations, and their shared Web representation.

## Claim

### Prose Claim

MCP and web Run and Check requests must invoke one shared native SQL connector directly and synchronously. They add no planner, scheduler, Workflow, queue, job, or second executor. The connector follows native DuckDB SQL semantics and adds no custom SQL-like or CFEL query parser.

The connector must provide the native SQL helper `expand(seed, relations, seed_kind := NULL)`. `seed` is a reference string; `relations` selects registered Relation Types; and `seed_kind` defaults to null and accepts only the supported Atom or Scope Unit kind values. The helper returns typed `kind` and `ref` references, not fetched objects or relation records. It reads the materialized nested relation facts from the in-memory rows, follows selected directions once, and does not synthesize a second inverse or a public relation table.

Run must return the complete query result, column names and types, row count, and column count. Check must return validity and exact row and column counts, or the query error. Query errors are returned to the caller, never as an empty successful result. Neither operation silently adds a limit or truncates rows; if a transport cannot carry a complete result, it reports that limitation explicitly. Source-file errors remain a separate stderr channel with source path, error, and available line or column.

Run and Check do not modify source files or the in-memory Projection. The web page presents ordinary rows through this connector and does not define a second result format, renderer, or custom result view.

Projection row hashes belong to the indexed `atoms` and `scope_units` rows; Run and Check do not automatically hash arbitrary SQL result rows.

