---
atom_id: CA-D-512
content_role: Delivery
current_scope_unit: DISCOVER_TOOLS
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:26 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
type: Eng Decision
tier: 3
---
# Summary

Encode DISCOVER_TOOLS Tool binding

## Scope

the DISCOVER_TOOLS capability for Tool/DISCOVER_TOOLS/Carrier.

## Claim

the DISCOVER_TOOLS Tool binding **must** be carried **in** the following TOML table **in** this Atom's Details, with JSON request **and** response Carriers.

## Details

accept a query, Scope Unit and availability filters, offset, and result limit; return compact matches, total matches, next offset, catalog fingerprint, and coverage diagnostics.

```toml
[tool_binding]
name = "DISCOVER_TOOLS"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/DISCOVER_TOOLS/discover_tools.py"
action_ids = ["CA-O-112"]
mcp_name = "discover_tools"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.
