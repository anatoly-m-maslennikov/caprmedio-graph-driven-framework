---
atom_id: CA-E-753
ref_id: CA-E-753
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 6
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
relations:
  evaluation_for:
  - CA-C-703
  - CA-R-2728
  - CA-M-462
  - CA-D-673
carrier_destination:
  file:
    name: CA-E-753-WORKBENCH_BACKEND-EVAL_CASE--verify-the-deployed-mcp-workbench-query-schema.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
updated_at: 2026-11-05 17:43:47 +0400
container:
  scope_unit: CA-SU-45
---

## Summary

Verify the deployed MCP Workbench query schema.

## Claim

### Prose Claim

The deployed MCP query operation advertises the shared Workbench query
contract: `sql` is required, and `preview` and `save` are accepted optional
arguments with their native types. A native MCP SDK client can send
`preview: 0` and `save: false` through the deployed endpoint without schema
rejection, while the shared query result and saved-resource behavior remain
consistent.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Deployed MCP tool schema | The advertised schema includes optional `preview` as a non-negative integer and `save` as a boolean, without rejecting either property. |
| Native SDK request with `preview: 0` and `save: false` | The request reaches the Workbench query operation and returns the expected zero-row preview without creating a saved query. |
