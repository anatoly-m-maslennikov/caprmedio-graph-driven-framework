---
atom_id: CA-R-1561
ref_id: CA-R-1561
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization"
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
tier: 2
relations:
  child_of:
  - CA-R-846
  - CA-R-2158
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1561-CORE_META_MODEL-RULE--let-ai-agents-resolve-concerns-under-bounded-authority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Let AI Agents resolve Concerns under bounded authority

## Claim

### Prose Claim


AI Agent resolution of Concerns under active delegated authority.


an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.
