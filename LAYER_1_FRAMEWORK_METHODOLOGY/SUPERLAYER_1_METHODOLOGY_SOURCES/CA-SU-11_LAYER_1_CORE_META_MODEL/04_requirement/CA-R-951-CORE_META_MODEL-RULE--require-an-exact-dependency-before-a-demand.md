---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  passive:
  - CAPRMEDIO_MODEL <+ Atom
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-933
atom_id: CA-R-951
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Requirement
form: Rule
---
## Summary
Require an exact dependency before a Demand

## Claim

### Prose Claim


Consumer Scope Units with an accepted Goal.


a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.
