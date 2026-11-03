---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//method_for
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 30
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1017
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Register method_for relation

## Claim

### Formal Claim

```CFEL
Relation//method_for ((HAS_CLASSIFICATION)) Derivation == Direct;

Atom/(.Header.Role: Method)// ((method_for)) Atom/(.Header.Role: Requirement)//
```

### Prose Claim

#### Applicability
Method For Relation.

`method_for` **means** the direct relation from a Method Atom to the
Requirement Atom that the Method serves.

Forward `Host ((method_for)) Target` and reverse `Target <((method_for)) Host` are views of the same Relation fact.
method_for relates Method Atom to served Requirement Atom.
