---
atom_id: CA-M-471
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
role: Method
form: Eng Policy
tier: 4
version: 1
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
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Expose every Workbench backend capability through MCP

## Claim scope

Workbench backend capabilities exposed through MCP.

## Claim

Expose every Workbench backend capability through MCP with the same arguments, results, errors and saved URLs as the web interface. Include `query_run`, `query_page`, `query_check`, `query_schema`, `query_save`, `worksheet_save`, `query_load` and `query_saved_list`. Browser-only preferences and local draft state are not backend capabilities and are not exposed through MCP.
