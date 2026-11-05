---
atom_id: CA-E-500
ref_id: CA-E-500
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 4
relations:
  evaluation_for:
  - CA-R-1570
  - CA-R-2465
  - CA-M-305
  - CA-D-467
status: Active
version: 28
updated_at: 2026-11-02 17:54:42 +0400
carrier_destination:
  file:
    name: CA-E-500-CORE_META_MODEL-EVAL_CASE--validate-workflow-scheme-and-step-carrier-separation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate Workflow scheme and Step carrier separation

## Claim

### Prose Claim


Workflow representation; Step Carrier separation.


the Workflow representation Evaluation **must** reject a Carrier arrangement that duplicates definition authority **or** derives execution order from storage order.

## Details

- a graph references separate Step Atoms; **every** leaf Step RUNS **`=1`** Action **or** Workflow. A referenced Action is carried outside the entire Workflow **and** Step directory tree; a called Workflow retains its separate identity and reference. A containing Step contains **`1+`** leaf Substeps and RUNS neither an Action nor a Workflow. A leaf Step's bindings use only previous Step outputs, enclosing Workflow Run input, or values fixed by that Step. Two leaf Steps may reuse the same Action with different inputs **without** copying its behavior: accept.
- place the Workflow Markdown Carrier beside an optional same-stem Directory Carrier containing its separate Step Markdown Carriers, **or** leave the Workflow **and** Steps separately addressable: retain the same graph meaning.
- place a Step Markdown Carrier beside its optional same-stem Directory Carrier containing its leaf Substep Markdown Carriers: accept. require the matching sibling Markdown Carrier for **every** Step directory; reject a missing **or** mismatched sibling. A Substep directory or another nested Step directory is not admitted by this layout.
- reorder files **or** folder navigation **without** changing the graph: retain the declared execution order.
- copy Step bindings into the graph, copy Action behavior into a Step, introduce an unresolved Step reference, **or** create another Workflow identity for the folder: reject.
- **when** using a folder-backed Workflow, require **`=1`** sibling Workflow Markdown Carrier with the same filename stem **and** separately carried Step Atoms inside the Directory Carrier; reject a missing **or** mismatched sibling, a second Workflow definition **or** an Action Atom Carrier anywhere inside the directory tree, **or** a folder that silently becomes their owning Scope Unit.
- derive a Step Relation, execution inheritance, **or** execution order from folder nesting instead of the declared graph **and** Step bindings: reject.
- move a Workflow **or** Step Directory Carrier **without** a Status-change request: retain the graph **and** carried Step and Substep Status values. read each Step and Substep's own Status; reject read-time inference from its parent **or** path.
- change a Workflow **or** containing Step parent's Status to an admitted value: require independent single-Atom Actions for that parent **and** the latest Revision of every contained Step and Substep under CA-R-1521: a Workflow's direct Steps and their direct leaf Substeps, or a Step's direct leaf Substeps. check each Atom's own model; reject an invented target value **or** a multi-target Action.
- include Draft, Active **and** Archived transitions admitted by the selected model; require the same requested Status for **all** contained latest Step and Substep Revisions. leave separately placed referenced Steps **and** Actions outside the tree unchanged.
- retain the Workflow-to-Step-to-Substep descendants inside the parent Carrier tree, including Archived placement under CA-D-466 **and** CA-D-289. preserve exact bytes, Version **and** Status of older archived Revisions; reject their inclusion as cascade targets **or** their metadata rewrite. no migration of legacy `archive/` trees is implied.
