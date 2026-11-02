---
atom_id: CA-R-2477
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//HAS_CLASSIFICATION
version: 4
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define classification and its written reverse

## Claim

HAS_CLASSIFICATION relates a declared Entity or instance to an applicable classification axis. `Entity >| Axis` and `Axis |< Entity` are opposite written views of the same fact. An axis is distinct from its value case.

```CFEL
$classified ((HAS_CLASSIFICATION)) $axis

((HAS_CLASSIFICATION)) == >|

((HAS_CLASSIFICATION)) >| Derivation == Direct
```

## Semantics

The Target is an applicable classification axis; the classified Entity may be a Relation or another declared Entity.


Forward `Host ((HAS_CLASSIFICATION)) Target` and reverse `Target <((HAS_CLASSIFICATION)) Host` are views of the same Relation fact.
HAS_CLASSIFICATION relates declared Entity or instance to applicable classification axis.

