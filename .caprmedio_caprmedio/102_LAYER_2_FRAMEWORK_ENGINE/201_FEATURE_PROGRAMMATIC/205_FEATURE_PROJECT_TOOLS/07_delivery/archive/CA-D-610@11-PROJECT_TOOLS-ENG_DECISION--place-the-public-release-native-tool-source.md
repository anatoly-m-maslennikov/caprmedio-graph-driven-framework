---
atom_id: CA-D-610@11
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Storage/Directory Layout
  depends_on:
  - Subject/Graph Node/Engineering/Delivery
  - Subject/Graph Node/Implementation/Code/Tool
  - Subject/Graph Node/Carrier
version: 11
updated_at: 2026-10-27 06:04:45 +0400
relations:
  delivery_for:
  - CA-R-1920
type: Eng Decision
tier: 4
---
# Summary

Place the public-release native Tool source

## Scope

the authoritative source carrier for the native public-release Tool.

## Claim

the native public-release Tool **must** be carried at `PROJECT_TOOLS/PUBLIC_RELEASE/public_release.py` with its package-local tests under `PUBLIC_RELEASE/tests/`.

## Details

The carrier is source material for package installation and discovery after the package registry admits it. Its presence alone does not claim an installed launcher or MCP route.
