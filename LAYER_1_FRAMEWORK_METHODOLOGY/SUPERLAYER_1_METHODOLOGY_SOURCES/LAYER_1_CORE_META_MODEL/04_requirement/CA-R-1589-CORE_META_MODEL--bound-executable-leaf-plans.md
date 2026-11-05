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
---
## Summary

Bound executable leaf Plans

## Claim

### Prose Claim


executable Plans with **none** directly contained Plan Atoms.


**every** executable Plan with **none** directly contained Plan Atoms **must** bound its own work **to** an estimate of **<=15** minutes for **=1** assigned AI Agent, with sufficient inputs, required output, verification, **and** no unresolved Operator decision; a Plan with contained children **may** have a larger roll-up estimate. the rule applies independently of Label.
