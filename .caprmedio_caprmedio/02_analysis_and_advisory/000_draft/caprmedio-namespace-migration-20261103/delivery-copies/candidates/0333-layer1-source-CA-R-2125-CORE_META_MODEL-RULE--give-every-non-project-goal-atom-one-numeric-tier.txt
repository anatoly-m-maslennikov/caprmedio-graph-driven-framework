---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
version: 10
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-2125
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Active
role: Requirement
form: Rule
---
## Summary
Give Every Non-Project-Goal Atom One Numeric Tier

## Claim scope
Atom other than a Project Goal Atom.

## Claim

**every** non-Project-Goal Atom **must** carry exactly one integer Tier. An ordinary Atom owned by a Scope Unit uses an integer Tier **>=0**. Project Goal is the separate explicit Tier `-1` case under CA-R-2132.

This rule defines owner-relative ranges, not a finite set of values. Higher integers remain admissible and may be assigned or raised when required by the approved governing-relation ordering. No Content-Role or Type-to-Tier restriction is imposed.
