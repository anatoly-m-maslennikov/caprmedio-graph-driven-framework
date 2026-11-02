---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
version: 17
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1565@17
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Admit the Operations Atom Types

## Scope

internal Type values of Operations Atoms.

## Claim

the admitted internal values of `Atom/Content Role: Operations/Type` **must** include (Action, Workflow, Step).

## Details

Branch, Fork, and Decision are not admitted internal Type values. Linear and Conditional are Step forms carried by Step definitions, not additional Operations Atom Types.
