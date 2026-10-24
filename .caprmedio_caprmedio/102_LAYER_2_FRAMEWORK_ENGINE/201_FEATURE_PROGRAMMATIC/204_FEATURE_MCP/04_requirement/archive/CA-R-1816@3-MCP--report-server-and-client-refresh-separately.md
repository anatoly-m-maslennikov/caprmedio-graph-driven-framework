---
atom_id: CA-R-1816@3
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: MCP/Tool registry
  depends_on:
  - MCP
  - Tool
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
---
# Summary

Report server and client refresh separately

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP gateway **must** distinguish successful server publication from confirmed client discovery of the published Tool registry.

## Details

- publish changed Tool names, schemas **and** descriptions as one validated registry generation.
- announce a changed registry through the negotiated MCP Tool-list-change notification capability.
- notification delivery does **not** prove that Codex refreshed its cached Tool list.
- report client refresh as unconfirmed unless evidence from that client establishes the current registry.
- clients that do **not** refresh require an explicit reconnect; the gateway **must not** claim to modify the Codex desktop application.
- the initial gateway installation requires a reconnect from the currently running server.

