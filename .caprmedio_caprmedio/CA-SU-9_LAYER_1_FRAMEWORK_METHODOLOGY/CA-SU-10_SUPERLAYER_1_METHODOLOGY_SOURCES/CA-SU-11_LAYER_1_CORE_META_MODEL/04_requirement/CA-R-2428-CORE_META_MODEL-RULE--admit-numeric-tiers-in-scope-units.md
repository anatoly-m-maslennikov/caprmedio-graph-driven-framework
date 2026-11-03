---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Tier
relations:
  child_of:
  - CA-R-917
version: 2
updated_at: 2026-11-02 00:18:22 +0400
atom_id: CA-R-2428
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Active
role: Requirement
form: Rule
---
## Summary

Admit Numeric Tiers in Scope Units

## Claim scope

ordinary Atoms owned by Scope Units in the Project.

## Claim

a Scope Unit in the Project **must** admit an integer Tier **>=0** for every ordinary Atom it owns. The explicit Project Goal case carries Tier `-1` under CA-R-2132. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.
