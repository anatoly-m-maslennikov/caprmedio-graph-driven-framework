---
atom_id: CA-R-1811
content_role: Requirement
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 20:00:03 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
type: Rule
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
