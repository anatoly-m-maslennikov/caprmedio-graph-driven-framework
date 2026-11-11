---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  passive:
  - CAPRMEDIO <+ STRUCTURE <+ Entity/Object/Continuant/Selection//Methodology Sources
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - CAPRMEDIO <+ MODEL <+ Package
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Verification
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation//evaluation_for
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
---
## Summary

Separate methodology and Tool Evaluation responsibilities

## Claim scope

Evaluation responsibility for operational definitions and their Tool implementations.

## Claim

**in** the CAPRMEDIO Project, Evaluation responsibility for operational definitions **and** their Tool implementations **must** follow this allocation:

## Details

- methodology source Scope Units own Evaluations of Action **and** Workflow definitions, including valid Action references, Step inputs, typed transitions, **and** termination **or** bounded retry conditions. these Evaluations **may** directly check O authority under CA-R-1018; checks for Steps **and** Runs reuse CA-E-486 **when** applicable.
- TOOLS **and** its Tool Scope Units own Evaluations of Tools: implementation behavior, interfaces, failures, **and** conformance **to** the Action implemented by the Tool. these Evaluations **must not** independently define the correctness rules of the referenced Action **or** Workflow.

checking whether a Tool realizes an Action correctly is distinct from checking whether that Action's definition is valid. a Tool test **may** use the methodology definition as its expected-behavior authority **without** taking ownership of definition validation.
