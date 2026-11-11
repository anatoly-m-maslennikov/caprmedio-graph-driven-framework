---
atom_id: CA-R-2511
ref_id: CA-R-2511@9
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 3
status: Archived
version: 9
updated_at: 2026-11-08 19:06:46 +0400
carrier_destination:
  file:
    name: CA-R-2511@9-CORE_META_MODEL-DECLARATION--declare-plan.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
---

## Summary

Declare Atom/(.Role := Plan)

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Plan) >| (Container == yes);

Atom/(.Header.Role: Plan);

# instances
Atom/(.Header.Role: Plan)//$plan {::0+}((CONTAINS)) Atom/(.Header.Role: Plan)//$contained_plan;

Atom/(.Header.Role: Plan)//$dependent {::0+}((IS_BLOCKED_BY)) Atom/(.Header.Role: Plan)//$prerequisite;

Atom/(.Header.Role: Plan)//$prerequisite_2 {::0+}((BLOCKS)) Atom/(.Header.Role: Plan)//$dependent_2;

Atom/(.Header.Role: Plan)//$atom;

IF (($atom.Header.Status = Active) AND ($atom.Header.Work Sequence Number{=1}))
THEN ($atom.Header.Container{==1})
```

## Semantics

A Plan describes intended work, an intended outcome or its execution record. Work Report is the Form for that execution record.
