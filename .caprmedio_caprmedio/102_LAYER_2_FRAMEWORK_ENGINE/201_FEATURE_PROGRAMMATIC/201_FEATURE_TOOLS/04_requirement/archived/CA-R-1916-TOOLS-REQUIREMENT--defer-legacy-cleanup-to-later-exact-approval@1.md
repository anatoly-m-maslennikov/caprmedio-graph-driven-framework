---
atom_id: CA-R-1916
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Legacy cleanup"
  depends_on: [Tool, Operator, Runtime, Manifest, Journal]
relations:
  relates_to: [CA-D-609, CA-E-609]
---
# Summary

Defer legacy cleanup to later exact approval

## Scope

the removal boundary after a completed retained-state migration.

## Claim

the INSTALL_TOOLS facade **must** remove legacy carriers **only** under a later exact Operator-approved inventory, and **must not** remove, move or glob-clean any carrier during installation or migration.

## Details

The cleanup approval binds migration ID, inventory digest, target context, ordered paths and approval digest. Every row and quiescence state is reopened immediately before deletion. Missing or changed approval, state or terminal recording refuses without deletion and preserves migration evidence.
