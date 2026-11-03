---
atom_id: CA-R-2546
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Subjects.Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Subjects.Active

## Claim

```CFEL
Atom.Subjects.Active{:0..1}: [string]{:1};
Atom.Subjects.Active.*[]{:0};
IF (Atom.Status >| Status Group = Current)
THEN (Atom.Subjects.Active{==1})
```
