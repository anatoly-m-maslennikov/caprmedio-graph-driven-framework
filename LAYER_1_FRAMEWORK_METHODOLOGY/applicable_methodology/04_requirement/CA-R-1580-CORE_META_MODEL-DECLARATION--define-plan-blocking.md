---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//BLOCKS
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Done'
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
version: 27
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
atom_id: CA-R-1580
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
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
  source_atom_revision: 27
  source_sha256: 19ecfd4058ac41328bd6d995963a8f3e6f6e3b10ed1bb5ce84834d4ff65a390f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Plan blocking

## Claim

### Formal Claim

```CFEL
# model
Relation//BLOCKS ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Plan//$plan ((BLOCKS)) Plan//$plan_2;
```

### Prose Claim

#### Applicability
Plan-blocking Relations in the Plan Graph.

**in** the Plan Graph, `A BLOCKS B` **means** that Plan `B` may start only
after Plan `A` is Done. An inverse lookup is derived from the same explicit
fact and is not separately authored; Subject DEPENDS_ON remains distinct.

Forward `Host ((BLOCKS)) Target` and reverse `Target <((BLOCKS)) Host` are views of the same Relation fact.
BLOCKS relates prerequisite Plan to dependent Plan.

#### Details
Plan endpoint admission, status, cardinality, authority and reachability belong
to the Plan Entity Definition CA-R-2511.
