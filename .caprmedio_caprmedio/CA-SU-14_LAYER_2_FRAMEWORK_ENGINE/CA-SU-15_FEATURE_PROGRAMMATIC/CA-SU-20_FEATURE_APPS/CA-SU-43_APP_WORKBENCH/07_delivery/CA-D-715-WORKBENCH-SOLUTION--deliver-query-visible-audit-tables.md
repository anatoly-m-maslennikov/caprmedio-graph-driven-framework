---
identity:
  atom_id: CA-D-715
  ref_id: CA-D-715
context:
  container:
    scope_unit: CA-SU-43
  role: delivery
  form: solution
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
  status: active
  version: 3
  updated_at: '2026-11-12T01:42:31.971586+00:00'
destination:
  file:
    name: CA-D-715-WORKBENCH-SOLUTION--deliver-query-visible-audit-tables.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Deliver query-visible audit tables

## Claim

### Prose Claim

Deliver these stable SQL tables through the shared Workbench backend and the existing `query_run` and `query_page` interfaces:

- `atom_parse_issues`
- `atom_schema_issues`
- `atom_declared_carrier_issues`
- `atom_physical_carrier_issues`
- `atom_duplicate_revision_issues`

Each table has only these columns: `reference` (nullable), `relative_path`, `filename`, `issue_category`, `property` (nullable), `observed` (nullable), `expected` (nullable), and `diagnostic`. HTTP and MCP must use the same backend and these exact names. Expose these table and column names through query_schema. Existing model-driven Atom Header/Content schema generation and invalid-Declaration handling remain in force. Publish audit rows after source rows commit, and report `audits_pending` and `last_audit_ms` through `workbench_status` and its web equivalent. A pending audit does not prevent queries or lifecycle responses. Audits leave source files unchanged.

