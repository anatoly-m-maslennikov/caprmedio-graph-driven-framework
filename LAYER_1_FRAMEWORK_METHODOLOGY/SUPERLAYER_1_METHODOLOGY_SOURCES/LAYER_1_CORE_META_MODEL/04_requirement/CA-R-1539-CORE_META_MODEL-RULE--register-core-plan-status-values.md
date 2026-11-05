---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1539
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Register Core Plan Status Values

## Claim

### Prose Claim


Core Plan Status values.


the Core Plan Status model **must** inherit the allowed values of Atom.Header.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.
