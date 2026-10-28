---
atom_id: CA-D-515
content_role: Delivery
current_scope_unit: GET_EXECUTION_STATUS
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:26 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  depends_on:
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

Encode GET_EXECUTION_STATUS Tool binding

## Scope

the GET_EXECUTION_STATUS capability for Tool/GET_EXECUTION_STATUS/Carrier.

## Claim

the GET_EXECUTION_STATUS Tool binding **must** be carried **in** the following TOML table **in** this Atom's Details, with JSON request **and** response Carriers.

## Details

accept a supported Run ID, optional Action ID and selection ordinal, and whether full saved results are requested; return status, output, results, progress, recording blockers, and report references.

```toml
[tool_binding]
name = "GET_EXECUTION_STATUS"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GET_EXECUTION_STATUS/get_execution_status.py"
action_ids = ["CA-O-115"]
mcp_name = "get_execution_status"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.
