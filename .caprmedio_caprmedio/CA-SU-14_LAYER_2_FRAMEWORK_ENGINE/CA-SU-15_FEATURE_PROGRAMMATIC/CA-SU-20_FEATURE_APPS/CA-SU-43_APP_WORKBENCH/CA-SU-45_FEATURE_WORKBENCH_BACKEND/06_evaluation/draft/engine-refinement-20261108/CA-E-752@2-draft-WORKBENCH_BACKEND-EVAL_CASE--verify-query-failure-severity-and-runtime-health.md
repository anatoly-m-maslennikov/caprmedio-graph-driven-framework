---
identity:
  atom_id: CA-E-752
  ref_id: CA-E-752@2-draft
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 6
relations:
  evaluation_for:
  - CA-C-702
  - CA-M-462
  - CA-M-396
state:
  status: Draft
  version: 2
  updated_at: 2026-11-08 20:40:58 +0400
destination:
  file:
    name: CA-E-752@2-draft-WORKBENCH_BACKEND-EVAL_CASE--verify-query-failure-severity-and-runtime-health.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/draft/engine-refinement-20261108
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Verify query-failure severity and runtime availability.

## Claim

### Prose Claim

An invalid SQL statement or invalid query argument is a failed request with a
`query_error` diagnostic at `WARNING` severity and outcome `failed`; the
healthy Workbench owner remains usable. A genuine Workbench-unavailable or
unexpected runtime failure remains `ERROR` with outcome `blocked` and keeps its
restart-required or runtime-failure boundary.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Invalid SQL or query arguments | Return the useful request error, log `query_error` as `WARNING`, mark the outcome `failed`, and keep the owner available. |
| Workbench-unavailable or unexpected runtime failure | Log `ERROR`, mark the outcome `blocked`, and preserve the runtime failure boundary. |
| Valid request after an invalid request | The native MCP/HTTP path continues and the valid request succeeds. |
