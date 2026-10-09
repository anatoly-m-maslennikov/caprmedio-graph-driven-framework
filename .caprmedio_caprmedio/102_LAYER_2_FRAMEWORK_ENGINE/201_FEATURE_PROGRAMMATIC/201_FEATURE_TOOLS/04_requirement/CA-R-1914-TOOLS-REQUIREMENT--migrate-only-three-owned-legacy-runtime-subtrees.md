---
atom_id: CA-R-1914
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Legacy state migration"
  depends_on: [Tool, Runtime, Project, Manifest, Journal]
relations:
  relates_to: [CA-D-605, CA-D-606, CA-E-608]
---
# Summary

Migrate only three owned legacy runtime subtrees

## Scope

the retained-state migration boundary for installation-owned legacy state.

## Claim

the INSTALL_TOOLS facade **must** migrate **only** `.caprmedio_install/project_mcp`, `.caprmedio_install/mcp_hot_reload` and `.caprmedio_install/workflow_orchestrator` by copy, verification and switch, and **must not** infer other state as owned.

## Details

An ordered inventory freezes paths, types, modes, digests and owned-process observations before copy. The migration verifies copied bytes and modes, switches only after revalidation under the installation lock, and retains the old subtrees and N/history. Any unsafe source or switch interruption remains a blocked or partial retained result.
