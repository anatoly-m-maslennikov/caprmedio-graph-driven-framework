---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  passive:
  - CAPRMEDIO_MODEL <+ Package/Implementation
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-933
atom_id: CA-R-954
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Requirement
form: Rule
---
## Summary
Target one Implementation result with each Demand

## Claim

### Prose Claim


Demand Atoms.


**every** Demand Atom **must** constrain **`=1`** Implementation result produced by its Claim Scope.
