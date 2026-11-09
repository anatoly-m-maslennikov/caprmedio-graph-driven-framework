---
atom_id: CA-D-639@16
ref_id: CA-D-639@16
container:
  scope_unit: CA-SU-21
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation
tier: 5
relations:
  delivery_for:
  - CA-R-2446
  depends_on:
  - CA-D-677
status: Archived
version: 16
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-639@16-MCP-DECISION--deliver-the-same-port-mcp-health-browser-view.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/archive
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

- Native implementation remains in the declared MCP delivery place and is included by the existing package/image boundary. Do not create another port, credentials, service lifecycle or Tool registry for the page.
- Explicit text/html negotiation renders gateway/registry observations, recent Tool calls and recent Workflow observations with timestamps, outcome/status, separate scheduler/actual Workflow fields, and safe error labels. Default/application-json/wildcard machine use retains the existing ready boolean JSON and 200/503 behavior. Host/Origin rejection is unchanged.
- Include a visible process-local since-start and bounded-history statement; absent or unobserved data is unknown. Health GET and snapshot rendering dispatch no operations. The explicit Workbench restart POST control defined by CA-D-677 is permitted; it calls the same native MCP operation. Do not add other dispatch, replay, reload or mutation controls. Do not include payloads, provider exception text, secrets or internal absolute paths.
- The documented browser URL uses the configured existing host port; never hard-code one developer's current port as framework authority. The normal local-release path delivers the changed package/image only after its complete gates. A source page, health snapshot, screenshot or successful package build is not installed adoption evidence.
