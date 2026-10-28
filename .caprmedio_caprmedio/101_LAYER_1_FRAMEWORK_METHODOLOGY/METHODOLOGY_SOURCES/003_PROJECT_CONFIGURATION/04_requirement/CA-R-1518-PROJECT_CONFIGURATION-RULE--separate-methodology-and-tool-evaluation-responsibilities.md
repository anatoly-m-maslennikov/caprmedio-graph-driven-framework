---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: evaluation_for'
version: 20
updated_at: 2026-10-27 19:59:56 +0400
relations:
  depends_on:
  - CA-R-1018
  - CA-E-486
atom_id: CA-R-1518
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Separate methodology and Tool Evaluation responsibilities

## Scope

Evaluation responsibility for operational definitions and their Tool implementations.

## Claim

**in** the CAPRMEDIO Project, Evaluation responsibility for operational definitions **and** their Tool implementations **must** follow this allocation:

## Details

- methodology source Scope Units own Evaluations of Action **and** Workflow definitions, including valid Action references, Step inputs, typed transitions, **and** termination **or** bounded retry conditions. these Evaluations **may** directly check O authority under CA-R-1018; checks for Steps **and** Runs reuse CA-E-486 **when** applicable.
- TOOLS **and** its Tool Scope Units own Evaluations of Tools: implementation behavior, interfaces, failures, **and** conformance **to** the Action implemented by the Tool. these Evaluations **must not** independently define the correctness rules of the referenced Action **or** Workflow.

checking whether a Tool realizes an Action correctly is distinct from checking whether that Action's definition is valid. a Tool test **may** use the methodology definition as its expected-behavior authority **without** taking ownership of definition validation.
