---
atom_id: CA-R-2520@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
version: 3
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.Work Sequence Number

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Plan).Header.Work Sequence Number{:0..1}: [int]{:1};
Atom/(.Header.Role: Plan).Header.Work Sequence Number.*[]{:0};
IF (Atom/(.Header.Role: Plan).Header.Work Sequence Number{=1})
THEN (Atom/(.Header.Role: Plan).Header.Work Sequence Number > 0);
UNIQUE(
  Atom/(.Header.Role: Plan)//,
  (.Header.Relations.IS_CONTAINED_BY.atom, .Header.Work Sequence Number),
  (.Header.Status = Active) AND (.Header.Work Sequence Number{=1}) AND (.Header.Relations.IS_CONTAINED_BY.atom{=1})
);
UNIQUE(
  Atom/(.Header.Role: Plan)//,
  (.Header.Relations.IS_CONTAINED_BY.scope_unit, .Header.Work Sequence Number),
  (.Header.Status = Active) AND (.Header.Work Sequence Number{=1}) AND (.Header.Relations.IS_CONTAINED_BY.scope_unit{=1})
)
```
