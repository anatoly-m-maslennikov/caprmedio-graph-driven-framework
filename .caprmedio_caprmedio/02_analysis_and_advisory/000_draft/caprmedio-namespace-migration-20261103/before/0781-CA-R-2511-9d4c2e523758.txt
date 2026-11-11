---
atom_id: CA-R-2511
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Plan)
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Role := Plan)

## Claim

```CFEL
Atom/(.Role: Plan);
IF ((Atom/(.Role: Plan).Status = Active) AND (Atom/(.Role: Plan).Work Sequence Number{=1}))
THEN (Atom/(.Role: Plan).Relations.contained_by{==1})
```

## Semantics

A Plan describes bounded intended work or an intended outcome.
