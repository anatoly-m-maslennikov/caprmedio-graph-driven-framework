---
atom_id: CA-R-2565
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Workflow
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Preserve Atom Version and Updated At When Archiving

## Claim

When a Workflow archives an Atom:

1. Keep Atom.Version unchanged.
2. Keep Atom.Updated At unchanged.
3. Do not create a new Atom Version solely for archiving.
