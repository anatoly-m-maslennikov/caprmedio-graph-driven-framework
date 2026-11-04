---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
version: 28
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-037
  - CA-R-1767
atom_id: CA-R-1671
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Permit orphan Implementation Decisions

## Claim

### Prose Claim


orphan permission for an active Eng Decision in strict authority mode.


`eng_decision` **must** be registered as orphan-permitted, so an active Eng Decision **may** have no parent Eng Policy even **in** strict authority mode.

## Details

This Atom-topology permission does not create a local Policy owner at a leaf or justify artificial children; local Eng Policy ownership and child applicability remain governed by CA-R-2119@8 and CA-R-2120@8.
