---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//implementation_of
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 31
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
atom_id: CA-R-1020
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1020-CORE_META_MODEL-DECLARATION--register-implementation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Register implementation_of relation

## Claim

### Formal Claim

```CFEL
Relation//implementation_of ((HAS_CLASSIFICATION)) Derivation == Direct;
Carrier//$implementation_carrier ((implementation_of)) Atom//$specification_atom
```

### Prose Claim

implementation_of is the direct Relation owned by a governed Implementation Carrier. The Host is that governed Implementation Carrier and each tuple targets the specification Atom it implements.

These are endpoint permissions. They are not extra fields on a reusable Relation Type and do not authorize an additional storage fact for a derived inverse. Forward `Host ((implementation_of)) Target` and reverse `Target <((implementation_of)) Host` are written views of the same direct fact.
