---
subjects:
  active: CFEL <+ Relation//evidence_for
  passive:
  - CFEL > Relation
version: 29
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
atom_id: CA-R-1021
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register evidence_for relation

## Claim scope

`evidence_for` relations.

## Claim

`evidence_for` **means** the direct relation from an Evidence carrier to the
carrier that the Evidence supports.

```CFEL
((evidence_for)) >| Derivation == Direct

$evidence_carrier ((evidence_for)) Carrier//
```

## Semantics



The Host is an Evidence carrier; the target is the carrier it supports.
Forward `Host ((evidence_for)) Target` and reverse `Target <((evidence_for)) Host` are views of the same Relation fact.
evidence_for relates Evidence carrier to supported carrier.

