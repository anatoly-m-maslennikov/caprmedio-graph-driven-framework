---
atom_id: CA-R-1810@9
content_role: Requirement
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool//CAPABILITY_CATALOG
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Tool Discovery Binding/Catalog Coverage Diagnostics
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  relates_to:
  - CA-M-318
  - CA-D-520
tier: 3
type: Rule
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
