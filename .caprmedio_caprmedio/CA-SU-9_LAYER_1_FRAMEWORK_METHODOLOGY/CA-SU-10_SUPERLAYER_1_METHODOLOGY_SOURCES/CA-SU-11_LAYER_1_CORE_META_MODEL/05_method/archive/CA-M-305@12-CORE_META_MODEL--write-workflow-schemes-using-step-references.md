---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph/Relation/Type: On Result'
version: 12
updated_at: 2026-10-24 01:37:42 +0400
relations:
  method_for:
  - CA-R-1570
atom_id: CA-M-305@12
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Write Workflow schemes using Step references

## Scope

Workflow schemes using Step references.

## Claim

**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, typed directed transitions, result conditions, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** the referenced Step Atoms rather than reproducing them **in** the scheme.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.

## Details
