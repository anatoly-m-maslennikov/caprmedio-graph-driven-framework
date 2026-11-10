---
identity:
  atom_id: CA-D-715
  ref_id: CA-D-715@1
context:
  container:
    scope_unit: CA-SU-43
  role: Delivery
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  delivery_for:
  - CA-R-970308648
  - CA-R-970308649
  - CA-R-970308650
  - CA-M-549
state:
  status: Archived
  version: 1
  updated_at: 2026-11-11 00:34:40 +0400
destination:
  file:
    name: CA-D-715@1-WORKBENCH-SOLUTION--deliver-query-visible-audit-tables.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Deliver query-visible audit tables

## Claim

### Prose Claim

Deliver these stable SQL tables through the shared Workbench backend and the existing `query_run` and `query_page` interfaces:

- `atom_content_issues`
- `atom_declared_carrier_issues`
- `atom_physical_carrier_issues`

Each table has only these columns: `reference` (nullable), `relative_path`, `filename`, `issue_category`, `property` (nullable), `observed` (nullable), `expected` (nullable), and `diagnostic`. HTTP and MCP must use the same backend and these exact names. Include the tables in the rebuildable schema only when their source declarations are valid. Do not call undeclared columns, add an Action, add background repair, add a second storage authority or change a source automatically.

