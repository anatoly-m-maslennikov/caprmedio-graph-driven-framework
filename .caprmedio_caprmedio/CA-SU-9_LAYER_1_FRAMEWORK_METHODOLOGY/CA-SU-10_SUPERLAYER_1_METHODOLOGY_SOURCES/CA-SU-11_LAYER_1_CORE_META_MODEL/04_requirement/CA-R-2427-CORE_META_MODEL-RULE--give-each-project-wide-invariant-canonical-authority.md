---
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2426
subjects:
  active: CAPRMEDIO_MODEL <+ Project
  passive:
  - CAPRMEDIO_MODEL <+ Project
atom_id: CA-R-2427
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Give each Project-wide invariant canonical authority

## Claim scope

Project-wide foundational invariants.

## Claim

Every Project-wide foundational invariant must have exactly one active Project-owned Tier `0` Atom as its canonical authority owner. One such Atom may own several related invariants; this does not require one Atom per invariant or one Tier `0` Atom for the Project. Faithful specialization does not create independent duplicate authority.
