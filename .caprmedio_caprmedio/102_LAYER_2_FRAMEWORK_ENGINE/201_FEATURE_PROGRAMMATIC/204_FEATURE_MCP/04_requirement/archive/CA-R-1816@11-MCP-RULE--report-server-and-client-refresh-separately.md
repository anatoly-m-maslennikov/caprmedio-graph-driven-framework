---
atom_id: CA-R-1816@11
content_role: Requirement
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
tier: 3
type: Rule
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

