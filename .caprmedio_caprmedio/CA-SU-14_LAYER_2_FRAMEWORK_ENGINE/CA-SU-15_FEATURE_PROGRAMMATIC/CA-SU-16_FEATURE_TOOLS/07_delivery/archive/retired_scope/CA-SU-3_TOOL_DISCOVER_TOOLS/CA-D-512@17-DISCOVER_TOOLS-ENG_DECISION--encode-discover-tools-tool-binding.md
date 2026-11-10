---
atom_id: CA-D-512
ref_id: CA-D-512
container:
  scope_unit: CA-SU-16
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  depends_on:
  - CA-R-2785
status: Archived
version: 17
updated_at: 2026-11-09 21:15:45 +0400
carrier_destination:
  file:
    name: CA-D-512@17-DISCOVER_TOOLS-ENG_DECISION--encode-discover-tools-tool-binding.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery/archive/retired_scope/CA-SU-3_TOOL_DISCOVER_TOOLS
current_scope_unit: TOOLS
author: Anatoly Maslennikov
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

An empty `request` returns the generated root catalog carried by CA-R-2785. It contains `root`, `groups` and `updated_at`, and uses the actual released MCP names, descriptions, schemas and annotations. The root entry is `discover_tools`; groups are Queries, Views and Service. Missing or invalid generated data is an explicit error. The existing explicit query, Scope Unit, availability, offset and limit selectors retain their source-binding search contract. Native descriptors do not acquire invented source paths, SHA-256 bindings or executable status from folder names.
