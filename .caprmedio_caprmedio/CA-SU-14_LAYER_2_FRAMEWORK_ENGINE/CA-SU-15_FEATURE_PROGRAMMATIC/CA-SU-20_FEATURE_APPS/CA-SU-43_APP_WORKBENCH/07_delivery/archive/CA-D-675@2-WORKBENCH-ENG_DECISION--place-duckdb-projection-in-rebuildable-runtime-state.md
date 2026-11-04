---
atom_id: CA-D-675
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
  - CA-R-2723
  - CA-R-2728
carrier_destination:
  file:
    name: CA-D-675@2-WORKBENCH-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 00:38:14 +0400
---

## Summary

Place the DuckDB Projection in rebuildable runtime state

## Claim scope

The in-memory placement and authority boundary of the Workbench query Projection.

## Claim

### Prose Claim

The existing application must own the rebuildable DuckDB Projection and Reader Schema Projection in memory. Source files are read directly; no DuckDB database file, derived database path, on-disk schema, cache, or stored intermediate source or materialized data is delivered. The public table surface remains the in-memory `atoms` and `scope_units` tables.

The source files remain the authority. The in-memory Projection is rebuildable and does not edit, move, archive, promote, or replace source Atoms. This Draft does not introduce a hot-swap owner or replacement-generation contract.

Any native read-only mechanism for an in-memory DuckDB connection remains an implementation research item. This Draft makes no promise about file-based read-only configuration.

