---
subjects:
  active: Package
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Entity/Object/Continuant/Selection//Methodology Sources
  - Atom/(.Role := Operations)
  - Aspects <+ Engineering <+ Architecture <+ Component Structure
  - Aspects <+ Engineering
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
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action.md
  source_atom_id: CA-R-1800
  source_atom_revision: 19
  source_sha256: c9e7e33f2a87fa3df303df2bfe358d02c38279cc416fc5bfa47fbaa61923acb9
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
