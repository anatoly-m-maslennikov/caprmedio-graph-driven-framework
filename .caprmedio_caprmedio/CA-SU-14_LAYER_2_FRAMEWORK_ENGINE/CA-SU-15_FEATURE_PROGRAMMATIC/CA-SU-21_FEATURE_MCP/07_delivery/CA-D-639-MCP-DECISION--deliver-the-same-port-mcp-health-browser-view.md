---
atom_id: CA-D-639
ref_id: CA-D-639
container:
  scope_unit: CA-SU-21
role: Delivery
form: Decision
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status
    Presentation
tier: 5
relations:
  delivery_for:
  - CA-R-2446
status: Active
version: 18
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-D-639-MCP-DECISION--deliver-the-same-port-mcp-health-browser-view.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Deliver the same-port MCP health browser view

## Claim

### Prose Claim

Deliver the health browser view at /caprmedio/health on the same configured loopback-published MCP listener, preserving its machine JSON representation and status semantics. Deliver the implementation and safe fixed error labels with the existing MCP package/image and operational instructions, not as an independent server, frontend build or execution-history authority.

## Details

### Scope

Delivery representation of the bounded health view in the existing MCP HTTP service.

- Keep native implementation in the declared MCP delivery place and existing package/image boundary; add no port, credentials, service lifecycle or Tool registry.
- Explicit text/html renders gateway/registry observations, recent Tool calls and recent Workflow observations with timestamps, outcome/status, separate scheduler/actual Workflow fields and safe error labels. Default/application-json/wildcard preserves ready-boolean JSON and 200/503; Host/Origin rejection is unchanged.
- State process-local since-start and bounded history; absent/unobserved is unknown. Health GET/snapshot dispatches no operations. Only CA-R-2782’s explicit Workbench-restart POST is allowed, through the same native MCP operation; add no replay, reload or mutation control.
- Document the configured existing host port, never a developer-specific port. Normal local release delivers the changed package/image only after complete gates; source pages, snapshots, screenshots or builds are not installed-adoption evidence.
