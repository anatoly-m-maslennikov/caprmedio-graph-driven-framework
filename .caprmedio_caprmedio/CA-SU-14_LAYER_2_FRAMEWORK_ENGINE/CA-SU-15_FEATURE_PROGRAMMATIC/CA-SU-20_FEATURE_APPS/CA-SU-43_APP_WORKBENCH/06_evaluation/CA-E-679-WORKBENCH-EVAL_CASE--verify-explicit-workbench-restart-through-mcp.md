---
identity:
  atom_id: CA-E-679
  ref_id: CA-E-679
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2782
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-679-WORKBENCH-EVAL_CASE--verify-explicit-workbench-restart-through-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Verify explicit Workbench restart through MCP

## Claim

### Prose Claim

Verify explicit MCP restart waits for fresh owner readiness, invalidates old result IDs, preserves sources/saved items and leaves session/unrelated services usable; invalid startup errors without recovery. In one session, Run/save/restart/query: fresh queries work, old Page ID rejects and saved SQL loads. Verify invalid Declaration remains unavailable until corrected then explicitly restarted; in-flight/cancelled work prevents closing its owner; bad arguments reject before effect; source bytes/history/MCP tools remain usable.
