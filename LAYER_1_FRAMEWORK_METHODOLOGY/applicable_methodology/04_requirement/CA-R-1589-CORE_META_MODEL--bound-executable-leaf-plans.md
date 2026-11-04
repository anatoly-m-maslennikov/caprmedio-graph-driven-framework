---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1589
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1589-CORE_META_MODEL--bound-executable-leaf-plans.md
  source_atom_id: CA-R-1589
  source_atom_revision: 24
  source_sha256: f19e0124a094114cc37d11723aaac33ca3e2929778e4fbfffed2f0b81177f0ce
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bound executable leaf Plans

## Claim

### Prose Claim


executable Plans with **none** directly contained Plan Atoms.


**every** executable Plan with **none** directly contained Plan Atoms **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a Plan with contained children **may** have a larger roll-up estimate. the rule applies independently of Label.
