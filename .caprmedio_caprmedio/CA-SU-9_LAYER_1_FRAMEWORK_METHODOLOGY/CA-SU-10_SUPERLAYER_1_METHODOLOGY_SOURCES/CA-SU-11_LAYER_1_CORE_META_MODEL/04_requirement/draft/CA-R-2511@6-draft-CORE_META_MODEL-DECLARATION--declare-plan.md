---
atom_id: CA-R-2511
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
version: 6
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-05 03:53:43 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2511@6-draft-CORE_META_MODEL-DECLARATION--declare-plan.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
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

Atom/(.Header.Role: Plan)//$dependent {:0+}((IS_BLOCKED_BY)) Atom/(.Header.Role: Plan)//$prerequisite;

Atom/(.Header.Role: Plan)//$prerequisite_2 {:0+}((BLOCKS)) Atom/(.Header.Role: Plan)//$dependent_2;

```

## Semantics

A Plan describes bounded intended work or an intended outcome.
