---
atom_id: "CA-D-610"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "PUBLIC_RELEASE native Tool source"
  depends_on: [Tool, Framework Engine, Carrier]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  delivery_for: [CA-R-1920]
---
# Summary

Place the public-release native Tool source

## Scope

the authoritative source carrier for the native public-release Tool.

## Claim

the native public-release Tool **must** be carried at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PUBLIC_RELEASE/public_release.py` with its package-local tests under `PUBLIC_RELEASE/tests/`.

## Details

The carrier is source material for package installation and discovery after the package registry admits it. Its presence alone does not claim an installed launcher or MCP route.
