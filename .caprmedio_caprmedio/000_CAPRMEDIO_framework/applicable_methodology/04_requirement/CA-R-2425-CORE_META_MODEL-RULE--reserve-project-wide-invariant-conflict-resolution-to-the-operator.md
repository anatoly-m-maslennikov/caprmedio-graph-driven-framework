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
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization"
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2425-CORE_META_MODEL-RULE--reserve-project-wide-invariant-conflict-resolution-to-the-operator.md
  source_atom_id: CA-R-2425
  source_atom_revision: 4
  source_sha256: 2bdae32e06fe10f9dabba603d97cc3df1055093c29ac1d34a17863abd13353d5
  original_relations_sha256: f9577d5716dcc9ccd23bd52379396798c3999355ced857a5e1cb469ad88f2b5d
---
## Summary

Reserve Project-wide invariant conflict resolution to the Operator

## Claim

### Prose Claim


conflicts between active Project-wide foundational invariants **and** an AI Agent's delegated conflict resolution.


- **only** an Operator **may** resolve a conflict between active Project-wide foundational invariants, **and** an Operator's decision to resolve that conflict is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for a conflict between active Project-wide foundational invariants but **must not** choose a resolution for a conflict between active Project-wide foundational invariants.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project-wide foundational invariants **only** **when** the AI Agent's active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.
