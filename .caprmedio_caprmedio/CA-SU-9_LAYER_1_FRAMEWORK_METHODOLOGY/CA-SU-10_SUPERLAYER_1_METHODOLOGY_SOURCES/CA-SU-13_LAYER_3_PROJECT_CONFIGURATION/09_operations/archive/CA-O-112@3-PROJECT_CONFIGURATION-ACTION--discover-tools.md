---
atom_id: CA-O-112@3
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Tool discovery
  depends_on:
  - Tool
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Implementation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Journal
relations:
  relates_to:
  - CA-R-1804
  - CA-D-512
---
# Summary

Find Tools by capability

## Operation

Tool discovery **means** the Programmatic Action implementing the following responsibility:

- search declared Tool bindings and observed entrypoints; keep implemented, MCP-exposed, source-only, missing, and unresolved bindings distinct.
- accept the declared inputs **and** return the declared results under CA-D-512-DISCOVER_TOOLS--encode-discover-tools-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
