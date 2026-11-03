---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//concern_about
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 32
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
atom_id: CA-R-1022
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1022-CORE_META_MODEL-DECLARATION--register-concern-about-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Register concern_about relation

## Claim

### Formal Claim

```CFEL
# model
Relation//concern_about ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: Concern)//$atom ((concern_about)) $governed
```

### Prose Claim

#### Applicability
`concern_about` relations.

`concern_about` **means** the direct relation from a Concern Atom to the
governed entity that it concerns.

The Host is a Concern Atom; the governed target is the Entity concerned.
Forward `Host ((concern_about)) Target` and reverse `Target <((concern_about)) Host` are views of the same Relation fact.
concern_about relates Concern Atom to governed entity concerned.

#### Details
Endpoint admission is an Atom Entity Definition concern, not Relation Definition
metadata.
