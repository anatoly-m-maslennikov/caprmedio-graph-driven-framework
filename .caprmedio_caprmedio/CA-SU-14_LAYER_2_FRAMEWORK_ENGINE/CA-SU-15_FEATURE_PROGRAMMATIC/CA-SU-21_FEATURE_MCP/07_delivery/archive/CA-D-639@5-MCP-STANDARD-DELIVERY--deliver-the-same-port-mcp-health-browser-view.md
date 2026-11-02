---
atom_id: CA-D-639@5
content_role: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Subject/Engineering/Carrier
  depends_on: []
relations:
  delivery_for:
  - CA-R-2007
type: Eng Decision
tier: 5
---
# Summary

Deliver the same-port MCP health browser view

## Scope

Delivery representation of the bounded health view in the existing MCP HTTP service.

## Claim

Deliver the health browser view at /health on the same configured loopback-published MCP listener, preserving its machine JSON representation and status semantics. Deliver the implementation and safe fixed error labels with the existing MCP package/image and operational instructions, not as an independent server, frontend build or execution-history authority.

## Details

- Native implementation remains in the declared MCP delivery place and is included by the existing package/image boundary. Do not create another port, credentials, service lifecycle or Tool registry for the page.
- Explicit text/html negotiation renders gateway/registry observations, recent Tool calls and recent Workflow observations with timestamps, outcome/status, separate scheduler/actual Workflow fields, and safe error labels. Default/application-json/wildcard machine use retains the existing ready boolean JSON and 200/503 behavior. Host/Origin rejection is unchanged.
- Include a visible process-local since-start and bounded-history statement; absent or unobserved data is unknown. Provide no controls that dispatch, replay, reload or mutate. Do not include payloads, provider exception text, secrets or internal absolute paths.
- The documented browser URL uses the configured existing host port; never hard-code one developer's current port as framework authority. The normal local-release path delivers the changed package/image only after its complete gates. A source page, health snapshot, screenshot or successful package build is not installed adoption evidence.
