---
atom_id: CA-R-2546@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header.Subjects.Active

## Claim

### Formal Claim

```CFEL
Atom.Header.Subjects.Active{:0..1}: [string]{:1};
Atom.Header.Subjects.Active.*[]{:0};
IF (Atom.Header.Status >| Status Group = Current)
THEN (Atom.Header.Subjects.Active{==1})
```
