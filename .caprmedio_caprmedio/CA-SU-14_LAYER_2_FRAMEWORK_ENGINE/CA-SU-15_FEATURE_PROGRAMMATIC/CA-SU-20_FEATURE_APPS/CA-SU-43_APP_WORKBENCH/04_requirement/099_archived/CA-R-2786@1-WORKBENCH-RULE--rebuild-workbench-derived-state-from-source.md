---
atom_id: CA-R-2786
ref_id: CA-R-2786@1
container:
  scope_unit: CA-SU-43
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
status: Archived
version: 1
updated_at: 2026-11-05 13:52:40 +0400
carrier_destination:
  file:
    name: CA-R-2786@1-WORKBENCH-RULE--rebuild-workbench-derived-state-from-source.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Rebuild Workbench derived state from source

## Claim

Workbench can perform a full reread of its governed source files. A full reread drops and recreates the dedicated DuckDB database, its WAL and temporary files, all Workbench schema, graph and query-result tables, and then reads the source again. It preserves source files, saved queries and Worksheets, and does not delete source Journal records. It returns success only after the new Workbench state is ready. An invalid Scope Unit Declaration or startup failure returns an explicit failure and leaves Workbench unavailable until another explicit operation. The operation does not retry automatically.

## Details

Full reread may discard ephemeral query-result IDs because the derived result tables are recreated. It does not delete source Atoms, Scope Unit Declarations, saved items or Journal records.
