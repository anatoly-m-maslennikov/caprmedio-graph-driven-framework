---
atom_id: "CA-D-611"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "PUBLIC_RELEASE package root"
  depends_on: [Tool, Framework Package, Carrier]
version: 1
updated_at: "2026-10-09 17:05:28 +0400"
relations:
  delivery_for: [CA-R-1921]
---
# Summary

Bind public release to its own package root

## Scope

the installed-source root of the public-release Tool.

## Claim

the public-release Tool **must** retain `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PUBLIC_RELEASE/` as its own installed package-relative root and resolve sibling `RELEASE_VERSION` evidence through the selected installed Framework package.

## Details

The rule does not alter `.caprmedio_install/releases/<digest>/manifest.toml`, `.caprmedio_install/current.toml`, or a Project runtime selection carrier; their owning installation authority remains separate.
