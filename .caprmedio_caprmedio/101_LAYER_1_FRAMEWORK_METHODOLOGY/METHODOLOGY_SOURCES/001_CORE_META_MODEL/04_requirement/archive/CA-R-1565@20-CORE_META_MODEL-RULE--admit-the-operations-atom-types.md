---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
version: 20
updated_at: 2026-10-29 07:45:27 +0400
relations: {}
atom_id: CA-R-1565@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Admit the Operations Atom Types

## Claim scope

internal Type values of Operations Atoms.

## Claim

the admitted internal values of `Atom/Content Role: Operations/Type` **must** include (Action, Workflow, Step).

## Details

Branch, Fork, and Decision are not admitted internal Type values. Linear and Conditional are Step forms carried by Step definitions, not additional Operations Atom Types.
