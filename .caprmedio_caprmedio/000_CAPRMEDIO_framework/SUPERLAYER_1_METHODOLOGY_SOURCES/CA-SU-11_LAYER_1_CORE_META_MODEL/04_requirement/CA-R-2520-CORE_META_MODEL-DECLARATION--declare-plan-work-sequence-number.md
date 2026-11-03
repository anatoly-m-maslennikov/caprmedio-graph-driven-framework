---
atom_id: CA-R-2520
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Role := Plan).Work Sequence Number

## Claim

```CFEL
Atom/(.Role: Plan).Work Sequence Number{:0..1}: [int]{:1};
Atom/(.Role: Plan).Work Sequence Number.*[]{:0};
IF (Atom/(.Role: Plan).Work Sequence Number{=1})
THEN (Atom/(.Role: Plan).Work Sequence Number > 0);
UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.atom, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.atom{=1})
);
UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.scope_unit, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.scope_unit{=1})
)
```
