---
atom_id: CA-D-517@9
content_role: Delivery
current_scope_unit: WATCH_EXECUTION
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool//WATCH_EXECUTION
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Programmatic Action/Execution Notification Adapter
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  relates_to:
  - CA-O-117
  - CA-R-1809
type: Eng Decision
tier: 3
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
