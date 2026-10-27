---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Continuant/Carrier/Directory Carrier
version: 19
updated_at: 2026-10-26 17:20:40 +0400
relations:
  evaluation_for:
  - CA-R-1570
  - CA-R-1569
  - CA-M-305
  - CA-D-467
atom_id: CA-E-500@19
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 4
---
# Summary

Validate Workflow scheme and Step carrier separation

## Scope

Workflow representation; Step Carrier separation.

## Claim

the Workflow representation Evaluation **must** reject a Carrier arrangement that duplicates definition authority **or** derives execution order from storage order.

## Details

- a graph references separate Step Atoms; **every** leaf Step binds **`=1`** Action carried outside the entire Workflow **and** nested Step directory tree, while a containing Step may contain nested Steps and binds no Action; two leaf Steps may reuse that Action with different inputs **without** copying its behavior: accept.
- place the Workflow Markdown Carrier beside an optional same-stem Directory Carrier containing its separate Step Markdown Carriers, **or** leave the Workflow **and** Steps separately addressable: retain the same graph meaning.
- place a Step Markdown Carrier beside its optional same-stem Directory Carrier containing subordinate Step Markdown Carriers, repeating at any nested Step depth: accept. require the matching sibling Markdown Carrier for **every** Step directory; reject a missing **or** mismatched sibling.
- reorder files **or** folder navigation **without** changing the graph: retain the declared execution order.
- copy Step bindings into the graph, copy Action behavior into a Step, introduce an unresolved Step reference, **or** create another Workflow identity for the folder: reject.
- **when** using a folder-backed Workflow, require **`=1`** sibling Workflow Markdown Carrier with the same filename stem **and** separately carried Step Atoms inside the Directory Carrier; reject a missing **or** mismatched sibling, a second Workflow definition **or** an Action Atom Carrier anywhere inside the directory tree, **or** a folder that silently becomes their owning Scope Unit.
- derive a Step Relation, execution inheritance, **or** execution order from folder nesting instead of the declared graph **and** Step bindings: reject.
- move a Workflow **or** Step Directory Carrier **without** a Status-change request: retain the graph **and** carried Step Status values. read each Step's own Status; reject read-time inference from its parent **or** path.
- change a Workflow **or** Step parent's Status to an admitted value: require independent single-Atom Actions for that parent **and** the latest Revision of **every** recursively contained Step under CA-R-1521, including nested Steps. check each Atom's own model; reject an invented target value **or** a multi-target Action.
- include Draft, Active **and** Archived transitions admitted by the selected model; require the same requested Status for **all** contained latest Step Revisions. leave separately placed referenced Steps **and** Actions outside the tree unchanged.
- retain descendants inside the parent Carrier tree, including Archived placement under CA-D-466 **and** CA-D-289. preserve exact bytes, Version **and** Status of older archived Revisions; reject their inclusion as cascade targets **or** their metadata rewrite. no migration of legacy `archive/` trees is implied.
