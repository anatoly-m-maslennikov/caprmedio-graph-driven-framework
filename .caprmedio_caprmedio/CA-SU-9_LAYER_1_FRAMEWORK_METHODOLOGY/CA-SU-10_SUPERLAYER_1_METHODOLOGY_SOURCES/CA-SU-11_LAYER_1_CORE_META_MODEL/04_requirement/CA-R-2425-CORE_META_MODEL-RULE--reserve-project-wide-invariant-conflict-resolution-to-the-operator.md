---
atom_id: CA-R-2425
ref_id: CA-R-2425
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Actor
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
tier: 1
relations:
  child_of:
  - CA-R-1058
status: Active
version: 4
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-2425-CORE_META_MODEL-RULE--reserve-project-wide-invariant-conflict-resolution-to-the-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Reserve Project-wide invariant conflict resolution to the Operator

## Claim

### Prose Claim


conflicts between active Project-wide foundational invariants **and** an AI Agent's delegated conflict resolution.


- **only** an Operator **may** resolve a conflict between active Project-wide foundational invariants, **and** an Operator's decision to resolve that conflict is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for a conflict between active Project-wide foundational invariants but **must not** choose a resolution for a conflict between active Project-wide foundational invariants.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project-wide foundational invariants **only** **when** the AI Agent's active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.
