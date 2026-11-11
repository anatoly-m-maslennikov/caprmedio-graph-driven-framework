---
identity:
  atom_id: CA-E-822
  ref_id: CA-E-822@1-draft
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Query Processing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2728@9-draft
  - CA-M-550@1-draft
  - CA-M-463
  IS_REPLACEMENT_FOR:
  - CA-E-674
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 01:59:26 +0400
destination:
  file:
    name: CA-E-822@1-draft-WORKBENCH_BACKEND-EVAL_CASE--verify-sql-source-updates-and-exclusive-owner-handoff.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/000_draft
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify SQL source updates and exclusive owner handoff

## Claim scope

The public-SQL guard for the file-backed DuckDB Projection.

## Claim

### Prose Claim

Verify the CA-R-2728@9-draft SQL and source-update contract through the shared owner. SELECT uses the Projection; supported UPDATE routes through the source adapter and never directly mutates projected source rows. Preserve exclusive owner handoff and explicit errors; no automatic retry, rollback or recovery.

## Details

Exercise SELECT/CTE/GRAPH_TABLE, multi-statement order and selection, first failure with retained completed effects, rejected unsupported DDL/DML and external access, source refresh and owner handoff. Verify Draft leaves Current unchanged, in-place and existing Draft edits preserve Version/UpdatedAt, new Draft metadata is initialized once by its lifecycle, computed columns reject writes, mixed-script preview writes no sources and later statements see earlier proposed changes; in both modes apply UPDATE followed by SELECT and UPDATE sees each preceding write through synchronized Projection or equivalent source-backed per-run state, with one evolving Draft per target in Draft mode and Current unchanged for outside queries; a subsequent SELECT returns the new value; synchronization failure stops subsequent statements and retains completed writes/results with an explicit error, and both preview and apply report all field changes/results, and find/replace uses the same writer and modes. Verify query_schema exposes issue tables and their actual columns for SQL completion and selection; issue discovery includes malformed/inaccessible source paths without fabricating Atom rows and covers the applicable audit requirements.