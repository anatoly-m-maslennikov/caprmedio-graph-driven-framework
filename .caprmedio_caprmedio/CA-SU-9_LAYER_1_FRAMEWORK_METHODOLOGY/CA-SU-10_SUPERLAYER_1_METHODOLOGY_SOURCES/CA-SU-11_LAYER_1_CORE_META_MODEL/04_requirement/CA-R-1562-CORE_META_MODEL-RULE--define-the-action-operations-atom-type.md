---
atom_id: CA-R-1562
ref_id: CA-R-1562
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Action
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Form
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Action
tier: 1
status: Active
version: 27
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1562-CORE_META_MODEL-RULE--define-the-action-operations-atom-type.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define the Action Operations Atom Type

## Claim

### Prose Claim


the Action Type of Operations Atoms.


the Operations Atom Type Action **means** the Type of an Operations Atom whose Claim specifies that same Atom's reusable Action behavior. the Action may be referenced by multiple Step Atoms in multiple Workflows without copying or redefining that behavior.
