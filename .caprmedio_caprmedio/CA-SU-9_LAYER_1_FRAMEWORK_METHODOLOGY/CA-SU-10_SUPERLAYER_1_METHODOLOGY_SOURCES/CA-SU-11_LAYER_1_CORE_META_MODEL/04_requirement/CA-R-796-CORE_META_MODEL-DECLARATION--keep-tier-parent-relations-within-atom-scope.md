---
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//child_of
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
version: 44
updated_at: 2026-11-03 20:00:05 +0400
relations:
  child_of:
  - CA-R-1174
atom_id: CA-R-796
ref_id: CA-R-796
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-796-CORE_META_MODEL-DECLARATION--keep-tier-parent-relations-within-atom-scope.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Keep tier-parent relations within Atom Scope

## Claim

### Formal Claim

```CFEL
# model
Relation//child_of ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$atom ((child_of)) Atom//$atom_2;
```

### Prose Claim

#### Applicability
The existing governing child_of relation, pending its separately planned replacement.

child_of is the directed governing connection from a child Atom to the parent Atom whose Claim governs that child's contribution. It is distinct from containment, dependency, classification and source-layer membership. The Atom definition CA-R-2508 and ordering definition CA-R-2149 govern endpoint admission and ordering. This definition preserves the existing relation until its separate replacement Epic; it does not migrate its actual links.

Forward `Host ((child_of)) Target` and reverse `Target <((child_of)) Host` are views of the same Relation fact.
child_of relates child Atom to parent Atom.
