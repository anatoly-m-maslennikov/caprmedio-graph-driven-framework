---
atom_id: CA-D-514@8
content_role: Delivery
current_scope_unit: GET_EXECUTION_CONTEXT
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 17:39:33 +0400
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Engineering/Tool//GET_EXECUTION_CONTEXT
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Programmatic Action/Execution Context Retrieval Adapter
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-O-114
  - CA-R-1806
type: Eng Decision
tier: 3
---
# Summary

Encode GET_EXECUTION_CONTEXT Tool binding

## Scope

the GET_EXECUTION_CONTEXT capability for Tool/GET_EXECUTION_CONTEXT/Carrier.

## Claim

the GET_EXECUTION_CONTEXT Tool binding **must** be carried **in** the following TOML table **in** this Atom's Details, with JSON request **and** response Carriers.

## Details

accept a Tool name or Operations Atom ID and a context budget; return source-bound content, related Workflow Steps and Actions, applicable RMED, implementation and prompt references, and explicit context gaps.

```toml
[tool_binding]
name = "GET_EXECUTION_CONTEXT"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GET_EXECUTION_CONTEXT/get_execution_context.py"
action_ids = ["CA-O-114"]
mcp_name = "get_execution_context"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.
