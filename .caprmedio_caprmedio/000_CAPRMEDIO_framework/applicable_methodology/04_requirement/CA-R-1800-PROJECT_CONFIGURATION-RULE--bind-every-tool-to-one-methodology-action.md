---
atom_id: CA-R-1800
ref_id: CA-R-1800
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Methodology Sources
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure"
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering
tier: 3
relations:
  depends_on:
  - CA-R-2465
status: Active
version: 19
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action.md
  source_atom_id: CA-R-1800
  source_atom_revision: 19
  source_sha256: d328fb8e3c5ab8ea50ba889c030583a3bf98105d0938d26c74cb43c379189eeb
  original_relations_sha256: 95a170d690ef47b6d4b2bfc3b07de342c82190a4797a6703732198276c9572d0
---
## Summary

Bind **every** Tool to one methodology Action

## Claim

### Prose Claim


Tools in the caprmedio Project.


**in** the caprmedio Project, **every** Tool **must** implement **`=1`** Action defined by an existing applicable methodology O Atom.

## Details

- the Tool's RMED identifies that Action as the behavior it realizes **and** specifies its implementation obligations **without** copying the canonical Action definition.
- a Workflow Step binds its Action under CA-R-2465; the corresponding Tool realizes that Action rather than redefining the Workflow graph.
- this cardinality constrains the Action implemented by the Tool. it does **not** count internal instructions, API calls, interactions, **or** retries.

the binding is **not** a requirement **to** use that Action **or** a particular Workflow **to** build the Tool.
