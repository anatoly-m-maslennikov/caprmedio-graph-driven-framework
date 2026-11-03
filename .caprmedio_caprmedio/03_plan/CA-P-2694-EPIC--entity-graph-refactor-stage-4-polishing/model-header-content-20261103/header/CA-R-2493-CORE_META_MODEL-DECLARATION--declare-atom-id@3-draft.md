---
atom_id: CA-R-2493@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.ID
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header.ID

## Claim

### Formal Claim

```CFEL
Atom.Header.ID{:1}: [string]{:1};
Atom.Header.ID.*[]{:0};
IF ((Atom.Header.Status >| Status Group = Current) OR (Atom.Header.Status >| Status Group = Archived))
THEN (IMMUTABLE(Atom.Header.ID))
```
