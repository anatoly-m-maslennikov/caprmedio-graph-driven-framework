---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 11
updated_at: 2026-11-04 09:19:08 +0400
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

## Claim

### Prose Claim


ordinary Atoms owned by non-Project Scope Units.


a non-Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns, except an Atom of Form Goal whose active Subject resolves to the Project Scope Unit root. That exact predicate carries Tier `-1` under CA-R-2132 regardless of its Container or owner. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.
