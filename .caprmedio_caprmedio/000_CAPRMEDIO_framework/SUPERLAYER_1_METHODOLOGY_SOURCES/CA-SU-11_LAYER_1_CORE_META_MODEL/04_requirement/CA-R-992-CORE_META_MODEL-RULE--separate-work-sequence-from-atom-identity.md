---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
version: 36
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2712
atom_id: CA-R-992
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Separate Work Sequence from Atom identity

## Claim

### Prose Claim


Work Sequence Numbers **and** Atom identity-related properties.


a Work Sequence Number **must not** establish **or** change Atom identity, Atom Scope, Claim Target Scope Unit, Type, authoring Subtype, decomposition, **or** blocking.
