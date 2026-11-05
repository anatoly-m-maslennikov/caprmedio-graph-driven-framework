---
atom_id: CA-O-112
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-11-05 13:04:02 +0400
subjects:
  governs: Subject/caprmedio/Action//Tool discovery
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
carrier_destination:
  file:
    name: CA-O-112-PROJECT_CONFIGURATION-ACTION--find-tools-by-capability.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-112-PROJECT_CONFIGURATION-ACTION--find-tools-by-capability.md
  source_atom_id: CA-O-112
  source_atom_revision: 12
  source_sha256: db5139d2d1071941433a510d17995ce8ebd4400aebdabe43b5c4fe925df62e55
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Find Tools by capability

## Operation

Tool discovery **means** the Programmatic Action implementing the following responsibility:

- for a non-empty request, search declared Tool bindings and observed entrypoints; keep implemented, MCP-exposed, source-only, missing, and unresolved bindings distinct.
- accept the declared inputs **and** return the declared results under CA-D-512-DISCOVER_TOOLS-ENG_DECISION--encode-discover-tools-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.

With an empty request, return the generated released-MCP root catalog under its declared root/groups contract. With a non-empty request, retain the source-binding search and its existing filters and result contract. Reading the catalog grants no execution or mutation authority.
