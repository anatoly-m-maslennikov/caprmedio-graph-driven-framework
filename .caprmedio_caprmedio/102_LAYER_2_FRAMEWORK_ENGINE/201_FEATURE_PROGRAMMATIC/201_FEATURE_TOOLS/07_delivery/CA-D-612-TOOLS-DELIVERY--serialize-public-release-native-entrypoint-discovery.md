---
atom_id: "CA-D-612"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "PUBLIC_RELEASE native entrypoint discovery"
  depends_on: [Tool, Package, Capability Discovery]
version: 2
updated_at: "2026-10-10 12:22:32 +0400"
relations:
  delivery_for: [CA-R-1922]
---
# Summary

Serialize public-release native entrypoint discovery

## Scope

the native description surface of the public-release Tool.

## Claim

the public-release source **must** expose its stable `PUBLIC_RELEASE` description and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PUBLIC_RELEASE/public_release.py` entrypoint. It remains unavailable as an MCP route unless the canonical `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` manifest admits the selected route `public.release` together with CA-D-613's one closed `public_release_source_admissions` record.

## Details

The description declares native selected-Workflow binding, not a direct live network capability. It creates no Atom `tool_binding`, direct capability-discovery contract, standalone MCP adapter, alternate registry, or caller-selected executor. The existing selected-route gateway may expose `public.release` only after that canonical manifest admission; missing, stale, malformed, incomplete, duplicate, or digest-mismatched admission leaves the source unavailable.
