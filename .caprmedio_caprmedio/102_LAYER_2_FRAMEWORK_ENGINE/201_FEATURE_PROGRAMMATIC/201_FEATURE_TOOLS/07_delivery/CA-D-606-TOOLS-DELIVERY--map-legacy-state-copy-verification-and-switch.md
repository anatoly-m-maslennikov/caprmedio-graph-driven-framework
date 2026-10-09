---
atom_id: CA-D-606
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Legacy migration copy and switch"
  depends_on: [Tool, Runtime, Manifest, Project, Journal]
relations:
  delivery_for: [CA-R-1914, CA-R-1916, CA-M-363]
---
# Summary

Map legacy state copy, verification and switch

## Scope

The loss-avoiding transfer of the three owned legacy subtrees to installation runtime state.

## Claim

the INSTALL_TOOLS facade **must** copy, verify and retain each owned legacy subtree **before** switching the target selector, and **must not** delete legacy state during migration.

## Details

`mapping.toml` has three exact roots: `project_mcp -> runtime/project_mcp`, `mcp_hot_reload -> runtime/mcp_hot_reload`, and `workflow_orchestrator -> runtime/workflow_orchestrator`, all beneath the migration directory. `copy-proof.toml` records source and destination ordered inventory digests, and `switch.toml` records previous selector SHA-256, replacement selector SHA-256, prior N/history references and state generation.

Copy uses staging beneath the migration root, rejects changed inventory rows and verifies byte and mode equality before atomic switch under CA-D-603. The old subtrees remain at their original paths, remain readable for recovery and are named by inventory proof. A partial copy, denied switch or terminal-recording failure retains actual state without claiming migration completion.
