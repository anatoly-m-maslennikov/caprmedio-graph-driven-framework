---
atom_id: CA-P-2640
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject
version: 3
updated_at: 2026-10-26 06:39:23 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Align Subject and Subject-link definitions

## Objective

Align the governing Subject definitions with Operator decision D01:
Subject names the thing or topic an Atom governs or depends on.
Define GOVERNS / DEPENDS_ON separately as the special relations from an Atom
to nodes in the Subject graph; their defining Atoms depend_on the Subject
definition.

## Details

This Task addresses the Subject/link part of I01 and G01. P2641 separately
handles the accepted open categories of Graph Nodes. Estimated own work: up to 15 minutes.

- Read Current R1275 and R2006, then the directly affected GOVERNS / DEPENDS_ON
  definitions. The review observed R1275@24 and R2006@7; those are evidence
  references, not fixed execution pins.
- Keep the Subject definition to the Operator's exact sentence above; remove
  its old relation-only meaning. Do not fold relation definitions into it.
- Define GOVERNS / DEPENDS_ON in their own Atoms. Reuse existing definitions
  where their identities and meaning fit; add the typed depends_on relation
  from each defining Atom to the Subject-definition Atom.
- The set of Subjects forms a graph. The Atom is the source of GOVERNS /
  DEPENDS_ON, and the addressed Subject graph node is the target. A path
  names the target, not the relation itself.
- Preserve the distinction between an object and its description. Do not mint
  another intermediate Subject object, new Domain entity, relation kind,
  authority precedence rule or generic named Selection.
- Keep role, Type and Local Scope Unit independent from Subject. Coordinate
  with P2641's open Continuant/Occurrent/Aspect categories; no new taxonomy
  or bulk remapping is part of this Task.
- Use normal predecessor history for changed Current definitions; leave
  existing Drafts, Archives and unrelated sources unchanged.
- Record changed source IDs and versions and any concrete unresolved consumer
  conflict. Split further work into a separate Task rather than expanding this
  one beyond its own-work estimate.

No code, renderer, MCP, Terms Graph or runtime implementation is included.
Do not claim the complete FPF finding closed before P2641 and the affected
source checks are complete.

### Completion evidence

R1275@25, R1199@28 and R1200@31 define Subject and its separate typed links; both link definitions depend on R1275. V01/V02 PASS.

Source verification: `.caprmedio_tmp/subject-fpf-refinement/verify.final.md`.
Final source/output pins: `.caprmedio_tmp/subject-fpf-refinement/graph-closure/graph.subject-views.manifest.json`.
Actual effect verified; no production tool/runtime implementation or release is claimed.

## Definition of Done

- The changed definitions use the Operator's accepted meaning of Subject.
- GOVERNS and DEPENDS_ON are defined separately as links to Subject graph
  nodes. Their defining Atoms depend_on the Subject-definition Atom.
- A Domain thing, an Engineering topic and a Documentation topic can each
  be named without inventing a new identity or temporal classification.
- No touched definition still calls Subject itself the Atom-to-target link.
- Actual source edits and their predecessors are recorded; the Task does
  not report a projection rebuild or complete I01 closure that did not occur.
