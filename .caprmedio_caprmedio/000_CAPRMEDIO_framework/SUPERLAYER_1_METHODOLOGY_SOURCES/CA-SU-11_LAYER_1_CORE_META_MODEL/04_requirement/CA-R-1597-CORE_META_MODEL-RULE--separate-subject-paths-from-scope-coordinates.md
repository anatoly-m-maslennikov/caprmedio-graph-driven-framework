---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
version: 20
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1597
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Separate Subject Paths from Scope Coordinates

## Claim

### Prose Claim


an Atom's Subject Paths.


an Atom's Subject Paths **must** identify the Subject Targets of its Subject Relations **without** substituting those paths for its owning Scope Unit **or** its Claim Target Scope Unit.
