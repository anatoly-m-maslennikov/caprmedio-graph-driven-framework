---
atom_id: CA-R-1804
ref_id: CA-R-1804
container:
  scope_unit: CA-SU-3
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Selection"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 13
updated_at: 2026-11-05 14:23:38 +0400
carrier_destination:
  file:
    name: CA-R-1804-DISCOVER_TOOLS-RULE--find-tools-by-capability.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-3_TOOL_DISCOVER_TOOLS/04_requirement
current_scope_unit: DISCOVER_TOOLS
author: Anatoly Maslennikov
---
# Summary

Find Tools by capability

## Scope

the DISCOVER_TOOLS capability for Tool/DISCOVER_TOOLS.

## Claim

For a non-empty request, the DISCOVER_TOOLS Tool **must** return a ranked, bounded selection of Tools matching the requested capability and filters, with exact source references and observed availability.

## Details

- implement the methodology Action CA-O-112-PROJECT_CONFIGURATION-ACTION--find-tools-by-capability.
- accept a query, Scope Unit and availability filters, offset, and result limit; return compact matches, total matches, next offset, catalog fingerprint, and coverage diagnostics.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.

An empty request returns the generated released-MCP root catalog with root tools, Queries, Views and Service groups and actual MCP descriptors. Non-empty requests retain the ranked, bounded source-binding search with its existing filters and result fields. These are distinct result contracts; do not invent source references for native descriptors.
