---
atom_id: CA-C-701
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 1
author: Anatoly Maslennikov
role: Concern
form: Problem
tier: 3
priority: medium
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  concern_about:
  - CA-M-463
  - CA-R-2729
carrier_destination:
  file:
    name: CA-C-701@1-WORKBENCH_BACKEND-PROBLEM--first-page-conversion-failures-retain-unreachable-result-tables.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern/archive
updated_at: 2026-11-05 17:43:47 +0400
ref_id: CA-C-701@1
---

## Summary

First-page conversion failures retain unreachable result tables.

## Concern

When conversion of the first page produced `NaN`, the request failed before a
query ID was returned, but the generated result table remained cached. That
leaked disposable query state for a result the caller could not address.

## Resolution

QueryStore now drops the generated result before propagating a first-page
conversion error. A later page-conversion failure with a known query ID keeps
that cache and ID available for other pages. `tests/test_query_store.py` passes
9 tests, including the `NaN` regression. This resolves the source defect;
runtime adoption and deployment remain separate tracking concerns.
