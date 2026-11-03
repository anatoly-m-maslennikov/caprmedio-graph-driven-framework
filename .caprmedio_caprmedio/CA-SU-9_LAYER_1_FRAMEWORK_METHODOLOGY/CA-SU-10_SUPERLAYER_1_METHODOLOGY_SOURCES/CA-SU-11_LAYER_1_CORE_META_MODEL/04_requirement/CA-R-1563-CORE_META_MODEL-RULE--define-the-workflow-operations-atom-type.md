---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Role:=Operations)/Workflow
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
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

## Claim scope

the Workflow Type of Operations Atoms.

## Claim

the Operations Atom Type Workflow **means** the Type of an Operations Atom whose Claim specifies **`=1`** Workflow graph scheme for that same Atom using references **to** Step Atoms and the Workflow's declared Step structure.
