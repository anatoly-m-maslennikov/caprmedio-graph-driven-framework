---
atom_id: CA-D-467
ref_id: CA-D-467@29
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/Directory
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Step
tier: 3
relations:
  delivery_for:
  - CA-R-1570
  - CA-R-2465
status: Archived
version: 29
updated_at: '2026-11-11 15:27:11 +0400'
carrier_destination:
  file:
    name: CA-D-467@29-CORE_META_MODEL-DECISION--store-workflow-graphs-and-steps-in-separate-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Store Workflow graphs **and** Steps in separate carriers

## Claim

### Prose Claim


folder-backed Workflows, Step Carriers, **and** their leaf Substep Carriers.


a folder-backed Workflow **must** use **`=1`** Workflow Atom Markdown Carrier **and** **`<=1`** optional sibling Directory Carrier with the same filename stem. the Directory Carrier contains separate Markdown Carriers for its Step Atoms; it **must not** contain a second Workflow definition.

## Details

- the Workflow Claim carries one Mermaid Scheme as a diagram-first visual summary; its text independently specifies the complete graph and may be repeated by the diagram. A Step Claim may carry at most one Mermaid Scheme with the same summary semantics. A leaf Step Atom carries its Action or Workflow reference and parameter/input bindings, while a containing Step carries its leaf Substep structure without RUNS.
- a containing Step Markdown Carrier **may** have **`<=1`** optional sibling Directory Carrier with the same filename stem containing its leaf Substep Markdown Carriers. this one-level Workflow-to-Step-to-Substep layout retains every folder-backed Step and Substep in its own Markdown Carrier; a Substep directory or another nested Step directory is not admitted.
- Action Atom Carriers **must** remain separately outside the entire Workflow **and** Step directory tree. Steps reference reusable Actions **without** copying their behavior.
- folder nesting organizes Carriers; it **must not** establish a Step/Substep Relation, execution inheritance, **or** execution order. the Workflow graph defines control flow; **every** leaf Step retains its own invocation of **`=1`** referenced Action or Workflow, and a containing Step has **`1+`** Substeps and no RUNS relation.
- the Atom files retain the existing Atom filename, frontmatter, **and** main-content rules; the folder is a grouping Carrier, **not** another Workflow definition **or** owning Scope Unit.
- grouping is optional: separately placed Workflow **and** Step Carriers remain permitted **when** their references resolve unambiguously. a carrier-only move does **not** redefine the graph **or** change carried Status.
- **every** admitted Workflow **or** containing Step parent Status change requires the containment cascade under CA-R-1521: compose independent single-Atom Actions for the latest Revision of the Workflow's direct Steps and their direct leaf Substeps, or the Step's direct leaf Substeps, requesting the same Status under each Atom's own model. separately placed referenced Steps **and** Actions outside the Carrier tree are **not** cascade targets; older archived Revisions retain their exact bytes, Version **and** Status.
- apply CA-D-466: Current Workflow, Step and Substep Carriers are placed locally in their actual containers. Draft and Archived Markdown Carriers are placed in the owning Scope Unit’s shared Operations `draft` and `archived` directories, regardless of logical container; apply CA-D-289’s Version suffixes to Archived Carrier basenames. This rule does **not** authorize independent legacy moves or rewrites.
- read each Step and Substep's Status from its own Markdown Carrier under CA-D-483; containing Status directories **or** parents **must not** override it. the cascade writes the changed latest Revisions; it **does not** infer execution order **or** execution inheritance.
