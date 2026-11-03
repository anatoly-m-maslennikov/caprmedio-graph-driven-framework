---
subjects:
  active: CFEL <+ Relation//BLOCKS
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Projection
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status: Done'
  - Atom
  - CFEL > Relation//DEPENDS_ON
version: 26
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1580
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1580-CORE_META_MODEL-DECLARATION--define-plan-blocking.md
  source_atom_id: CA-R-1580
  source_atom_revision: 26
  source_sha256: 2801c8ca2d8ba9962601228e7f0eedc9d4a495602a22ed829ed71d30fe74cfdc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Plan blocking

## Claim scope

Plan-blocking Relations in the Plan Graph.

## Claim

**in** the Plan Graph, `A BLOCKS B` **means** that Plan `B` may start only
after Plan `A` is Done. An inverse lookup is derived from the same explicit
fact and is not separately authored; Subject DEPENDS_ON remains distinct.

```CFEL
Plan// ((BLOCKS)) Plan//;

((BLOCKS)) >| Derivation == Direct
```

## Semantics


Forward `Host ((BLOCKS)) Target` and reverse `Target <((BLOCKS)) Host` are views of the same Relation fact.
BLOCKS relates prerequisite Plan to dependent Plan.

## Details

Plan endpoint admission, status, cardinality, authority and reachability belong
to the Plan Entity Definition CA-R-2511.
