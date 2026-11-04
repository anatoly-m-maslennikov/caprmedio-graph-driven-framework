---
atom_id: CA-M-462
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
  - CA-R-2728
carrier_destination:
  file:
    name: CA-M-462@1-WORKBENCH-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-03 23:17:14 +0400
---

## Summary

Constrain public DuckDB queries to native read-only access.

## Claim scope

Public SQL access to the DuckDB Projection.

## Claim

### Prose Claim

Public SQL access to the DuckDB Projection must use DuckDB's native read-only connection mode. It must not rely on a SQL keyword check.

Before public SQL is accepted, the owner must disable external access and lock its configuration. Public SQL must not be able to re-enable external file or network access.

These constraints apply together:

- native read-only mode prevents Projection changes, including writes nested in a WITH query;
- disabled external access prevents unrelated file and network access; and
- trusted setup registers only the CAPRMEDIO helpers required by public SQL before the read-only query mode is opened.

Public SQL does not write Atom carriers or the Projection.
