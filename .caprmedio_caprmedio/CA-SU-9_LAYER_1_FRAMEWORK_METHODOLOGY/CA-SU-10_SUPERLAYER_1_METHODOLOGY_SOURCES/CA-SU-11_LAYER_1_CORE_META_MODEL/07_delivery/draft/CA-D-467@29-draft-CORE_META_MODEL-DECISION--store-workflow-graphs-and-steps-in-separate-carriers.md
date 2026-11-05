---
atom_id: CA-D-467
ref_id: CA-D-467@29-draft
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/Directory
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom.Header.Container
tier: 3
relations:
  delivery_for:
  - CA-R-1570
  - CA-R-2465
status: Draft
version: 29
updated_at: 2026-11-05 06:15:15 +0400
carrier_destination:
  file:
    name: CA-D-467@29-draft-DECISION--store-workflow-graphs-and-steps-in-separate-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
---
## Summary

Store Workflow graphs **and** Steps in separate carriers

## Claim

### Prose Claim


folder-backed Workflows and optional recursive Step Carriers.


a folder-backed Workflow **must** use **`=1`** Workflow Atom Markdown Carrier **and** **`<=1`** optional sibling Directory Carrier with the same filename stem. the Directory Carrier contains separate Markdown Carriers for its Step Atoms; it **must not** contain a second Workflow definition.

## Details

- the Workflow Atom's main content carries the graph scheme. Each Step Atom carries its own definition: a leaf Step carries its single Action or Workflow reference and parameter/input bindings; a containing Step carries references to its direct contained Steps and has no RUNS target.
- A Step Markdown Carrier **may** have **`<=1`** optional sibling Directory Carrier with the same filename stem containing its direct contained Step Carriers. This same-stem grouping rule applies recursively at every Step level. Grouping is optional for Carrier layout; it does not weaken the requirement that a formal containment edge, `Header.Container`, and placement in the resolved parent folder agree. Ordinary graph references to separately contained Workflow or Step Atoms may remain separately placed. When a directory is used, its matching Step Markdown Carrier remains separately addressable.
- Action Atom Carriers **must** remain separately outside the entire Workflow **and** Step directory tree. Steps reference reusable Actions **without** copying their behavior.
- Carrier placement organizes files. Directory nesting alone must not override the matching `Header.Container` and formal containment edge. The declared Workflow graph defines control flow; a formal Step containment edge identifies its same immediate whole and does not establish execution inheritance **or** execution order. Each Step has exactly one declared composition form: it RUNS one Action, RUNS one Workflow, or contains one or more Steps and RUNS neither target. Every Step has exactly one immediate whole, and its containment chain ends at exactly one root Workflow.
- `Header.Container` identifies each Atom's logical immediate parent by Scope Unit or Atom identity (ID); the parent's folder is resolved from that identity. For a formally contained Step, its `Header.Container`, formal `CONTAINS`/`IS_CONTAINED_BY` edge, and Carrier placement in the resolved parent folder must all identify the same parent. CA-D-264 reads back that same direct containment fact; no second relation is authored. An ordinary graph reference alone does not establish containment, change `Header.Container`, or move the referenced Step.
- the Atom files retain the existing Atom filename, frontmatter, **and** main-content rules; the folder is a grouping Carrier, **not** another Workflow definition **or** owning Scope Unit.
- grouping is optional: ordinary references to separately contained Workflow **and** Step Carriers remain permitted **when** their references resolve unambiguously. A Step with formal containment remains in its declared parent's resolved folder. A carrier-only move does **not** redefine the control-flow graph **or** change carried Status.
- For a folder-backed Workflow or containing-Step parent, every admitted Status change follows CA-R-1521. Its selected descendants are the latest Revisions of all recursively contained Steps in that parent Carrier tree; separately placed referenced Steps and Actions outside the tree are not selected. Older archived Revisions retain their exact bytes, Version and Status. CA-R-1521 governs the required per-Atom Actions, admitted target Status values and same-Status cascade.
- Apply CA-D-466 Status placement inside each local Workflow or Step container. Step descendants actually carried inside a parent Carrier tree remain there for every Status, including Archived. Separately placed referenced Steps remain separately addressable outside that tree and are not moved into it. Apply CA-D-289 Version suffixes to Archive Carrier basenames. This rule does not migrate noncanonical legacy `archive/` trees.
- Read each Step's Status from its own Markdown Carrier under CA-D-483; containing Status directories or parents must not override it. The cascade writes selected latest Revisions as governed by CA-R-1521; it does not infer execution order or execution inheritance.
