---
atom_id: CA-R-1993
ref_id: CA-R-1993
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CARRIES
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
relations:
  child_of:
  - CA-R-1174
version: 20
updated_at: 2026-11-03 20:00:05 +0400
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1993-CORE_META_MODEL-DECLARATION--define-carries.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Define CARRIES

## Claim

### Formal Claim

```CFEL
# model
Relation//CARRIES ((HAS_INVERSE)) Relation//IS_CARRIED_BY;

Relation//CARRIES ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Carrier//$carrier ((CARRIES)) $represented_entity
```

### Prose Claim

#### Claim scope
Carrier bindings of non-ephemeral Entities.

CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.

The Target is the non-ephemeral Entity stored or represented by the Carrier.
Forward `Host ((CARRIES)) Target` and reverse `Target <((CARRIES)) Host` are views of the same Relation fact.
CARRIES relates Carrier to non-ephemeral Entity.

#### Details
IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity to its Carrier. The Carrier binding exposes this inverse direction; it is not a separately authored primitive Relation fact. This preserves the existing meaning defined by CA-D-257. Neither direction requires a separately registered binding for each YAML field or Markdown section, a new Carrier, a snapshot or a historical record. The applicable D policy specifies how the represented Entity is bound and represented. No additional endpoint class, graph ownership, cardinality or inference permission is introduced by moving this definition to R.
