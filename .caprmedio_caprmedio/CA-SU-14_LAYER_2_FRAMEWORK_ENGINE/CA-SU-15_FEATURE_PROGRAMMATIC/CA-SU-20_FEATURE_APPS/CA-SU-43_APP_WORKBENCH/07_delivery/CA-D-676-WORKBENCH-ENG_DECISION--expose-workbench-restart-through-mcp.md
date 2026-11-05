---
atom_id: CA-D-676
ref_id: CA-D-676
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 2
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 5
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2782
updated_at: 2026-11-05 06:00:43 +0400
carrier_destination:
  file:
    name: CA-D-676-WORKBENCH-ENG_DECISION--expose-workbench-restart-through-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery
container:
  scope_unit: CA-SU-43
---

## Summary

Expose Workbench restart through MCP

## Claim scope

The selected Project's Workbench service operation in the existing MCP gateway.

## Claim

Expose the native MCP tool `workbench_restart({})`. It accepts no service name, shell command or container arguments. Close the old Workbench owner before starting its replacement. Return `{service: "workbench", status: "ready"}` only after fresh indexing succeeds. Return the shared explicit `workbench_unavailable` error when startup fails. Serialize restart with that Project's Workbench operations so an in-flight request cannot use a closed owner, including after caller cancellation. MCP and other services stay running. Old query-result IDs become unknown; saved-item IDs remain loadable. Restart itself writes no Business Journal event and adds no retry or rollback.

Health-page controls invoke this same native operation through the gateway. Do not add a second restart implementation, generic service registry, shell execution or Docker control.
