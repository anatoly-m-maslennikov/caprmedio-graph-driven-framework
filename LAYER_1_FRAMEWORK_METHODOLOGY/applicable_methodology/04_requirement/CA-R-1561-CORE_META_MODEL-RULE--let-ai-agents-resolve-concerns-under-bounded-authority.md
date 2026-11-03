---
subjects:
  active: Entity/Object/Continuant/Actor/AI Agent
  passive:
  - Entity/Object/Continuant/Actor/AI Agent
  - Atom/(.Role := Concern)
  - Atom
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
version: 28
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-846
  - CA-R-2158
atom_id: CA-R-1561
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1561-CORE_META_MODEL-RULE--let-ai-agents-resolve-concerns-under-bounded-authority.md
  source_atom_id: CA-R-1561
  source_atom_revision: 28
  source_sha256: beaae4014dd7fa495cb2c57b940ad0b8c66502730a79065af040fb304785d13f
  original_relations_sha256: af574ef6cc9f70a0e3208d8edf3eb5d463694adc224f444c2c998dbbf30fa88a
---
## Summary

Let AI Agents resolve Concerns under bounded authority

## Claim scope

AI Agent resolution of Concerns under active delegated authority.

## Claim

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.
