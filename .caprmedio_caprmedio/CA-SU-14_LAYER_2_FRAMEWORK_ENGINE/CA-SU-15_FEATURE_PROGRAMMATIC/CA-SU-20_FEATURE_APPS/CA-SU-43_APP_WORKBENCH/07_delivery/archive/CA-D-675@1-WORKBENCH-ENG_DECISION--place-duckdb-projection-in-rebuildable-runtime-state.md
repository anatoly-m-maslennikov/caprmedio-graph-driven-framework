---
atom_id: CA-D-675
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
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
    name: CA-D-675@1-WORKBENCH-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-03 23:17:14 +0400
---

## Summary

Place the DuckDB Projection in rebuildable runtime state

## Claim scope

The delivery boundary and ownership of the per-Project DuckDB Projection state.

## Claim

### Prose Claim

Deliver the rebuildable query database inside the existing Project Docker/runtime boundary. Its concrete path is runtime state, not another governing source or configuration artifact.

The Projection instance identity follows the existing rule when first created and remains the same across rebuilds. Delivery does not allocate a pre-created identity or make the database authoritative. It does not edit, move, archive or promote source Atoms.

Use the existing Docker application's stdout/stderr boundary for technical output. Source-file errors go to stderr, not query-result records.
