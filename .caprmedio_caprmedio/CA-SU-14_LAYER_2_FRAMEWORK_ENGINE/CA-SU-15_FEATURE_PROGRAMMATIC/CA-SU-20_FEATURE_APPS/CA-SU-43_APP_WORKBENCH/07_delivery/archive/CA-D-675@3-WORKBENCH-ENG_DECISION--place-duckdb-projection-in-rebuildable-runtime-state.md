---
atom_id: CA-D-675
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 3
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
    name: CA-D-675@3-WORKBENCH-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 05:16:33 +0400
---

## Summary

Place the DuckDB Projection in rebuildable runtime state

## Claim scope

The in-memory placement and authority boundary of the Workbench query Projection.

## Claim

### Prose Claim

The existing application must own the rebuildable DuckDB Projection and Reader Schema Projection in memory. Source files are read directly; no DuckDB database file, derived database path, on-disk schema, cache, or stored intermediate source or materialized data is delivered. The public table surface remains the in-memory `atoms` and `scope_units` tables.

Deliver a compatible DuckDB and DuckPGQ pair in the WORKBENCH Docker image. Install the extension at image build time. Trusted application startup loads it, enables the required SQL/PGQ grammar for the selected DuckDB version, and creates the in-memory graph before accepting public queries. For DuckDB 2.0, grammar activation uses `active_grammar_extensions = ['duckpgq']`. Startup does not download an extension or require a separate database server.

The source files remain the authority. The in-memory Projection and property graph are rebuildable and do not edit, move, archive, promote, or replace source Atoms. Restart the application after code changes. The selected DuckDB/DuckPGQ pair must pass the indexed Evaluation cases, including native parsing, extension-side-effect rejection, graph refresh, and no spilling. This contract uses no file-based read-only connection switch.

