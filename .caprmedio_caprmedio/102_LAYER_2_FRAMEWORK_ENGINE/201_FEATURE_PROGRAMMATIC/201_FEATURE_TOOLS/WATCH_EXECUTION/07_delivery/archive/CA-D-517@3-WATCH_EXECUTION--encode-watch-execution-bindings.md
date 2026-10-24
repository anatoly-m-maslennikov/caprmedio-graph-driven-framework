---
atom_id: CA-D-517@3
content_role: Delivery
current_scope_unit: WATCH_EXECUTION
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Tool/WATCH_EXECUTION/Carrier
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
  - CA-O-117
  - CA-R-1809
---
# Summary

Encode WATCH_EXECUTION Tool binding

## Scope

the WATCH_EXECUTION capability for Tool/WATCH_EXECUTION/Carrier.

## Claim

the WATCH_EXECUTION Tool binding **must** be carried **in** the following TOML table **in** this Atom's Details, with JSON request **and** response Carriers.

## Details

accept a supported Run ID, opaque cursor and bounded wait timeout; return a new cursor, updates, current status, timeout state, and full report reference.

```toml
[tool_binding]
name = "WATCH_EXECUTION"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WATCH_EXECUTION/watch_execution.py"
action_ids = ["CA-O-117"]
mcp_name = "watch_execution"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.
