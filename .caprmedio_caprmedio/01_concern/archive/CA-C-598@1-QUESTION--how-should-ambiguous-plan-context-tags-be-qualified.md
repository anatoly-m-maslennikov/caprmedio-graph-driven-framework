---
atom_id: CA-C-598
ref_id: CA-C-598@1
container:
  scope_unit: CA-SU-00
role: Concern
form: Question
topics:
  main_subject: Subject/Domain/Node/Continuant/Atom.Subjects
  dependencies:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
tier: 3
status: Archived
version: 1
updated_at: 2026-10-24 08:22:44 +0400
carrier_destination:
  file:
    name: CA-C-598@1-QUESTION--how-should-ambiguous-plan-context-tags-be-qualified.md
    path: .caprmedio_caprmedio/01_concern/archive
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

How should ambiguous Plan context tags be qualified?

## Question

Can remaining contextual Evaluation, Workflow, Action and Operations tags stay broad topics instead of being guessed as specific Atom Types or actual Runs?

## Scope

This one-time migration of exact standalone words in Current Plan subjects.depends_on. No GOVERNS default and no RMEDO default.

## Details

Bounded choice: use the same named Engineering topics. These describe technical context for how work is checked, sequenced or performed; they do not assert an independently carried object, an O/E Atom, an executed Run, a record, or a passed check.

The source-specific passes already mapped supported E specifications and O definitions to their precise Domain paths, and check-construction/check-execution mechanisms to their precise Engineering topics. Remaining broad context is not upgraded into those stronger claims merely from a word.

Preserve each Plan's primary topic, actual scope, body, status, Tier and typed relations. A broad topic may be refined during later content review; this migration does not make that refinement mandatory for read-only topic lookup. This is a bounded uncertainty disposition, not a new global default for other Roles or new authoritative rules about Evaluation/Operations.
