---
identity:
  atom_id: CA-R-2782
  ref_id: CA-R-2782
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 4
state:
  status: Active
  version: 5
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2782-WORKBENCH-SOLUTION--restart-workbench-without-restarting-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-676
  - CA-D-677
---
## Summary

Workbench can restart without restarting MCP

## Claim


### Prose Claim
Allow Operator/AI Agent to restart selected Project Workbench only through native `workbench_restart({})` or explicit health-page action. Restart closes old owner, rebuilds admitted Current/Draft sources and Current Scope Unit Declaration index, clears temporary result IDs, preserves sources/saved queries/Views and leaves MCP/unrelated services/container running. Return ready only after replacement is ready; invalid startup returns shared `workbench_unavailable` and stays unavailable until explicit restart—no retry, rollback or Business Journal event.

`workbench_restart({})` accepts no service/shell/container arguments and serializes with Project work, including cancellation, so no request uses a closed owner. Health GET stays read-only and available on failure; POST `/caprmedio/health/workbench-restart` uses the same gateway, Project selection, blacklist and error boundary. Single Project body is empty; shared host requires exactly one `project_root` field and rejects unknown/repeated fields before effect. Render actual escaped ready/failure; add no picker, shell/Docker/JavaScript/query-editor control. Correcting an invalid Declaration alone does not restart Workbench.
