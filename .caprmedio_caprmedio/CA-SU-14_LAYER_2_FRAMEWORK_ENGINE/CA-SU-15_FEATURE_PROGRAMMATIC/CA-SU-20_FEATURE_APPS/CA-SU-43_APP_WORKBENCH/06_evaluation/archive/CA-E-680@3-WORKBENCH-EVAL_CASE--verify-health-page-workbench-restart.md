---
identity:
  atom_id: CA-E-680
  ref_id: CA-E-680@3
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2782
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-E-680@3-WORKBENCH-EVAL_CASE--verify-health-page-workbench-restart.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Verify health-page Workbench restart

## Claim

### Prose Claim

The health page's Restart Workbench button invokes the same native MCP operation and shows the actual success or failure. The page remains available when Workbench fails. Opening the page is read-only; no restart occurs before the explicit POST action.

## Details

| Scenario | Expected outcome |
| --- | --- |
| GET HTML health page and machine JSON readiness | Restart button is present in HTML; no service operation runs. Existing JSON readiness is unchanged. |
| Submit the fixed restart form for the Project | Health HTML shows the actual ready result; fresh queries work; old result IDs are unknown and saved items remain loadable. |
| Restart with a still-invalid Current Scope Unit Declaration | Health page shows failure; MCP and the health page remain usable. |
| Shared host action | It requires an explicit Project folder and restarts only the selected Project. |
| Missing, repeated or unknown form fields | Rejected before any restart effect. |
| Tool is blacklisted | The health action reports the blocked operation and does not bypass the native MCP blacklist. |
