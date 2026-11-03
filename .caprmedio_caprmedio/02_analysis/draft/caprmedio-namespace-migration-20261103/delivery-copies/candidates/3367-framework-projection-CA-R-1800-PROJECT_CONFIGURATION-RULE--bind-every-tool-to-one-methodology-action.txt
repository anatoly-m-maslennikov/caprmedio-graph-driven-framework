---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Package
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - CAPRMEDIO <+ STRUCTURE <+ Entity/Object/Continuant/Selection//Methodology Sources
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Architecture <+ Component Structure
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering
version: 19
updated_at: 2026-11-02 18:35:20 +0400
relations:
  depends_on:
  - CA-R-2465
atom_id: CA-R-1800
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action.md
  source_atom_id: CA-R-1800
  source_atom_revision: 19
  source_sha256: 159f57b52e20b145c3a06156fe6af7482771bd3b5c74bfab70a07c7f1864d7a7
  original_relations_sha256: 95a170d690ef47b6d4b2bfc3b07de342c82190a4797a6703732198276c9572d0
---
## Summary

Bind **every** Tool to one methodology Action

## Claim scope

Tools in the caprmedio Project.

## Claim

**in** the caprmedio Project, **every** Tool **must** implement **`=1`** Action defined by an existing applicable methodology O Atom.

## Details

- the Tool's RMED identifies that Action as the behavior it realizes **and** specifies its implementation obligations **without** copying the canonical Action definition.
- a Workflow Step binds its Action under CA-R-2465; the corresponding Tool realizes that Action rather than redefining the Workflow graph.
- this cardinality constrains the Action implemented by the Tool. it does **not** count internal instructions, API calls, interactions, **or** retries.

the binding is **not** a requirement **to** use that Action **or** a particular Workflow **to** build the Tool.
