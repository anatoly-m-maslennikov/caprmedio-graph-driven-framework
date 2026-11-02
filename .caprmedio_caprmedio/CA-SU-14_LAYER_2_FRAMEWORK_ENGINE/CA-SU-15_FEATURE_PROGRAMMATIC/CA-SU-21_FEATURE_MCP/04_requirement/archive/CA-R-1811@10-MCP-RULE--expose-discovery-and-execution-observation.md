---
atom_id: CA-R-1811@10
content_role: Requirement
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/UX/MCP Selected Capability and Workflow Interface
  depends_on:
  - Subject/Graph Node/Engineering/MCP.Execution Observation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1810
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
