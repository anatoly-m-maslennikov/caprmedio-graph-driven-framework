---
identity:
  atom_id: CA-R-2998@2
  ref_id: CA-R-2998@2
context:
  container:
    scope_unit: CA-SU-45
  role: Requirement
  form: Rule
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-R-2998@2-WORKBENCH_BACKEND-RULE--profile-workbench-without-changing-source-files.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/04_requirement/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Profile Workbench without changing source files

## Claim

### Prose Claim

An explicitly requested Workbench diagnostic run must report CPU hotspots, Python allocations, process memory and DuckDB-managed memory without changing source files, the live Workbench database or the live MCP process. Profiling is opt-in; ordinary latency, throughput and rebuild acceptance tests run without instrumentation.
