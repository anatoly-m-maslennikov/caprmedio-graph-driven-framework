---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Actor
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
version: 4
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-1058
atom_id: CA-R-2425
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2425-CORE_META_MODEL-RULE--reserve-project-wide-invariant-conflict-resolution-to-the-operator.md
  source_atom_id: CA-R-2425
  source_atom_revision: 4
  source_sha256: 4d8c8bb9598c09cbe8f7942ee8c64b6d1eb2bf4443179bbcb99054e2144a0c32
  original_relations_sha256: f9577d5716dcc9ccd23bd52379396798c3999355ced857a5e1cb469ad88f2b5d
---
## Summary

Reserve Project-wide invariant conflict resolution to the Operator

## Claim scope

conflicts between active Project-wide foundational invariants **and** an AI Agent's delegated conflict resolution.

## Claim

- **only** an Operator **may** resolve a conflict between active Project-wide foundational invariants, **and** an Operator's decision to resolve that conflict is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for a conflict between active Project-wide foundational invariants but **must not** choose a resolution for a conflict between active Project-wide foundational invariants.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project-wide foundational invariants **only** **when** the AI Agent's active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.
