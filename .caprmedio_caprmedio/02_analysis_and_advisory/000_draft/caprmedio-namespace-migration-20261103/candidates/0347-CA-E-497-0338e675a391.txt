---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Invocation Context
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Atom
version: 20
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-M-304
  - CA-R-1789
  - CA-R-1790
  - CA-R-1791
  - CA-R-1792
  - CA-R-1793
atom_id: CA-E-497
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
---
## Summary

Validate self-contained agentic invocations

## Claim scope

an Agentic Step invocation from its supplied context.

## Claim

the Evaluation **must** check that an Agentic Step invocation can be understood **and** resumed from its supplied context **without** remembered Workflow procedure.

## Details

- remove earlier conversation from an Integrated session: the supplied invocation still identifies the requested Action, inputs, evidence, actual effects, authority boundaries, expected result, **and** return route.
- supply the invocation **to** an Isolated context: require the same admitted responsibility **and** constraints rather than implicit access **to** the parent conversation.
- omit required context **or** make a referenced input inaccessible: require a visible missing-input result, **not** guessed execution.
- deliver the same pending invocation again: preserve its identity **and** actual effects; repeated delivery **must not** imply a new Run **or** authorization **to** replay effects.
- provide a prompt that contradicts its bound definition **or** expands permission: reject the instruction even **if** it is self-contained.
- a Step result returns **or** a Workflow hands off: the executor owns the declared routing; a returned prompt alone is **not** Step completion **or** successor completion.

check exact supplied evidence, **not** a claim that the session will remember how **to** proceed.
