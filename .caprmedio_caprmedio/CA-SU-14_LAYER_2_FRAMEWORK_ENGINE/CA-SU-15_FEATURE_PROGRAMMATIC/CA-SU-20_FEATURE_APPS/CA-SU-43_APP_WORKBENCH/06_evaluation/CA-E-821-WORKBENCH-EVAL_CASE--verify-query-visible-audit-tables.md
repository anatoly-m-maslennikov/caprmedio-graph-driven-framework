---
identity:
  atom_id: CA-E-821
  ref_id: CA-E-821
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 6
relations:
  evaluation_for:
  - CA-R-970308648
  - CA-R-970308649
  - CA-R-970308650
  - CA-M-549
  - CA-D-715
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 00:34:40 +0400
destination:
  file:
    name: CA-E-821-WORKBENCH-EVAL_CASE--verify-query-visible-audit-tables.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Verify query-visible audit tables

## Claim

### Prose Claim

Using the real Workbench backend and both query interfaces, verify that:

- each of the three audit cases has positive and negative examples for both Current and Draft sources;
- readable Current and Draft Atoms with no issue produce no audit row;
- each inaccessible source produces `issue_category = query_inaccessible_atom`, each declared carrier conflict produces `issue_category = declared_carrier_inconsistency`, and each physical carrier mismatch produces `issue_category = physical_carrier_mismatch`, with source identity or path, diagnostic and observed or expected values in the appropriate columns;
- an invalid or unreadable source is reported without a normal Atom row, valid sources remain queryable, and source files remain unchanged;
- `query_run` and `query_page` return the same audit rows through HTTP and MCP.

