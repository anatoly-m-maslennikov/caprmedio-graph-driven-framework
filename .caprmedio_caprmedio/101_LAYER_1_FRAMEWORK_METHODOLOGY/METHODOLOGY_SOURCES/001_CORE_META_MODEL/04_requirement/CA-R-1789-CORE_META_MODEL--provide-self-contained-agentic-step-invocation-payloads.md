---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Invocation Context
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action.Execution Kind'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Execution Context
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 16
updated_at: 2026-10-27 20:00:03 +0400
relations: {}
atom_id: CA-R-1789
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Provide self-contained Agentic Step Invocation payloads

## Scope

an executor dispatching **or** resuming an Agentic Step.

## Claim

the executor **must** provide a self-contained Invocation sufficient for the receiving context **to** perform the admitted Action **without** remembering the Workflow procedure from earlier conversation.

- identify the Workflow Run **and** Step Run, exact admitted definition bindings, bound inputs **or** accessible references, relevant prior results **and** actual effects, applicable permissions, **and** required output.
- provide the instruction derived from the Action **and** its Step binding, including how **to** return the result **or** request missing input. the instruction is a derived presentation of governing authority, **not** another independently maintained procedure.
- an Integrated Invocation returns this context **and** instruction through the session interface; an Isolated Invocation supplies it **to** the separate context. no particular transport is required by this core rule.

## Details
