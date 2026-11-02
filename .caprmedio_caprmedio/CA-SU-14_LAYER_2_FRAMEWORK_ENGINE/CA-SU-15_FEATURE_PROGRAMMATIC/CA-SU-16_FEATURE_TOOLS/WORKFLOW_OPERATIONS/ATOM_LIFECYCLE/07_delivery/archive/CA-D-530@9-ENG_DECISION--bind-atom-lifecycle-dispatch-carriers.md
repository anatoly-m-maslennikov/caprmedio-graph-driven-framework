---
atom_id: CA-D-530@9
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Atom Lifecycle/Dispatch Carrier Topology
  depends_on:
  - Subject/Graph Node/Engineering/Atom Lifecycle
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations:
  delivery_for:
  - CA-R-1825
  - CA-R-1826
  - CA-R-1827
  - CA-R-1828
type: Eng Decision
tier: 4
---
# Summary

Bind Atom lifecycle dispatch carriers

## Scope

The authority-relative `WORKFLOW_OPERATIONS/ATOM_LIFECYCLE` RMED packet.

## Claim

The packet delivers its Requirements in `04_requirement`, golden QA Cases in `06_evaluation`, and delivery contracts in `07_delivery`; it composes existing native lifecycle Tool Carriers rather than replacing them.

## Details

`ATOM_LIFECYCLE` is a bounded authority path below registered `TOOLS`, not a declared Scope Unit.
