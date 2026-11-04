---
atom_id: CA-R-2712
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
version: 3
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-05 03:53:43 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2712@3-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-work-sequence-number.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.Work Sequence Number

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role:=Plan).Header.Work Sequence Number :: [int]{::0..1};

Atom/(.Header.Role:=Plan).Header.Work Sequence Number.*[]{::0};

# instances
Atom/(.Header.Role:=Plan)//$atom;

IF ($atom.Header.Work Sequence Number{=1})
THEN ($atom.Header.Work Sequence Number > 0);

UNIQUE(
  Atom/(.Header.Role:=Plan)//$atom_2,
  (.Header.Container, .Header.Work Sequence Number),
  (.Header.Status = Active) AND (.Header.Work Sequence Number{=1}) AND (.Header.Container{=1})
)
```
