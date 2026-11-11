---
atom_id: CA-R-2511
ref_id: CA-R-2511@6-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
tier: 3
status: Draft
version: 6
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-2511@6-draft-DECLARATION--declare-atom-role-plan.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Declare Atom/(.Role := Plan)

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Context.Role :: Plan;

Atom/(.Header.Context.Role in (Plan)) >| (Container == yes);

Atom/(.Header.Context.Role in (Plan));

# instances
Atom/(.Header.Context.Role in (Plan))//$plan {::0+}((CONTAINS)) Atom/(.Header.Context.Role in (Plan))//$contained_plan;

Atom/(.Header.Context.Role in (Plan))//$dependent {::0+}((IS_BLOCKED_BY)) Atom/(.Header.Context.Role in (Plan))//$prerequisite;

Atom/(.Header.Context.Role in (Plan))//$prerequisite_2 {::0+}((BLOCKS)) Atom/(.Header.Context.Role in (Plan))//$dependent_2;

FOR EACH $parent[<Atom>, ((.Header.Context.Role = Plan) AND (.Header.State.Status in (Done, Canceled)))]:
(
    FOR EACH $descendant[<Atom>, ((.Header.Context.Role = Plan) AND (.Header.State.Status >| Status Group = Current))]:
    (
        IF ($parent ((RECURSIVELY_CONTAINS)) $descendant)
        THEN ($descendant.Header.State.Status :: [in (Done, Canceled)]{::1})
    )
)
```

## Semantics

A Plan describes bounded intended work or an intended outcome.
