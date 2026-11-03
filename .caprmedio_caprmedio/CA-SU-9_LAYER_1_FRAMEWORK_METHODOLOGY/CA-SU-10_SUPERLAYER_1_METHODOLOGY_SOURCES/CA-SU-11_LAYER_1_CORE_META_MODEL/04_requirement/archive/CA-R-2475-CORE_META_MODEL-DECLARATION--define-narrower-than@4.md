---
atom_id: CA-R-2475
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define NARROWER_THAN

## Claim

The narrower kind inherits applicable Relation and Property constraints without cloning declarations or instance facts.

```CFEL
$narrower ((NARROWER_THAN)) $broader;
((NARROWER_THAN)) ((HAS_INVERSE)) ((HAS_NARROWER));

((NARROWER_THAN)) == /;
((NARROWER_THAN)) >| Derivation == Direct
```

## Semantics

The endpoints are declared kinds supporting narrowing; a Property does not narrow. The narrower kind inherits applicable constraints.



Forward `Host ((NARROWER_THAN)) Target` and reverse `Target <((NARROWER_THAN)) Host` are views of the same Relation fact.
In `X/Y`, Y NARROWER_THAN X; traversal runs from broader to narrower.
NARROWER_THAN relates narrower declared kind to broader declared kind.

