---
atom_id: CA-D-512
content_role: Delivery
current_scope_unit: DISCOVER_TOOLS
status: Active
author: Anatoly Maslennikov
version: 16
updated_at: 2026-11-05 14:23:38 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations:
  depends_on:
  - CA-D-678
type: Eng Decision
tier: 3
carrier_destination:
  file:
    name: CA-D-512-DISCOVER_TOOLS-ENG_DECISION--encode-discover-tools-tool-binding.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-3_TOOL_DISCOVER_TOOLS/07_delivery
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
entrypoint = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/TOOL_DISCOVER_TOOLS/discover_tools.py"
action_ids = ["CA-O-112"]
mcp_name = "discover_tools"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.

## Root MCP catalog

An empty `request` returns the generated root catalog carried by CA-D-678. It contains `root`, `groups` and `updated_at`, and uses the actual released MCP names, descriptions, schemas and annotations. The root entry is `discover_tools`; groups are Queries, Views and Service. Missing or invalid generated data is an explicit error. The existing explicit query, Scope Unit, availability, offset and limit selectors retain their source-binding search contract. Native descriptors do not acquire invented source paths, SHA-256 bindings or executable status from folder names.
