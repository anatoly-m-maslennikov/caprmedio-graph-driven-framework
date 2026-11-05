---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
version: 27
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1563
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Define the Workflow Operations Atom Type

## Claim

### Prose Claim


the Workflow Type of Operations Atoms.


the Operations Atom Type Workflow **means** the Type of an Operations Atom whose Claim specifies **`=1`** Workflow graph scheme for that same Atom using references **to** Step Atoms and the Workflow's declared Step structure.
