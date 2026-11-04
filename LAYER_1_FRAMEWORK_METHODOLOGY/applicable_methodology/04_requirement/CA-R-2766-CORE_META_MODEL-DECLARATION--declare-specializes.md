---
atom_id: CA-R-2766
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//SPECIALIZES
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
version: 2
updated_at: 2026-11-04 19:46:41 +0400
carrier_destination:
  file:
    name: CA-R-2766-CORE_META_MODEL-DECLARATION--declare-specializes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2766-CORE_META_MODEL-DECLARATION--declare-specializes.md
  source_atom_id: CA-R-2766
  source_atom_revision: 2
  source_sha256: 9ff42b4c80c6fd56cdb208661b1dbeb899e32bf061a13f3f3de183967259282c
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---

## Summary

Declare SPECIALIZES

## Claim

### Formal Claim

```CFEL
# model
Relation//SPECIALIZES ((HAS_INVERSE)) Relation//IS_SPECIALIZED_BY;

Relation//SPECIALIZES ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$child ((SPECIALIZES)) Atom//$parent
```

### Prose Claim

The child Atom's Claim is more specific or stricter than the parent Atom's Claim in the same or a narrower Scope and preserves the parent's applicable constraints. A conditional specialization is included. A reference or dependency alone does not establish SPECIALIZES.

## Semantics

SPECIALIZES relates a child Atom to the Atom whose Claim it specializes.
