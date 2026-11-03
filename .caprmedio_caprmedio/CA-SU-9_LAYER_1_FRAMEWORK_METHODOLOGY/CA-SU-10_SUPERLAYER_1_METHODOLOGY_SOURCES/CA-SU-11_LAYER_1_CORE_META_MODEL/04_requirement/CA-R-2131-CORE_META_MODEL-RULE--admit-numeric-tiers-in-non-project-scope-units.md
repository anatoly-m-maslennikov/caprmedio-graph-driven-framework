---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Tier
version: 10
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-2131
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Active
role: Requirement
form: Rule
---
## Summary

Admit Numeric Tiers in Non-Project Scope Units

## Claim scope

ordinary Atoms owned by non-Project Scope Units.

## Claim

a non-Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.
