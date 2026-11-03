---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//child_of
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Content.Claim Scope
version: 43
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-R-1174
atom_id: CA-R-796
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
---
## Summary

Keep tier-parent relations within Atom Scope

## Claim

### Formal Claim

```CFEL
Atom// ((child_of)) Atom//;

Relation//child_of ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

#### Applicability
The existing governing child_of relation, pending its separately planned replacement.

child_of is the directed governing connection from a child Atom to the parent Atom whose Claim governs that child's contribution. It is distinct from containment, dependency, classification and source-layer membership. The Atom definition CA-R-2508 and ordering definition CA-R-2149 govern endpoint admission and ordering. This definition preserves the existing relation until its separate replacement Epic; it does not migrate its actual links.

Forward `Host ((child_of)) Target` and reverse `Target <((child_of)) Host` are views of the same Relation fact.
child_of relates child Atom to parent Atom.
