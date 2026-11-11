---
atom_id: CA-R-1498
ref_id: CA-R-1498
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RECURSIVELY_CONTAINS
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
tier: 1
status: Active
version: 18
updated_at: '2026-11-11 15:37:01 +0400'
carrier_destination:
  file:
    name: CA-R-1498-CORE_META_MODEL-RELATION_DECLARATION--derive-recursive-containment-from-direct-containment.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Derive Recursive Containment from Direct Containment

## Claim

### Formal Claim

```CFEL
# model
$container ((RECURSIVELY_CONTAINS)) $descendant;

Relation//RECURSIVELY_CONTAINS ((HAS_CLASSIFICATION)) Derivation == Derived
```

## Semantics

The Host recursively contains the Target when one or more successive `CONTAINS` links lead from Host to Target. Intermediate Entities need only satisfy the endpoint constraints of `CONTAINS`. Derive this Relation from the existing links.
