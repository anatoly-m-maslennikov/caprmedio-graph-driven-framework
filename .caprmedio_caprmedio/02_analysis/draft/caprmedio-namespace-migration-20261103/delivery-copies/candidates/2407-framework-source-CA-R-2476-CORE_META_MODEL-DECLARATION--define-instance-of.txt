---
atom_id: CA-R-2476
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//INSTANCE_OF
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define INSTANCE_OF

## Claim

```CFEL
$instance ((INSTANCE_OF)) $kind;
((INSTANCE_OF)) ((HAS_INVERSE)) ((HAS_INSTANCE));

((INSTANCE_OF)) == //;
((INSTANCE_OF)) >| Derivation == Direct
```

## Semantics

The Host is an instance of the Target declared kind; a Property kind is not independently instantiated.



Forward `Host ((INSTANCE_OF)) Target` and reverse `Target <((INSTANCE_OF)) Host` are views of the same Relation fact.
In `X//Y`, Y INSTANCE_OF X; traversal runs from kind to instance.
INSTANCE_OF relates instance of a declared kind to declared kind.

