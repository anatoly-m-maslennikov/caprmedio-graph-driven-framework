---
atom_id: CA-E-751
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 6
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  evaluation_for:
  - CA-C-701
  - CA-M-463
  - CA-R-2729
carrier_destination:
  file:
    name: CA-E-751-WORKBENCH_BACKEND-EVAL_CASE--verify-first-page-conversion-cleanup.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
updated_at: 2026-11-05 17:43:47 +0400
---

## Summary

Verify query-cache cleanup at the page-conversion boundary.

## Claim

### Prose Claim

If first-page conversion fails after materialization, QueryStore removes the
generated result table and registration before returning the failure, so no
query ID is exposed for the failed result. If a later page conversion fails
after a query ID is known, the query ID and cache remain available for other
page requests.

## Details

| Fixture | Expected outcome |
| --- | --- |
| First-page conversion of `NaN` or infinity | The request fails without a query ID and leaves no generated result table or registration. |
| Later-page conversion with a known query ID | The page request fails, but the known query ID and materialized cache remain available. |
