---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
version: 16
updated_at: 2026-10-27 19:59:41 +0400
relations:
  method_for:
  - CA-R-1570
atom_id: CA-M-305
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
- state the entry, declared Step order and structural Relations, Conditional Step routing, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** leaf Step Atoms rather than reproducing them **in** the scheme; a containing Step carries its nested substeps and no own Action launch.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.

## Details
