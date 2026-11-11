---
atom_id: CA-R-1792
ref_id: CA-R-1792
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Action).Execution Kind'
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Journal
tier: 2
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1792-CORE_META_MODEL-RULE--preserve-terminal-workflow-handoff-approval-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Preserve terminal Workflow handoff approval boundaries

## Claim

### Prose Claim


a terminal Workflow handoff from an Agentic Step Invocation.


a terminal Workflow handoff **must** end the predecessor Run **and** let the executor admit a separate successor under `CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results`. a session instruction **must not** silently resume an ended Run **or** bypass approval.
