---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Carrier/Directory
  - CAPRMEDIO_MODEL <+ Atom.Header.Container
version: 29
updated_at: 2026-11-05 06:15:15 +0400
relations:
  evaluation_for:
  - CA-R-1570
  - CA-R-2465
  - CA-M-305
  - CA-D-467
atom_id: CA-E-500
ref_id: CA-E-500@29-draft
status: Draft
tier: 4
role: Evaluation
form: Eval Case
carrier_destination:
  file:
    name: CA-E-500@29-draft-EVAL_CASE--validate-workflow-scheme-and-step-carrier-separation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Validate Workflow scheme and Step carrier separation

## Claim

### Prose Claim


Workflow representation; Step Carrier separation.


the Workflow representation Evaluation **must** reject a Carrier arrangement that duplicates definition authority **or** derives execution order from storage order.

## Details

- a graph references separate Step Atoms. Each Step has exactly one form: it RUNS **`=1`** Action, RUNS **`=1`** Workflow, or contains **`1+`** Steps and RUNS neither target. Each Step has exactly one immediate whole, either its Workflow or a containing Step, and the containment chain ends at exactly one root Workflow. A referenced Action remains outside the entire Workflow and nested Step directory tree; a called Workflow retains its separate identity and reference. A leaf Step's bindings use only previous Step outputs, enclosing Workflow Run input, or values fixed by that Step. Two Steps may reuse the same Action with different inputs without copying its behavior: accept.
- place the Workflow Markdown Carrier beside an optional same-stem Directory Carrier containing its formally contained Step Markdown Carriers, **or** keep ordinary references to separately contained Steps separately addressable: retain the same control-flow graph.
- place a Step Markdown Carrier beside an optional same-stem Directory Carrier containing its directly contained Step Carriers: accept. Apply this rule recursively at every Step level. When a Step directory is present, require its matching Step Markdown Carrier; reject a missing or mismatched sibling. Also accept ordinary graph references to separately contained Steps. Directory nesting alone does not establish formal containment or execution order.
- for every Workflow and Step Atom, require `Header.Container` to identify its logical immediate parent by Scope Unit or Atom identity (ID); resolve the parent's folder from that identity. For each formal Workflow `CONTAINS` Step or Step `IS_CONTAINED_BY` Workflow/containing Step edge, require the same parent in `Header.Container`, the formal edge, and the Step Carrier's resolved placement; require CA-D-264's direct containment readback to agree. Reject any disagreement. An ordinary graph reference alone does not establish or change containment, assign `Header.Container`, or move the referenced Step.
- reorder files **or** folder navigation **without** changing the graph: retain the declared execution order.
- copy Step bindings into the graph, copy Action behavior into a Step, introduce an unresolved Step reference, **or** create another Workflow identity for the folder: reject.
- **when** using a folder-backed Workflow, require **`=1`** sibling Workflow Markdown Carrier with the same filename stem **and** separately carried Step Atoms inside the Directory Carrier; reject a missing **or** mismatched sibling, a second Workflow definition **or** an Action Atom Carrier anywhere inside the directory tree, **or** a folder that silently becomes their owning Scope Unit.
- derive a Step graph edge, execution inheritance, **or** execution order from folder nesting alone instead of the declared graph **and** Step bindings: reject. Formal containment remains governed by the matching `Header.Container`, `CONTAINS`/`IS_CONTAINED_BY` edge, and resolved placement.
- move a Workflow or Step Directory Carrier without a Status-change request: retain the graph and each carried Step Status. Read each Step's own Status under CA-D-483; reject read-time inference from its parent or path.
- change a Workflow or containing Step parent's Status to an admitted value: select the latest Revision of every recursively contained Step under CA-R-1521 and apply the requested Status under each Atom's own model. Compose separately admitted single-Atom Actions for the parent and each selected Step. Reject an invented target value or a multi-target Action. Separately placed referenced Steps and Actions outside the parent Carrier tree are not cascade targets.
- include Draft, Active and Archived transitions admitted by each applicable Status model; require the same requested Status for all recursively contained latest Step Revisions. Leave separately placed referenced Steps and Actions outside the tree unchanged.
- retain Step descendants actually carried inside the parent Carrier tree there for every Status, including Archived placement under CA-D-466 and CA-D-289. Keep separately placed referenced Steps outside that tree and separately addressable. Preserve exact bytes, Version and Status of older archived Revisions; reject their inclusion as cascade targets or metadata rewrite. No migration of legacy `archive/` trees is implied.
