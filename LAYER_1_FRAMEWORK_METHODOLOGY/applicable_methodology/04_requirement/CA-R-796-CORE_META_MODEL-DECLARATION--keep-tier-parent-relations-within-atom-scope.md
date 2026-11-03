---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//child_of
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Claim Scope
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-796-CORE_META_MODEL-DECLARATION--keep-tier-parent-relations-within-atom-scope.md
  source_atom_id: CA-R-796
  source_atom_revision: 43
  source_sha256: a0f21fd75cce43e50f07bee22413daa06a5c2313d52e0c3160153e845325cc91
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Keep tier-parent relations within Atom Scope

## Claim scope

The existing governing child_of relation, pending its separately planned replacement.

## Claim

child_of is the directed governing connection from a child Atom to the parent Atom whose Claim governs that child's contribution. It is distinct from containment, dependency, classification and source-layer membership. The Atom definition CA-R-2508 and ordering definition CA-R-2149 govern endpoint admission and ordering. This definition preserves the existing relation until its separate replacement Epic; it does not migrate its actual links.

```CFEL
Atom// ((child_of)) Atom//;

((child_of)) >| Derivation == Direct
```

## Semantics


Forward `Host ((child_of)) Target` and reverse `Target <((child_of)) Host` are views of the same Relation fact.
child_of relates child Atom to parent Atom.

