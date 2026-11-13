---
atom_id: CA-R-3001
ref_id: CA-R-3001@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTRIBUTES_TO
tier: 3
status: archived
version: 2
updated_at: 2026-11-07 15:18:44 +0400
carrier_destination:
  file:
    name: CA-R-3001@2-CORE_META_MODEL-DECLARATION--declare-contributes-to.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare CONTRIBUTES_TO

## Claim

### Formal Claim

```CFEL
# model
Relation//CONTRIBUTES_TO ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$contributor ((CONTRIBUTES_TO)) Atom//$contribution
```

## Semantics

The Host contributes toward the Target. Contribution is distinct from verified satisfaction of a Requirement.
