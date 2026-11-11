---
atom_id: CA-R-1580
ref_id: CA-R-1580
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//BLOCKS
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status: Done'
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
tier: 1
status: Active
version: 29
updated_at: 2026-11-04 16:52:59 +0400
carrier_destination:
  file:
    name: CA-R-1580-DECLARATION--define-plan-blocking.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Plan blocking

## Claim

### Formal Claim

```CFEL
# model
Relation//BLOCKS <((HAS_INVERSE)) Relation//IS_BLOCKED_BY;

Relation//BLOCKS ((HAS_CLASSIFICATION)) Derivation == Derived;

# instances
Atom/(.Header.Context.Role: Plan)//$prerequisite ((BLOCKS)) Atom/(.Header.Context.Role: Plan)//$dependent
```

## Semantics

BLOCKS relates a prerequisite Plan to a dependent Plan that may start only after that prerequisite is Done.
