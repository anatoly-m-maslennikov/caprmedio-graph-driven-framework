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
version: 6
updated_at: "2026-10-13 18:23:23 +0400"
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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-500-CORE_META_MODEL-QA_CASE--validate-workflow-scheme-and-step-carrier-separation.md
  source_atom_id: CA-E-500
  source_atom_revision: 6
  source_sha256: c87e71a0928926c3b34570761a61e64c5c0702e0cb63240c63d4bd46191c3740
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
- move a Workflow **or** Step Directory Carrier **without** a Status-change request: retain the graph **and** carried Step Status values. read each Step's own Status; reject read-time inference from its parent **or** path.
- change a Workflow **or** Step parent's Status to an admitted value: require independent single-Atom Actions for that parent **and** the latest Revision of **every** recursively contained Step under CA-R-1521, including nested Steps. check each Atom's own model; reject an invented target value **or** a multi-target Action.
- include Draft, Active **and** Archived transitions admitted by the selected model; require the same requested Status for **all** contained latest Step Revisions. leave separately placed referenced Steps **and** Actions outside the tree unchanged.
- retain descendants inside the parent Carrier tree, including Archived placement under CA-D-466 **and** CA-D-289. preserve exact bytes, Version **and** Status of older archived Revisions; reject their inclusion as cascade targets **or** their metadata rewrite. no migration of legacy `archive/` trees is implied.
