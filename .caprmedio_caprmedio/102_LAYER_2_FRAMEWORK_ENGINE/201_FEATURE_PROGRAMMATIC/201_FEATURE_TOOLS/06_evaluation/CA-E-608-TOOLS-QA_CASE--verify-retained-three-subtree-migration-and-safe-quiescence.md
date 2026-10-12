---
atom_id: CA-E-608
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Migration acceptance"
  depends_on: [Tool, Runtime, Process, Manifest, Journal]
relations:
  evaluation_for: [CA-R-1914, CA-R-1915, CA-M-363, CA-D-605, CA-D-607]
---
# Summary

Verify retained three-subtree migration and safe quiescence

## Scope

the owned legacy-copy and unsafe-process acceptance matrix.

## Claim

the QA case **must** accept a migration **only** after all three owned subtrees are copied and byte/mode-verified before switch, and **must** block unsafe quiescence without deletion or selector change.

## Details

The success fixture inventories exact roots, proves owned processes through generation/command, copies, verifies, switches and reopens old state and N/history. It injects an adjacent unowned directory, changed row, symlink, process with PID only, external process, timeout and switch interruption; each preserves old state and truthfully reports blocked or partial evidence.
