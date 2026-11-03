---
atom_id: CA-R-2493
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.ID
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.ID

## Claim

```CFEL
Atom.ID{:1}: [string]{:1};
Atom.ID.*[]{:0};
IF ((Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived))
THEN (IMMUTABLE(Atom.ID))
```
