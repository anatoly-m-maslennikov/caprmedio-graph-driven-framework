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
