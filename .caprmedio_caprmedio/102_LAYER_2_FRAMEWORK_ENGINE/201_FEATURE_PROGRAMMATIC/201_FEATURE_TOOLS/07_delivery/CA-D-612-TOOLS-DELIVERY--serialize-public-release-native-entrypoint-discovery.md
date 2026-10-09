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
version: 1
updated_at: "2026-10-09 17:05:28 +0400"
relations:
  delivery_for: [CA-R-1922]
---
# Summary

Serialize public-release native entrypoint discovery

## Scope

the native description surface of the public-release Tool.

## Claim

the public-release source **must** expose its stable `PUBLIC_RELEASE` description and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PUBLIC_RELEASE/public_release.py` entrypoint while remaining unavailable as an MCP route until an owning registry admits that route.

## Details

The description declares native selected-Workflow binding, not a live network capability.
