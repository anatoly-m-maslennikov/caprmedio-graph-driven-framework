---
subjects:
  active: Entity/Object/Continuant/Actor/AI Agent
  passive:
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent.Permissions
  - Atom/(.Role := Concern)
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1702
atom_id: CA-R-1557
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1557-CORE_META_MODEL-RULE--keep-conflict-discovery-in-exploration-mode.md
  source_atom_id: CA-R-1557
  source_atom_revision: 21
  source_sha256: b8bb46673306a0d38b8ddb6bc4daa8bc39e50b1769769df2c9a1a8e58fc9fcc2
  original_relations_sha256: 86f48d79fbbfe66ffab2b0bb686a446bbbe206535c96d6e0d3b25f21670f9677
---
## Summary

Keep conflict discovery in Exploration Mode

## Claim scope

AI Agent discovery of conflicts in Exploration Mode.

## Claim

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.
