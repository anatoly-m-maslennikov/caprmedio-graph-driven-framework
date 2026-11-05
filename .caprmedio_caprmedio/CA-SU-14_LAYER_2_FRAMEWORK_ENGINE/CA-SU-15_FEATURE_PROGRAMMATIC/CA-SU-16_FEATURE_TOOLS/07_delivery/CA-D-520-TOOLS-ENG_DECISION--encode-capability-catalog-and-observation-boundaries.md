---
atom_id: CA-D-520
ref_id: CA-D-520
role: Delivery
form: Eng Decision
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-11-02 19:30:12 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-D-520-TOOLS-ENG_DECISION--encode-capability-catalog-and-observation-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery
---
# Summary

Encode capability catalog and observation boundaries

## Scope

the TOOLS capability for Capability Catalog/Carrier.

## Claim

the Capability Catalog **must** use the following source, binding **and** result Carrier contract.

## Details

- the Project control root is declared by paths.control_root **in** the Project's settings. current Scope Unit Declarations provide Scope Unit ancestry **and** native bindings.
- source Atoms are explicit active Markdown Carriers under that control root, excluding the delivered APPLICABLE_METHODOLOGY files while retaining its METHODOLOGY_SOURCES descendants.
- a Tool Binding is a fenced TOML table **in** a D Atom's Details containing name, entrypoint, action_ids, optional workflow_ids **and** optional mcp_name. paths are repository-relative.
- compact discovery results contain identity, Summary, Kind, Scope Unit, source binding, implementation availability **and** match evidence. context responses contain exact content **and** incompleteness diagnostics.
- default bounds: 10 search results, **`<=50`** per page, 10,000 source candidates, 8 MiB per file, 256 MiB per scan, 60 seconds per scan, 256 KiB per context, **`<=8`** MiB per context, **`<=30`** seconds per wait. exhausted bounds return incomplete coverage.
- shared Run evidence **and** full reports keep their existing locations. status, result, continuation **and** wait calls create no new Journal **or** second event store.
- the initial observation backend is RMED Atoms Base Revise. its gather, check **and** fix Action results retain their existing Run ID **and** selection ordinal; independent Action Run identity is not invented.
