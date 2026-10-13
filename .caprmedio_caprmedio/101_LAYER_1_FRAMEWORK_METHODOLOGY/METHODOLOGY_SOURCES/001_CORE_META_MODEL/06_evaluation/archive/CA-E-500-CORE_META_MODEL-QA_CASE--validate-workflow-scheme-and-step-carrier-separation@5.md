---
subjects:
  governs: "Workflow/Carrier"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Directory Carrier"
    - "Atom Collection"
    - "Workflow/Relation Kind: On Result"
version: 5
updated_at: "2026-10-13 17:24:28 +0400"
relations: {"evaluation_for": ["CA-R-1570", "CA-R-1569", "CA-M-305", "CA-D-467"]}
atom_id: "CA-E-500"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
---
# Summary

Validate Workflow scheme and Step carrier separation

## Scope

Workflow representation; Step Carrier separation.

## Claim

the Workflow representation Evaluation **must** reject a Carrier arrangement that duplicates definition authority **or** derives execution order from storage order.

## Details

- a graph references separate Step Atoms, **every** Step binds **`=1`** Action carried outside the entire Workflow **and** nested Step directory tree, **and** two Steps reuse that Action with different inputs **without** copying its behavior: accept.
- place the Workflow Markdown Carrier beside an optional same-stem Directory Carrier containing its separate Step Markdown Carriers, **or** leave the Workflow **and** Steps separately addressable: retain the same graph meaning.
- place a Step Markdown Carrier beside its optional same-stem Directory Carrier containing subordinate Step Markdown Carriers, repeating at any nested Step depth: accept. require the matching sibling Markdown Carrier for **every** Step directory; reject a missing **or** mismatched sibling.
- reorder files **or** folder navigation **without** changing the graph: retain the declared execution order.
- copy Step bindings into the graph, copy Action behavior into a Step, introduce an unresolved Step reference, **or** create another Workflow identity for the folder: reject.
- **when** using a folder-backed Workflow, require **`=1`** sibling Workflow Markdown Carrier with the same filename stem **and** separately carried Step Atoms inside the Directory Carrier; reject a missing **or** mismatched sibling, a second Workflow definition **or** an Action Atom Carrier anywhere inside the directory tree, **or** a folder that silently becomes their owning Scope Unit.
- derive a Step Relation, execution inheritance, **or** execution order from folder nesting instead of the declared graph **and** Step bindings: reject.
- move a Workflow **or** Step Directory Carrier **without** changing the graph **or** Step Atoms' independent Status values: accept; reject a Status cascade **without** an explicit authorized change for **every** affected Step.
