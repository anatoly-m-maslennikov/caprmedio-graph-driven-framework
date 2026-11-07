---
atom_id: CA-R-3001
ref_id: CA-R-3001@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTRIBUTES_TO
tier: 3
status: Draft
version: 1
updated_at: "2026-11-07 14:23:30 +0400"
carrier_destination:
  file:
    name: CA-R-3001@1-draft-CORE_META_MODEL-DECLARATION--declare-contributes-to.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
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
