---
atom_id: CA-C-604
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-27 15:50:10 +0400
subjects:
  governs: Subject/Graph Node
  depends_on:
  - Subject/Graph Node/Implementation
  - Subject/Graph Node/Domain/Continuant/Atom
relations: {}
---
# Summary

Where should the Implementation Subject branch live?

## Question

Should Implementation belong under `Subject/Graph Node/Domain/Continuant/Atom/Content Role: Implementation`, remain at `Subject/Graph Node/Implementation`, or have another placement?

## Scope

Placement of Implementation in the Subject hierarchy and its relationship to Content Role I and Atom.

## Details

The existing Implementation branch contains Code, Prompts, Documentation and Resources. The Operator identifies Implementation as Content Role I; the established model has no Implementation Atoms.

The proposed direct rename to `Subject/Graph Node/Content Role: Implementation` was paused when the placement question was reopened. Keep the Current Implementation branch outside Domain while this Question is open. No batch move is authorized by this record.

Resolve whether placing Implementation under Atom would classify its code, prompts and documentation as Atoms, and how to represent Content Role I without losing the distinction between classification and the actual implementation units.

The current baseline is [Candidate #9 / P2667](../03_plan/done/CA-P-2665-EPIC--refine-engineering-subject-branch/done/02-CA-P-2667-TASK--settle-engineering-subject-structure.md).
