---
atom_id: CA-R-1804@2
content_role: Requirement
current_scope_unit: DISCOVER_TOOLS
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Engineering/Tool Discovery Binding
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-O-112
  - CA-R-1810
type: Rule
---
# Summary

Find Tools by capability

## Scope

the DISCOVER_TOOLS capability for Tool/DISCOVER_TOOLS.

## Claim

the DISCOVER_TOOLS Tool **must** return a ranked, bounded selection of Tools matching the requested capability and filters, with exact source references and observed availability.

## Details

- implement the methodology Action CA-O-112-PROJECT_CONFIGURATION-ACTION--discover-tools.
- accept a query, Scope Unit and availability filters, offset, and result limit; return compact matches, total matches, next offset, catalog fingerprint, and coverage diagnostics.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
