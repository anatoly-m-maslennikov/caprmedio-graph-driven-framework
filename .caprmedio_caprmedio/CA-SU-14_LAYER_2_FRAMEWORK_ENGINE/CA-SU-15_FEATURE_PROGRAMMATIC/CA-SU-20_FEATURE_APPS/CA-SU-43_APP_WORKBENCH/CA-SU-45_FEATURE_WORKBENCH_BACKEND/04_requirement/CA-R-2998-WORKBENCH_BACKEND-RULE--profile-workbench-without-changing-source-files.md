---
atom_id: CA-R-2998
ref_id: CA-R-2998
container:
  scope_unit: CA-SU-45
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Active
version: 1
updated_at: 2026-11-07 03:26:51 +0400
carrier_destination:
  file:
    name: CA-R-2998-WORKBENCH_BACKEND-RULE--profile-workbench-without-changing-source-files.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/04_requirement
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Profile Workbench without changing source files

## Claim

### Prose Claim

An explicitly requested Workbench diagnostic run must report CPU hotspots, Python allocations, process memory and DuckDB-managed memory without changing source files, the live Workbench database or the live MCP process. Profiling is opt-in; ordinary latency, throughput and rebuild acceptance tests run without instrumentation.
