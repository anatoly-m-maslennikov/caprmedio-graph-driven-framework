---
atom_id: CA-R-2511
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
version: 3
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-04 11:00:07 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2511-CORE_META_MODEL-DECLARATION--declare-plan.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2511-CORE_META_MODEL-DECLARATION--declare-plan.md
  source_atom_id: CA-R-2511
  source_atom_revision: 3
  source_sha256: 741bdb16b86ded6ef4c2034e96267b70ed3bd449f1ab116849ed4c92c651f3e2
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
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
Atom/(.Header.Role: Plan)//$plan {:0+}((CONTAINS)) Atom/(.Header.Role: Plan)//$contained_plan;

Atom/(.Header.Role: Plan)//$atom;

IF (($atom.Header.Status = Active) AND ($atom.Header.Work Sequence Number{=1}))
THEN ($atom.Header.Relations.IS_CONTAINED_BY{==1})
```

## Semantics

A Plan describes bounded intended work or an intended outcome.
