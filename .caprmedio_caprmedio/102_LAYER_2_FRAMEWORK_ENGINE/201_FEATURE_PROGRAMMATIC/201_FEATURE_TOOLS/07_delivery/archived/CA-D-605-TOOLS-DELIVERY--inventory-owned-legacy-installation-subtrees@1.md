---
atom_id: CA-D-605
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Legacy migration inventory"
  depends_on: [Tool, Runtime, Project, Manifest, Journal]
relations:
  delivery_for: [CA-R-1914, CA-R-1915, CA-M-363]
---
# Summary

Inventory owned legacy installation subtrees

## Scope

The exact owned legacy state eligible for a retained-state migration.

## Claim

the INSTALL_TOOLS facade **must** inventory **only** `.caprmedio_install/project_mcp`, `.caprmedio_install/mcp_hot_reload` and `.caprmedio_install/workflow_orchestrator` before migration, and **must not** infer ownership from adjacent or similarly named state.

## Details

`.caprmedio_runtime/installation/migrations/<migration_id>/inventory.toml` contains schema, target context digest, ordered source-root rows, each relative path, type, SHA-256, mode and owned-process observations. The inventory includes selector and N/history references required to preserve prior runtime provenance, but does not absorb authoring sources, settings, unrelated `.caprmedio_install` members, external processes or arbitrary user files.

Symlinks, special files, path traversal, duplicate roots, changed bytes or unproven owner identity reject before copy. The inventory is re-read after quiescence and before switch; it is retained even for a blocked migration.
