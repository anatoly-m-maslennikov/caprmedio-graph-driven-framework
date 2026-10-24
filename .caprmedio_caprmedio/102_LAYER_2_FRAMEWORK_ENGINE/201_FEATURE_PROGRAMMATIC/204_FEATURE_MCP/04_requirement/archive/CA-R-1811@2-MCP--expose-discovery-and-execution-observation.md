---
atom_id: CA-R-1811@2
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 03:06:32 +0400
subjects:
  governs: MCP
  depends_on:
  - Tool
  - Action
  - Workflow
  - Subject/Domain/Node/Continuant/Atom
  - Scope Unit
  - Implementation
  - Workflow Run
  - Journal
relations:
  relates_to: [CA-R-1810]
---
# Summary

Expose discovery and execution observation

## Scope

the MCP capability for MCP.

## Claim

the MCP interface **must** expose the declared discovery, context **and** execution-observation Tools with the canonical Implementation's input schemas **and** results.

## Details

- expose discover_tools, discover_operations, get_execution_context, get_execution_status, resume_execution_context **and** watch_execution.
- call the same canonical Tool code used by direct invocation.
- watch_execution provides caller-requested updates through a bounded wait; an idle MCP connection does **not** independently deliver a new chat message.
- report supported Run backends explicitly; unsupported Workflow **or** standalone Action Runs remain explicit rather than fabricated.
