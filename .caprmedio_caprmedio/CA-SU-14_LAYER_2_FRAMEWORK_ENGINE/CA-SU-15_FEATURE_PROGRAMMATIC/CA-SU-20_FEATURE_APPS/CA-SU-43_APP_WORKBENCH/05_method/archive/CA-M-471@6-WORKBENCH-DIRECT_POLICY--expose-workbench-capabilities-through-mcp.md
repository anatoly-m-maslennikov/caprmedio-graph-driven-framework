---
identity:
  atom_id: CA-M-471
  ref_id: CA-M-471@6
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Direct Policy
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Architecture <+ Communication <+ Interface Contracts
  tier: 4
relations:
  method_for:
  - CA-R-2728
  - CA-R-2729
  - CA-R-2776
  - CA-R-2727
state:
  status: Archived
  version: 6
  updated_at: 2026-11-10 00:46:37 +0400
destination:
  file:
    name: CA-M-471@6-WORKBENCH-DIRECT_POLICY--expose-workbench-capabilities-through-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Expose every Workbench backend capability through MCP

## Claim scope

Workbench backend capabilities exposed through MCP.

## Claim

### Prose Claim

Implement each Workbench backend capability once in the shared backend. Expose it through web and MCP adapters with the same arguments, results, errors and saved URLs. Include `query_run(save=true)`, `query_page`, `query_check`, `query_schema`, `view_save`, `query_load` and `query_saved_list`. There is no separate `query_save` or `worksheet_save` capability. Browser-only preferences and local draft state are not backend capabilities and are not exposed through MCP.

Workspace and View coordination is a backend capability and is exposed through MCP with the same state as the embedded interface. Native Codex chat is outside Workbench; Workbench does not duplicate its conversation control.

Result-file export is a shared backend capability available through both interfaces. Use the same explicit `result_delivery` and `result_format` arguments. File delivery is the default; browser grids request inline pages. Omit automatic SQL echoes from execution, validation and result fetch. Explicit SQL reads remain available.
