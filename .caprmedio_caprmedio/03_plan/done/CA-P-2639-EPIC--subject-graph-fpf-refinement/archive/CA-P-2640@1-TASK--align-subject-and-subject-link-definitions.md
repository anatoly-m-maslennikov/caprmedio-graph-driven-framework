---
atom_id: CA-P-2640@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-26 04:51:47 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Align Subject and Subject-link definitions

## Objective

Align the governing Subject definitions with Operator decision D01:
Subject names the thing or topic; GOVERNS / DEPENDS_ON are the special
relations from an Atom to nodes in the Subject graph.

## Details

This Task addresses the Subject/link part of I01 and G01, not the unresolved
temporal classification of Graph Nodes. Estimated own work: up to 15 minutes.

- Read Current R1275 and R2006, then the directly affected GOVERNS / DEPENDS_ON
  definitions. The review observed R1275@24 and R2006@7; those are evidence
  references, not fixed execution pins.
- Correct the relation-only definition of Subject. The set of Subjects forms
  a graph; its nodes are the things or topics addressed by Atom Subjects.
  The Atom is the source of GOVERNS / DEPENDS_ON, and the addressed Subject
  graph node is the target. A path names the target, not the relation itself.
- Preserve the distinction between an object and its description. Do not mint
  another intermediate Subject object, new Domain entity, relation kind,
  authority precedence rule or generic named Selection.
- Keep role, Type and Local Scope Unit independent from Subject. Do not force
  abstract topics into Continuant or Occurrent while that question is open.
- Use normal predecessor history for changed Current definitions; leave
  existing Drafts, Archives and unrelated sources unchanged.
- Record changed source IDs and versions and any concrete unresolved consumer
  conflict. Split further work into a separate Task rather than expanding this
  one beyond its own-work estimate.

No code, renderer, MCP, Terms Graph or runtime implementation is included.
Do not claim the complete FPF finding closed before its remaining root
classification question and the affected-source checks are resolved.

## Definition of Done

- The changed definitions use the Operator's accepted meaning of Subject.
- GOVERNS and DEPENDS_ON are links to Subject graph nodes, not synonymous
  names for the nodes.
- A Domain thing, an Engineering topic and a Documentation topic can each
  be named without inventing a new identity or temporal classification.
- No touched definition still calls Subject itself the Atom-to-target link.
- Actual source edits and their predecessors are recorded; the Task does
  not report a projection rebuild or complete I01 closure that did not occur.
