---
identity:
  atom_id: CA-D-679@2
  ref_id: CA-D-679@2
context:
  container:
    scope_unit: CA-SU-43
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  delivery_for:
  - CA-R-2786
  depends_on:
  - CA-D-676
  - CA-D-677
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-D-679@2-WORKBENCH-DECISION--expose-workbench-reread-service.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Expose Workbench full reread through MCP and health

## Claim scope

The selected Project's Workbench service operation in the existing MCP gateway and health page.

## Claim

Expose the native MCP service tool `workbench_reread({})` and a health-page Full reread action through the same Workbench gateway operation. The operation has no generic service name, shell command, container argument or service registry. Add `workbench_reread` to the `Service` group of the generated `discover_tools` catalog. MCP and health use the same Project selection, operation and explicit failure boundary. The health page remains available when Workbench is unavailable. The operation does not restart MCP, another service or the container, and does not write a business Journal event.

## Details

The health action is an explicit POST to `/caprmedio/health/workbench-reread`; GET remains read-only. In shared mode it carries the existing explicit `project_root` form field; the single-Project action accepts no body. It reports success only after the full reread is ready and reports the same failure when source validation or startup fails.
