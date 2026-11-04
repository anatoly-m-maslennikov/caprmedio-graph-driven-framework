---
atom_id: CA-R-2511
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
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

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Plan);

# instances
Atom/(.Header.Role: Plan)//$atom;

IF (($atom.Header.Status = Active) AND ($atom.Header.Work Sequence Number{=1}))
THEN ($atom.Header.Relations.IS_CONTAINED_BY{==1})
```

## Semantics

A Plan describes bounded intended work or an intended outcome.
