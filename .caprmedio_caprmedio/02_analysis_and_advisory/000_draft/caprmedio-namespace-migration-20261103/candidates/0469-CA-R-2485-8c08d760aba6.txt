---
atom_id: CA-R-2485
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_INVERSE
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define HAS_INVERSE

## Claim

HAS_INVERSE links a direct Relation to its derived inverse. The inverse swaps the direct Relation's Host and Target. Its links are derived from the direct links and are not authored separately.

```CFEL
Relation// ((HAS_INVERSE)) Relation//;

((HAS_INVERSE)) >| Derivation == Direct
```

## Semantics


Forward `Host ((HAS_INVERSE)) Target` and reverse `Target <((HAS_INVERSE)) Host` are views of the same Relation fact.
HAS_INVERSE relates direct Relation to derived inverse Relation.

