---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  passive:
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Methodology Sources
  - CAPRMEDIO_MODEL <+ Scope Unit
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - CAPRMEDIO_MODEL <+ Package
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Verification
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//evaluation_for
version: 25
updated_at: 2026-11-02 18:35:20 +0400
relations:
  depends_on:
  - CA-R-1018
  - CA-E-486
atom_id: CA-R-1518
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1518-PROJECT_CONFIGURATION-RULE--separate-methodology-and-tool-evaluation-responsibilities.md
  source_atom_id: CA-R-1518
  source_atom_revision: 25
  source_sha256: a9a6736286df475fc2c63e800a57e683212aa720845c0435fef12108f1c8ced5
  original_relations_sha256: a160656a5227133f915358025dba2043d381de3a00738d92f5015d7253981f14
---
## Summary

Separate methodology and Tool Evaluation responsibilities

## Claim

### Prose Claim


Evaluation responsibility for operational definitions and their Tool implementations.


**in** the CAPRMEDIO Project, Evaluation responsibility for operational definitions **and** their Tool implementations **must** follow this allocation:

## Details

- methodology source Scope Units own Evaluations of Action **and** Workflow definitions, including valid Action references, Step inputs, typed transitions, **and** termination **or** bounded retry conditions. these Evaluations **may** directly check O authority under CA-R-1018; checks for Steps **and** Runs reuse CA-E-486 **when** applicable.
- TOOLS **and** its Tool Scope Units own Evaluations of Tools: implementation behavior, interfaces, failures, **and** conformance **to** the Action implemented by the Tool. these Evaluations **must not** independently define the correctness rules of the referenced Action **or** Workflow.

checking whether a Tool realizes an Action correctly is distinct from checking whether that Action's definition is valid. a Tool test **may** use the methodology definition as its expected-behavior authority **without** taking ownership of definition validation.
