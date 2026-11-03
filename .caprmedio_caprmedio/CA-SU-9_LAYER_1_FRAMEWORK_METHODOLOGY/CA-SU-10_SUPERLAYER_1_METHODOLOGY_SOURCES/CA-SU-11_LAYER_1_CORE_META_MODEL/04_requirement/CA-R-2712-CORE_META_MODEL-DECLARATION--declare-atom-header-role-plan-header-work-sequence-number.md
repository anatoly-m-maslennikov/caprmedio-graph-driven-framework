---
atom_id: CA-R-2712
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
version: 1
relations: {}
tier: 3
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2712-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-work-sequence-number.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
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
