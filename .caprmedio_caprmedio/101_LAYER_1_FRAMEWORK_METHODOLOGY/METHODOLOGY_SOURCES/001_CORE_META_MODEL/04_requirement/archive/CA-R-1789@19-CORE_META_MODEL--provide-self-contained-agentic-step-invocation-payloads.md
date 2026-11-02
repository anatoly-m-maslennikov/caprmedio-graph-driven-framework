---
subjects:
  governs: Entity/Object/Occurrent/Execution/Step Run.Invocation Context
  depends_on:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind'
  - Entity/Object/Occurrent/Execution/Step Run.Execution Context
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/History/Journal
version: 19
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1789@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Provide self-contained Agentic Step Invocation payloads

## Claim scope

an executor dispatching **or** resuming an Agentic Step.

## Claim

the executor **must** provide a self-contained Invocation sufficient for the receiving context **to** perform the admitted Action **without** remembering the Workflow procedure from earlier conversation.

- identify the Workflow Run **and** Step Run, exact admitted definition bindings, bound inputs **or** accessible references, relevant prior results **and** actual effects, applicable permissions, **and** required output.
- provide the instruction derived from the Action **and** its Step binding, including how **to** return the result **or** request missing input. the instruction is a derived presentation of governing authority, **not** another independently maintained procedure.
- an Integrated Invocation returns this context **and** instruction through the session interface; an Isolated Invocation supplies it **to** the separate context. no particular transport is required by this core rule.
