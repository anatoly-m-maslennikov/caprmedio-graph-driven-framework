---
atom_id: CA-C-702
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Resolved
version: 2
author: Anatoly Maslennikov
role: Concern
form: Problem
tier: 3
priority: medium
relations:
  concern_about:
  - CA-M-462
  - CA-M-396
carrier_destination:
  file:
    name: CA-C-702-WORKBENCH_BACKEND-PROBLEM--invalid-sql-and-arguments-are-logged-as-blocking-runtime-failures.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern/021_resolved
updated_at: 2026-11-10 20:47:54 +0400
ref_id: CA-C-702
container:
  scope_unit: CA-SU-45
topics:
  main_subject: MODEL//CAPRMEDIO <+ Projection
---

## Summary

Invalid SQL and arguments are logged as blocking runtime failures.

## Concern

Invalid SQL and invalid query arguments were logged as blocking `ERROR` even
when the Workbench runtime remained healthy. This conflated a failed request
with a failed runtime and obscured whether the owner could continue serving
requests.

## Resolution

`query_error` now uses `WARNING` with outcome `failed`; an actual Workbench
runtime failure remains `ERROR` with outcome `blocked`. The focused
`test_runtime_failure_diagnostics.py` checks pass 9 tests, MCP HTTP checks pass
13, and a native SDK flow succeeds after the failed request. This resolves the
source diagnostic classification; deployment adoption remains separate.
