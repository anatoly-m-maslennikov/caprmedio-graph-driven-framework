---
atom_id: CA-D-515
ref_id: CA-D-515
container:
  scope_unit: CA-SU-6
role: Delivery
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 14
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-515-GET_EXECUTION_STATUS-ENG_DECISION--encode-get-execution-status-tool-binding.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-6_TOOL_GET_EXECUTION_STATUS/07_delivery
current_scope_unit: GET_EXECUTION_STATUS
author: Anatoly Maslennikov
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
entrypoint = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/TOOL_GET_EXECUTION_STATUS/get_execution_status.py"
action_ids = ["CA-O-115"]
mcp_name = "get_execution_status"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.
