---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//evaluation_for
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom.Tier
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1018
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register Evaluation targets

## Claim scope

direct `evaluation_for` relations.

## Claim

`evaluation_for` **means** the direct relation from an Evaluation Atom to an
Atom whose authority the Evaluation checks.

```CFEL
((evaluation_for)) >| Derivation == Direct;

Atom/(.Role: Evaluation)// ((evaluation_for)) Atom//
```

## Semantics


Forward `Host ((evaluation_for)) Target` and reverse `Target <((evaluation_for)) Host` are views of the same Relation fact.
evaluation_for relates Evaluation Atom to Atom whose authority is evaluated.

