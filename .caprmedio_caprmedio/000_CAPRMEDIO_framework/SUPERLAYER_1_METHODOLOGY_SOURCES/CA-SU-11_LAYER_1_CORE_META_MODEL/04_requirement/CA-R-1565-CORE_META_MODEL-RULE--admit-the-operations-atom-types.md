---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
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

## Claim

### Prose Claim


internal Type values of Operations Atoms.


the admitted internal values of `Atom/(.Header.Role := Operations).Header.Form` **must** include (Action, Workflow, Step).

## Details

Branch, Fork, and Decision are not admitted internal Type values. Linear and Conditional are Step forms carried by Step definitions, not additional Operations Atom Types.
