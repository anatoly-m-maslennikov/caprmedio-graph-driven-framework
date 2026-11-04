---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//BLOCKS
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Done'
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
version: 29
updated_at: 2026-11-04 16:52:59 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-1580
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1580-CORE_META_MODEL-DECLARATION--define-plan-blocking.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1580-CORE_META_MODEL-DECLARATION--define-plan-blocking.md
  source_atom_id: CA-R-1580
  source_atom_revision: 29
  source_sha256: 25e9d08d3851209230e686a23c42d7819f3fddd4b163d3e18947c6b6eedb8ae5
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
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
Atom/(.Header.Role: Plan)//$prerequisite ((BLOCKS)) Atom/(.Header.Role: Plan)//$dependent
```

## Semantics

BLOCKS relates a prerequisite Plan to a dependent Plan that may start only after that prerequisite is Done.
