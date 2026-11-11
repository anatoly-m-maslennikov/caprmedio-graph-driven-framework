---
atom_id: CA-R-1789
ref_id: CA-R-1789
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Invocation Context
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Action).Execution Kind'
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Journal
tier: 2
status: Active
version: 21
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1789-CORE_META_MODEL-RULE--provide-self-contained-agentic-step-invocation-payloads.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Provide self-contained Agentic Step Invocation payloads

## Claim

### Prose Claim


an executor dispatching **or** resuming an Agentic Step.


the executor **must** provide a self-contained Invocation sufficient for the receiving context **to** perform the admitted Action **without** remembering the Workflow procedure from earlier conversation.

- identify the Workflow Run **and** Step Run, exact admitted definition bindings, bound inputs **or** accessible references, relevant prior results **and** actual effects, applicable permissions, **and** required output.
- provide the instruction derived from the Action **and** its Step binding, including how **to** return the result **or** request missing input. the instruction is a derived presentation of governing authority, **not** another independently maintained procedure.
- an Integrated Invocation returns this context **and** instruction through the session interface; an Isolated Invocation supplies it **to** the separate context. no particular transport is required by this core rule.
