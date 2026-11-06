---
atom_id: CA-R-1562
ref_id: CA-R-1562
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom.Header.Form
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1562-CORE_META_MODEL-RULE--define-the-action-operations-atom-type.md
  source_atom_id: CA-R-1562
  source_atom_revision: 27
  source_sha256: fb291779180976175d52053ae03bd1c8d3b5884ccb85baf92d82927be81408d3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define the Action Operations Atom Type

## Claim

### Prose Claim


the Action Type of Operations Atoms.


the Operations Atom Type Action **means** the Type of an Operations Atom whose Claim specifies that same Atom's reusable Action behavior. the Action may be referenced by multiple Step Atoms in multiple Workflows without copying or redefining that behavior.
