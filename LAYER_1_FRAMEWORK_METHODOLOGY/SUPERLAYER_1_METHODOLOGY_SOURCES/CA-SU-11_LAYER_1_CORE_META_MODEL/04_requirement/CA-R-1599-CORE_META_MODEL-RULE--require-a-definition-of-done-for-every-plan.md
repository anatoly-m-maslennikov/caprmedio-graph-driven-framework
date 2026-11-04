---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content.Definition of Done'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1599
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Require a Definition of Done for every Plan

## Claim

### Prose Claim


Plan Atoms, including Hubs with no own work.


**every** Plan Atom **must** have **`=1`** Definition of Done, including a Hub with no own work.
