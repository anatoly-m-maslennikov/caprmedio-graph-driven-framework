---
atom_id: CA-R-1810
ref_id: CA-R-1810
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Transformation"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 12
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1810-TOOLS-RULE--derive-one-current-capability-catalog.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
current_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Derive one current capability catalog

## Scope

the TOOLS capability for Capability Catalog.

## Claim

the Capability Catalog **must** be **`=1`** derived read model shared by Tool discovery, Operations discovery **and** execution-context retrieval.

## Details

- active source Atoms **and** authoritative Project Structure declare capabilities **and** scope ancestry.
- D-owned Tool bindings declare Implementation paths **and** Action bindings; observed files **and** registered MCP handlers establish observed availability.
- declared authority, observed Implementation **and** exposed execution are distinct facts.
- source changes invalidate the derived catalog. duplicate active identifiers, ambiguous bindings, malformed sources **and** bounded reads remain visible.
- the catalog is a Projection; its descriptions do **not** become a separately authored source of truth.
