---
atom_id: CA-C-600
ref_id: CA-C-600
role: Concern
form: Question
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-24 08:47:45 +0400
topics:
  main_subject: Subject/Domain/Node/Continuant/Atom.Subjects
  dependencies:
  - Subject/Engineering/Implementation
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-C-600-CAPRMEDIO-QUESTION--how-should-existing-plan-implementation-context-tags-be-qualified.md
    path: .caprmedio_caprmedio/01_concern
---
# Summary

How should existing Plan implementation-context tags be qualified?

## Question

Does a bare Implementation dependency in a Plan mean an independent Domain node, or the technical implementation topic already used by the methodology?

## Scope

Exact standalone Implementation values in Current Plan subjects.depends_on only. Qualified legacy paths, governed Implementation nodes and all RMEDO owners remain separately reviewed.

## Details

Bounded choice: qualify the existing contextual topic as Subject/Engineering/Implementation, already governed by Current R1873. Candidate #7 treats Engineering topics as subjects of how a project is built and realized, not necessarily independent objects.

This preserves an existing general dependency tag without narrowing it to a mentioned tool, graph, validation subsystem or native object. It does not assert a new Implementation Content Role or Domain entity, claim that code exists, or approve obsolete task content. Preserve the Plan Objective, lifecycle, ownership, relations and all unrelated metadata.
