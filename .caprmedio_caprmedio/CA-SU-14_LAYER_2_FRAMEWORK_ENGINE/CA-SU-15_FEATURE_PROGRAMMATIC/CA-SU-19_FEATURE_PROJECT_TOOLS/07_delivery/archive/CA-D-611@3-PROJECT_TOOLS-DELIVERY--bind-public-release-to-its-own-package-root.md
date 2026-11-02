---
atom_id: CA-D-611@3
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: PUBLIC_RELEASE package root
  depends_on:
  - Tool
  - Framework Package
  - Subject/Engineering/Carrier
version: 3
updated_at: 2026-10-23 23:34:06 +0400
relations:
  delivery_for:
  - CA-R-1921
type: Eng Decision
---
# Summary

Bind public release to its own package root

## Scope

the installed-source root of the public-release Tool.

## Claim

the public-release Tool **must** retain `PROJECT_TOOLS/PUBLIC_RELEASE/` as its own installed package-relative root and resolve sibling `RELEASE_VERSION` evidence through the selected installed Framework package.

## Details

The rule does not alter `.caprmedio_install/releases/<digest>/manifest.toml`, `.caprmedio_install/current.toml`, or a Project runtime selection carrier; their owning installation authority remains separate.
