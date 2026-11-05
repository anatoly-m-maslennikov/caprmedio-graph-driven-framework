---
atom_id: CA-C-555
ref_id: CA-C-555
container:
  scope_unit: CA-SU-21
role: Concern
form: Problem
topics:
  main_subject: Entity/Node/Continuant/Implementation
relations:
  concern_about:
  - CA-R-1811
  - CA-R-2446
status: Active
version: 3
updated_at: 2026-10-30 03:11:57 +0400
carrier_destination:
  file:
    name: CA-C-555-MCP-PROBLEM--diagnose-provider-call-failures-behind-healthy-mcp-gateway.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/01_concern
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
priority: high
---
# Summary

Diagnose provider call failures behind healthy MCP gateway

## Concern

Fresh MCP discovery invocation returns uncertain while the live Gateway and HTTP health remain available. Gateway liveness alone hides the provider-call failure; the exact inner cause is not established.

## Evidences

On 2026-10-21, a connected discover_tools request for MCP health returned outcome uncertain with the fixed diagnostic Implementation call failed; no automatic replay. The read-only get_mcp_reload_status call succeeded for the same serving generation 09a0d6bbcaaa2ebb84db353f2350ed8bfa42fa5fb33c54021be68e4dfd44684c. Bounded live inspection observed the existing localhost container healthy and HTTP /health returning 200 ready true, with initialize/tools-list working. Native current-source catalog inspection completed in about 3.47 seconds. These observations do not prove a timeout or stale image caused the failure; the running image and checkout differ, but inspected committed discovery/provider files are unchanged.

## Blast radius

Discovery and context-based workflows may be unavailable even though transport and the Docker readiness bit pass. P2508 diagnoses without replay; P2509-P2511 provide bounded truthful health visibility and isolated checks. P2512-P2513 perform the expressly authorized normal local release after all gates. A dashboard or new image does not by itself resolve the underlying defect; retain this Problem until actual safe post-adoption evidence establishes the affected read path or the remaining fault is diagnosed.
