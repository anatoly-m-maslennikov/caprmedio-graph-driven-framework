---
subjects:
  active: Entity/Object/Continuant/Actor/AI Agent
  passive:
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Object/Continuant/Actor/Operator
  - Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
version: 23
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-1713
atom_id: CA-R-1555
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1555-CORE_META_MODEL--govern-ca-execution-gates.md
  source_atom_id: CA-R-1555
  source_atom_revision: 23
  source_sha256: 1730640b34268355fe1a9bdf642522fa9044c82fd6faec19863719f8006edbe0
  original_relations_sha256: 47a017ddc25d777e9a3d23993aebbd24381f2642f26fda3d06692854c0d4808a
---
## Summary
Govern CA execution gates

## Claim scope
identified AI Agents considering clarification omission under applicable configured confidence requirements.

## Claim

an identified AI Agent **may** omit clarification **only** **when** confidence **in** **every** following item meets its applicable configured requirement:

- intent;
- scope;
- route;
- entry criteria.

confidence **must not** create delegated authority **or** bypass per-action Operator approval **when** active authority requires it.
