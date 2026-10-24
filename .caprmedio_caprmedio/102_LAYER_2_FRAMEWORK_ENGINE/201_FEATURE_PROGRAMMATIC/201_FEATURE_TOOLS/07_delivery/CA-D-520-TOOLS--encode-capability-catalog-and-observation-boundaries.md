---
atom_id: CA-D-520
content_role: Delivery
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Engineering/Tool//CAPABILITY_CATALOG
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Tool Discovery Binding/Catalog Coverage Diagnostics
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1810
  - CA-M-318
  - CA-M-319
type: Eng Decision
tier: 3
---
# Summary

Encode capability catalog and observation boundaries

## Scope

the TOOLS capability for Capability Catalog/Carrier.

## Claim

the Capability Catalog **must** use the following source, binding **and** result Carrier contract.

## Details

- the Project control root is declared by paths.control_root **in** the Project's settings. its project_structure.toml provides Scope Unit ancestry **and** native bindings.
- source Atoms are explicit active Markdown Carriers under that control root, excluding the delivered APPLICABLE_METHODOLOGY files while retaining its METHODOLOGY_SOURCES descendants.
- a Tool Binding is a fenced TOML table **in** a D Atom's Details containing name, entrypoint, action_ids, optional workflow_ids **and** optional mcp_name. paths are repository-relative.
- compact discovery results contain identity, Summary, Kind, Scope Unit, source binding, implementation availability **and** match evidence. context responses contain exact content **and** incompleteness diagnostics.
- default bounds: 10 search results, **`<=50`** per page, 10,000 source candidates, 8 MiB per file, 256 MiB per scan, 60 seconds per scan, 256 KiB per context, **`<=8`** MiB per context, **`<=30`** seconds per wait. exhausted bounds return incomplete coverage.
- shared Run evidence **and** full reports keep their existing locations. status, result, continuation **and** wait calls create no new Journal **or** second event store.
- the initial observation backend is RMED Atoms Base Revise. its gather, check **and** fix Action results retain their existing Run ID **and** selection ordinal; independent Action Run identity is not invented.
