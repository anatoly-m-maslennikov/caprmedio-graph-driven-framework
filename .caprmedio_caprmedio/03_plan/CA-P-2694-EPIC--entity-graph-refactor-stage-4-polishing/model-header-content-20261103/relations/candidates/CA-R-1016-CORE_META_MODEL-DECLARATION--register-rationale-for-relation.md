---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//rationale_for
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 31
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
atom_id: CA-R-1016
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register rationale_for relation

## Claim

### Formal Claim

```CFEL
Relation//rationale_for ((HAS_CLASSIFICATION)) Derivation == Direct;

Atom/(.Header.Role: "Analysis & Advisory")/(.Header.Form: Rationale)// ((rationale_for)) Atom//
```

### Prose Claim

#### Applicability
Rationale For Relation.

`rationale_for` **means** the direct relation from a Rationale Analysis & Advisory Atom
to the Atom that it explains.

Forward `Host ((rationale_for)) Target` and reverse `Target <((rationale_for)) Host` are views of the same Relation fact.
rationale_for relates Rationale Analysis & Advisory Atom to explained Atom.
