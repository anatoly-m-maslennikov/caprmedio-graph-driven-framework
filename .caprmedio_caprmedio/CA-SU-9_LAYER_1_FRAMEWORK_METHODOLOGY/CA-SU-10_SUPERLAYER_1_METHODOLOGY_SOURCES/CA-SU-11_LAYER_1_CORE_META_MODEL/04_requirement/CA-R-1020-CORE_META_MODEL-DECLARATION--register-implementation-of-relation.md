---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//implementation_of
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 30
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
atom_id: CA-R-1020
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1020-CORE_META_MODEL-DECLARATION--register-implementation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Register implementation_of relation

## Claim

### Formal Claim

```CFEL
Relation//implementation_of ((HAS_CLASSIFICATION)) Derivation == Direct;

$implementation_carrier ((implementation_of)) Atom//
```

### Prose Claim

#### Applicability
the `implementation_of` direct relation owned by a governed Implementation carrier.

`implementation_of` **means** the direct relation from an Implementation
carrier to the specification Atom that it implements.

The Host is an Implementation carrier; the target is the specification Atom it implements.
Forward `Host ((implementation_of)) Target` and reverse `Target <((implementation_of)) Host` are views of the same Relation fact.
implementation_of relates Implementation carrier to specification Atom.
