---
atom_id: CA-O-112
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 19:59:46 +0400
subjects:
  governs: Subject/caprmedio/Action//Tool discovery
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
---
# Summary

Find Tools by capability

## Operation

Tool discovery **means** the Programmatic Action implementing the following responsibility:

- search declared Tool bindings and observed entrypoints; keep implemented, MCP-exposed, source-only, missing, and unresolved bindings distinct.
- accept the declared inputs **and** return the declared results under CA-D-512-DISCOVER_TOOLS-ENG_DECISION--encode-discover-tools-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
