---
atom_id: CA-R-2766
ref_id: CA-R-2766
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//SPECIALIZES
tier: 1
status: Active
version: 2
updated_at: 2026-11-04 19:46:41 +0400
carrier_destination:
  file:
    name: CA-R-2766-DECLARATION--declare-specializes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare SPECIALIZES

## Claim

### Prose Claim

The child Atom's Claim is more specific or stricter than the parent Atom's Claim in the same or a narrower Scope and preserves the parent's applicable constraints. A conditional specialization is included. A reference or dependency alone does not establish SPECIALIZES.

### Formal Claim

```CFEL
# model
Relation//SPECIALIZES ((HAS_INVERSE)) Relation//IS_SPECIALIZED_BY;

Relation//SPECIALIZES ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$child ((SPECIALIZES)) Atom//$parent
```

## Semantics

SPECIALIZES relates a child Atom to the Atom whose Claim it specializes.
