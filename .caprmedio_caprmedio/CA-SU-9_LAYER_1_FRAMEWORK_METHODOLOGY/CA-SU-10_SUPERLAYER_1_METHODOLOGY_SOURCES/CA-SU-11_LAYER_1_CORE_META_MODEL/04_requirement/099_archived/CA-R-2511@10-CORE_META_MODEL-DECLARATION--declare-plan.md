---
atom_id: CA-R-2511
ref_id: CA-R-2511@10
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 3
status: Archived
version: 10
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-2511@10-CORE_META_MODEL-DECLARATION--declare-plan.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
---

## Summary

Declare Atom/(.Role := Plan)

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Role :: Plan;

Atom/(.Header.Role in (Plan)) >| (Container == yes);

Atom/(.Header.Role in (Plan));

# instances
Atom/(.Header.Role in (Plan))//$plan {::0+}((CONTAINS)) Atom/(.Header.Role in (Plan))//$contained_plan;

Atom/(.Header.Role in (Plan))//$dependent {::0+}((IS_BLOCKED_BY)) Atom/(.Header.Role in (Plan))//$prerequisite;

Atom/(.Header.Role in (Plan))//$prerequisite_2 {::0+}((BLOCKS)) Atom/(.Header.Role in (Plan))//$dependent_2;

FOR EACH $atom[<Atom>, (.Header.Role = Plan)]:
(
    IF (($atom.Header.Status = Active) AND ($atom.Header.Work Sequence Number{=1}))
    THEN ($atom.Header.Container{==1})
)
```

## Semantics

A Plan describes intended work, an intended outcome or its execution record. Work Report is the Form for that execution record.
