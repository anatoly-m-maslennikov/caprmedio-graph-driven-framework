---
atom_id: CA-R-2712
ref_id: CA-R-2712@4
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
tier: 3
status: Archived
version: 4
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2712@4-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-work-sequence-number.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.Work Sequence Number

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Plan).Header.Work Sequence Number:: [int]{::0..1};

Atom/(.Header.Role: Plan).Header.Work Sequence Number.*[]{::0};

# instances
Atom/(.Header.Role: Plan)//$atom;

IF ($atom.Header.Work Sequence Number{=1})
THEN ($atom.Header.Work Sequence Number > 0);

UNIQUE(
  Atom/(.Header.Role: Plan)//$atom_2,
  (.Header.Container.atom, .Header.Work Sequence Number),
  (.Header.Status = Active) AND (.Header.Work Sequence Number{=1}) AND (.Header.Container.atom{=1})
);

UNIQUE(
  Atom/(.Header.Role: Plan)//$atom_3,
  (.Header.Container.scope_unit, .Header.Work Sequence Number),
  (.Header.Status = Active) AND (.Header.Work Sequence Number{=1}) AND (.Header.Container.scope_unit{=1})
)
```
