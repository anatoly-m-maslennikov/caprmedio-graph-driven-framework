---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1565
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Admit the Operations Atom Types

## Claim scope

internal Type values of Operations Atoms.

## Claim

the admitted internal values of `Atom/Content Role: Operations/Type` **must** include (Action, Workflow, Step).

## Details

Branch, Fork, and Decision are not admitted internal Type values. Linear and Conditional are Step forms carried by Step definitions, not additional Operations Atom Types.
