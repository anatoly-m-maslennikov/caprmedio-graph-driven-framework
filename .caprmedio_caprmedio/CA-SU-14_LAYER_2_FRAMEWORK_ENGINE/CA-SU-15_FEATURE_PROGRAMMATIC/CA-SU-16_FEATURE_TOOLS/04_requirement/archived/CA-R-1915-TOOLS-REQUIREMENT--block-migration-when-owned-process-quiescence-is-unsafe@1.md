---
atom_id: CA-R-1915
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Migration quiescence"
  depends_on: [Tool, Runtime, Process, Journal]
relations:
  relates_to: [CA-D-607, CA-E-608]
---
# Summary

Block migration when owned-process quiescence is unsafe

## Scope

the safe shutdown precondition for an owned legacy state switch.

## Claim

the INSTALL_TOOLS facade **must** quiesce **only** a process proved owned by its legacy subtree and generation/command evidence, and **must** block migration when that proof or shutdown result is unsafe.

## Details

Unknown, external, stale, ambiguous or non-responsive processes are never signaled, killed or replaced. Quiescence evidence records the request, response and deadline and is rechecked before copy/switch. A block preserves old state and history without selector mutation.
