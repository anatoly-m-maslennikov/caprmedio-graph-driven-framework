---
atom_id: CA-R-1810@4
content_role: Requirement
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Capability Catalog
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
  - CA-M-318
  - CA-D-520
tier: 3
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
