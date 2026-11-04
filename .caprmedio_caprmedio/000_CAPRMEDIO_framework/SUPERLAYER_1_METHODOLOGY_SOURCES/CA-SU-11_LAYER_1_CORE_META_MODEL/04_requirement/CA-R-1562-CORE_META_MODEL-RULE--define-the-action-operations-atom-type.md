---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom.Header.Form
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
version: 27
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1562
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Define the Action Operations Atom Type

## Claim

### Prose Claim


the Action Type of Operations Atoms.


the Operations Atom Type Action **means** the Type of an Operations Atom whose Claim specifies that same Atom's reusable Action behavior. the Action may be referenced by multiple Step Atoms in multiple Workflows without copying or redefining that behavior.
