---
atom_id: CA-R-1517
ref_id: CA-R-1517
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Methodology Sources
tier: 3
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1517-PROJECT_CONFIGURATION-RULE--keep-tool-operational-authority-outside-its-own-subtree.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1517-PROJECT_CONFIGURATION-RULE--keep-tool-operational-authority-outside-its-own-subtree.md
  source_atom_id: CA-R-1517
  source_atom_revision: 18
  source_sha256: d08a520b6ead06bf6bbca310de105264a4151c2b41fcc8b890bd2647e02ee239
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Tool operational authority outside its own subtree

## Claim

### Prose Claim


Tools' implementation references to methodology Action and Workflow definitions in the caprmedio Project.


**in** the caprmedio Project, a Tool's implementation reference **to** a methodology Action **or** Workflow definition **must not** target an O Atom owned by the Tool's Scope Unit **or** **any** descendant of that Scope Unit.

## Details

- the restriction concerns the owner of the operational definition, **not** the location of the Tool's code, prompts, **or** runtime results.
- methodology Evaluations of their own Action **and** Workflow definitions under CA-R-1518 are **not** Tool implementation references **and** are **not** prohibited by this rule.

this restriction prevents self-reference through the Tool's own subtree; it does **not** establish that **all** indirect dependency cycles are absent.
