---
identity:
  atom_id: CA-M-549
  ref_id: CA-M-549
context:
  container:
    scope_unit: CA-SU-43
  role: method
  form: decision
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-970308648
  - CA-R-970308649
  - CA-R-970308650
state:
  status: active
  version: 2
  updated_at: '2026-11-12T01:42:24.596360+00:00'
destination:
  file:
    name: CA-M-549-WORKBENCH-DECISION--reuse-canonical-carrier-validation-for-audits.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Reuse canonical carrier validation for audits

## Claim

### Prose Claim

Reuse the existing source reader, locator and canonical carrier validation for the five Workbench audit tables. Audit the same selected Current, Draft and Backlog scan and any loaded Archive sources. Compare duplicate ID and Version pairs only for Current and Archived rows.

Measure audit elapsed time separately from source capture, relation materialization and DuckDB writes. Coalesce audit work for committed source changes and perform it outside the lifecycle response path. Apply the diagnostic changes for the latest affected paths so an older result cannot replace diagnostics for a newer source state. Keep the audit tables query-visible and leave source files unchanged.
