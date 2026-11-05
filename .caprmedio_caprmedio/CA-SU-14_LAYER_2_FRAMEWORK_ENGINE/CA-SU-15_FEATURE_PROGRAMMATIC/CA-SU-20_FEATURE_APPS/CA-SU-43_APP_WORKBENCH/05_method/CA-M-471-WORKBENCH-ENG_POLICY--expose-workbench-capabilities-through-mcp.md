---
atom_id: CA-M-471
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
role: Method
form: Eng Policy
tier: 4
version: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2728
  - CA-R-2729
  - CA-R-2776
carrier_destination:
  file:
    name: CA-M-471-WORKBENCH-ENG_POLICY--expose-workbench-capabilities-through-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
updated_at: 2026-11-05 16:45:35 +0400
---

## Summary

Expose every Workbench backend capability through MCP

## Claim scope

Workbench backend capabilities exposed through MCP.

## Claim

Expose every Workbench backend capability through MCP with the same arguments, results, errors and saved URLs as the web interface. Include `query_run(save=true)`, `query_page`, `query_check`, `query_schema`, `view_save`, `query_load` and `query_saved_list`. There is no separate `query_save` or `worksheet_save` capability. Browser-only preferences and local draft state are not backend capabilities and are not exposed through MCP.

Workspace and View coordination is a backend capability and is exposed through MCP with the same state as the embedded interface. Native Codex chat is outside Workbench; Workbench does not duplicate its conversation control.
